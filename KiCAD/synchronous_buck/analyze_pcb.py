import sys
import math
from pathlib import Path
from collections import defaultdict


def parse_sexpr(text: str):
    tokens = []
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if c.isspace():
            i += 1
        elif c in "()":
            tokens.append(c)
            i += 1
        elif c == '"':
            i += 1
            buf = []
            while i < n:
                if text[i] == "\\" and i + 1 < n:
                    buf.append(text[i + 1])
                    i += 2
                elif text[i] == '"':
                    i += 1
                    break
                else:
                    buf.append(text[i])
                    i += 1
            tokens.append(("STR", "".join(buf)))
        else:
            start = i
            while i < n and not text[i].isspace() and text[i] not in '()"':
                i += 1
            tokens.append(text[start:i])

    stack = [[]]
    for tok in tokens:
        if tok == "(":
            new_list = []
            stack[-1].append(new_list)
            stack.append(new_list)
        elif tok == ")":
            if len(stack) > 1:
                stack.pop()
        elif isinstance(tok, tuple) and tok[0] == "STR":
            stack[-1].append(tok[1])
        else:
            stack[-1].append(tok)
    return stack[0][0] if stack[0] else []


def get_sub(node, key: str):
    for item in node:
        if isinstance(item, list) and item and item[0] == key:
            return item
    return None


def get_subs(node, key: str):
    return [item for item in node if isinstance(item, list) and item and item[0] == key]


def resolve_net_name(net_node, name_node, nets_by_id: dict) -> str:
    if name_node and len(name_node) > 1 and name_node[1]:
        return name_node[1]
    if not net_node or len(net_node) < 2:
        return ""
    val = net_node[1]
    try:
        nid = int(val)
        return net_node[2] if len(net_node) > 2 else nets_by_id.get(nid, "")
    except ValueError:
        return val


def analyze_pcb(pcb_path: Path) -> str:
    raw = pcb_path.read_text(encoding="utf-8", errors="replace")
    tree = parse_sexpr(raw)

    nets_by_id = {}
    all_net_names = set()
    layers = []
    footprints = []
    segments = []
    vias = []
    zones = []
    edge_pts = []

    def collect_edge_pts(item):
        layer_node = get_sub(item, "layer")
        if layer_node and len(layer_node) > 1 and layer_node[1] == "Edge.Cuts":
            for key in ("start", "end", "mid", "center"):
                pt = get_sub(item, key)
                if pt and len(pt) >= 3:
                    try:
                        edge_pts.append((float(pt[1]), float(pt[2])))
                    except ValueError:
                        pass
            pts_node = get_sub(item, "pts")
            if pts_node:
                for xy in get_subs(pts_node, "xy"):
                    if len(xy) >= 3:
                        try:
                            edge_pts.append((float(xy[1]), float(xy[2])))
                        except ValueError:
                            pass

    for item in tree[1:]:
        if not isinstance(item, list) or not item:
            continue
        tag = item[0]

        if tag == "layers":
            for l in item[1:]:
                if isinstance(l, list) and len(l) >= 3:
                    layers.append((l[0], l[1], l[2]))

        elif tag == "net" and len(item) >= 3:
            try:
                nets_by_id[int(item[1])] = item[2]
            except ValueError:
                pass
            if item[2]:
                all_net_names.add(item[2])

        elif tag == "footprint":
            fp_name = item[1] if len(item) > 1 else ""
            layer_n = get_sub(item, "layer")
            fp_layer = layer_n[1] if layer_n and len(layer_n) > 1 else "?"
            at_n = get_sub(item, "at")
            x = float(at_n[1]) if at_n and len(at_n) > 1 else 0.0
            y = float(at_n[2]) if at_n and len(at_n) > 2 else 0.0
            rot = float(at_n[3]) if at_n and len(at_n) > 3 else 0.0

            ref, val = "?", "?"
            for prop in get_subs(item, "property"):
                if len(prop) >= 3:
                    if prop[1] == "Reference":
                        ref = prop[2]
                    elif prop[1] == "Value":
                        val = prop[2]
            if ref == "?" or val == "?":
                for fpt in get_subs(item, "fp_text"):
                    if len(fpt) >= 3:
                        if fpt[1] == "reference" and ref == "?":
                            ref = fpt[2]
                        elif fpt[1] == "value" and val == "?":
                            val = fpt[2]

            pads = []
            for pad in get_subs(item, "pad"):
                pad_num = pad[1] if len(pad) > 1 else "?"
                pad_type = pad[2] if len(pad) > 2 else "?"
                net_name = resolve_net_name(get_sub(pad, "net"), None, nets_by_id)
                if net_name:
                    all_net_names.add(net_name)
                pads.append((pad_num, pad_type, net_name))

            for sub in item[1:]:
                if isinstance(sub, list) and sub and sub[0].startswith("fp_"):
                    collect_edge_pts(sub)

            footprints.append({
                "ref": ref,
                "val": val,
                "fp": fp_name,
                "layer": fp_layer,
                "x": x,
                "y": y,
                "rot": rot,
                "pads": pads,
            })

        elif tag in ("segment", "arc"):
            st = get_sub(item, "start")
            en = get_sub(item, "end")
            wi = get_sub(item, "width")
            la = get_sub(item, "layer")
            net_name = resolve_net_name(get_sub(item, "net"), None, nets_by_id)
            if net_name:
                all_net_names.add(net_name)
            if st and en and wi and la:
                dx = float(en[1]) - float(st[1])
                dy = float(en[2]) - float(st[2])
                segments.append({
                    "len": math.hypot(dx, dy),
                    "width": float(wi[1]),
                    "layer": la[1],
                    "net": net_name,
                })

        elif tag == "via":
            si = get_sub(item, "size")
            dr = get_sub(item, "drill")
            la = get_sub(item, "layers")
            net_name = resolve_net_name(get_sub(item, "net"), None, nets_by_id)
            if net_name:
                all_net_names.add(net_name)
            vias.append({
                "size": float(si[1]) if si and len(si) > 1 else 0.0,
                "drill": float(dr[1]) if dr and len(dr) > 1 else 0.0,
                "layers": la[1:] if la else [],
                "net": net_name,
            })

        elif tag == "zone":
            net_name = resolve_net_name(get_sub(item, "net"), get_sub(item, "net_name"), nets_by_id)
            if net_name:
                all_net_names.add(net_name)
            la = get_sub(item, "layer")
            las = get_sub(item, "layers")
            filled = len(get_subs(item, "filled_polygon")) > 0
            z_layers = [la[1]] if la and len(la) > 1 else (las[1:] if las else [])
            zones.append({
                "net_name": net_name,
                "layers": z_layers,
                "filled": filled,
            })

        elif tag.startswith("gr_"):
            collect_edge_pts(item)

    lines = [f"# KiCad PCB Analiz Raporu: `{pcb_path.name}`\n"]

    # 1. Kart Boyutları ve Katmanlar
    lines.append("## 1. Kart Boyutları ve Katman Yapısı")
    if edge_pts:
        xs = [p[0] for p in edge_pts]
        ys = [p[1] for p in edge_pts]
        w = max(xs) - min(xs)
        h = max(ys) - min(ys)
        lines.append(f"- **Kart Sınırı (Edge.Cuts):** {w:.2f} mm x {h:.2f} mm (X: {min(xs):.1f}..{max(xs):.1f}, Y: {min(ys):.1f}..{max(ys):.1f})")
    else:
        lines.append("- **Kart Sınırı (Edge.Cuts):** Tanımlı sınır bulunamadı.")

    cu_layers = [f"{l[1]} ({l[2]})" for l in layers if l[1].endswith(".Cu")]
    lines.append(f"- **Bakır Katmanlar ({len(cu_layers)}):** {', '.join(cu_layers)}")
    lines.append(f"- **Toplam Eleman:** {len(footprints)} | **Yol Segmenti:** {len(segments)} | **Via:** {len(vias)} | **Zone:** {len(zones)}\n")

    # 2. Bakır Dolgular (Zones)
    lines.append("## 2. Bakır Dolgular (Copper Zones)")
    if zones:
        for z in zones:
            status = "Dolu (Filled)" if z["filled"] else "BOŞ / Doldurulmamış (B tuşuna basılmalı)"
            lines.append(f"- **Net:** `{z['net_name']}` | **Katman:** {', '.join(z['layers'])} | **Durum:** {status}")
    else:
        lines.append("- Kartta tanımlı copper zone bulunamadı.")
    lines.append("")

    # 3. Net Bazlı Yol Kalınlıkları, Uzunluklar ve Katman Dağılımı
    lines.append("## 3. Net Bazlı Yol (Track) ve Via Özeti")
    lines.append("| Net Adı | Pad Sayısı | Segment | Toplam Uzunluk (mm) | Yol Kalınlıkları (mm) | Kullanılan Katmanlar | Via Sayısı |")
    lines.append("| :--- | :---: | :---: | :---: | :--- | :--- | :---: |")

    pad_counts = defaultdict(int)
    unconnected_pads = []
    for fp in footprints:
        for p_num, p_type, n_name in fp["pads"]:
            if p_type == "np_thru_hole":
                continue
            if not n_name or n_name.startswith("unconnected-"):
                unconnected_pads.append(f"{fp['ref']}-Pin{p_num} ({fp['val']}) -> `{n_name or 'BOŞ'}`")
            else:
                pad_counts[n_name] += 1

    seg_by_net = defaultdict(list)
    for s in segments:
        seg_by_net[s["net"]].append(s)

    vias_by_net = defaultdict(list)
    for v in vias:
        vias_by_net[v["net"]].append(v)

    sorted_nets = sorted(
        [n for n in all_net_names if n and not n.startswith("unconnected-")],
        key=lambda n: (-len(seg_by_net[n]), n)
    )

    for n_name in sorted_nets:
        segs = seg_by_net[n_name]
        tot_len = sum(s["len"] for s in segs)
        widths = sorted({round(s["width"], 3) for s in segs})
        w_str = ", ".join(f"{w:g}" for w in widths) if widths else "-"
        used_layers = sorted({s["layer"] for s in segs})
        l_str = ", ".join(used_layers) if used_layers else "Yol Yok (Unrouted)"
        v_cnt = len(vias_by_net[n_name])
        lines.append(f"| `{n_name}` | {pad_counts[n_name]} | {len(segs)} | {tot_len:.1f} | {w_str} | {l_str} | {v_cnt} |")
    lines.append("")

    # 4. Bağlantısız Pinler
    lines.append("## 4. Bağlantısız (Unconnected) Pinler")
    if unconnected_pads:
        for up in unconnected_pads:
            lines.append(f"- {up}")
    else:
        lines.append("- Bağlantısız pin tespit edilmedi.")
    lines.append("")

    # 5. Via Ölçüleri Özeti
    lines.append("## 5. Via Ölçü Dağılımı")
    via_specs = defaultdict(int)
    for v in vias:
        via_specs[(v["size"], v["drill"], "->".join(v["layers"]))] += 1
    if via_specs:
        for (sz, dr, ly), cnt in sorted(via_specs.items(), key=lambda x: -x[1]):
            lines.append(f"- **Çap/Delik:** {sz:g} mm / {dr:g} mm ({ly}) — **{cnt} adet**")
    else:
        lines.append("- Kartta via bulunamadı.")
    lines.append("")

    # 6. Komponent Yerleşimi ve Bağlantı Haritası
    lines.append("## 6. Komponent Listesi ve Yerleşim")
    lines.append("| Ref | Değer | Footprint | Katman | Konum (X, Y) | Rot | Pin Bağlantıları |")
    lines.append("| :--- | :--- | :--- | :---: | :---: | :---: | :--- |")

    for fp in sorted(footprints, key=lambda f: f["ref"]):
        conn_list = []
        for p_num, p_type, n_name in fp["pads"]:
            if p_type == "np_thru_hole":
                continue
            short_net = n_name if n_name else "NC"
            conn_list.append(f"{p_num}:{short_net}")
        conn_str = ", ".join(conn_list)
        fp_short = fp["fp"].split(":")[-1]
        lines.append(
            f"| **{fp['ref']}** | {fp['val']} | `{fp_short}` | {fp['layer']} | ({fp['x']:.1f}, {fp['y']:.1f}) | {fp['rot']:g}° | {conn_str} |"
        )

    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        pcb_files = list(Path(".").glob("*.kicad_pcb"))
        if not pcb_files:
            print("Kullanım: python analyze_pcb.py <dosya_adi.kicad_pcb>")
            sys.exit(1)
        target = pcb_files[0]
    else:
        target = Path(sys.argv[1])

    if not target.exists():
        print(f"Hata: '{target}' bulunamadı.")
        sys.exit(1)

    report = analyze_pcb(target)
    out_file = target.with_name("pcb_analysis_report.md")
    out_file.write_text(report, encoding="utf-8")
    print(report)
    print(f"\n[OK] Rapor kaydedildi: {out_file.resolve()}")