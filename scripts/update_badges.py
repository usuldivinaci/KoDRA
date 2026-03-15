#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Met à jour les badges "Case Performance Badge" dans les README.md des cas KoDRA
à partir de last_run_metrics.json (écrit par KoDRA après chaque run) ou en parsant
results/results.html et results/index.html.
Usage: python scripts/update_badges.py [--dry-run] [case_name]
"""
import os
import re
import json
import argparse

def find_project_root():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(script_dir)
    if os.path.isdir(os.path.join(root, "Cases")) and os.path.isfile(os.path.join(root, "KoDRA.py")):
        return root
    # Si on lance depuis la racine
    if os.path.isdir("Cases") and os.path.isfile("KoDRA.py"):
        return os.path.abspath(".")
    return root

def load_last_run_metrics(case_path):
    path = os.path.join(case_path, "last_run_metrics.json")
    if not os.path.isfile(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def parse_results_html(case_path):
    """Extrait norm, duration_sec, status depuis results/results.html et results/index.html."""
    out = {}
    results_dir = os.path.join(case_path, "results")
    # results.html : <tr><td>Unicity State Norm (KODra)</td><td>0.793887</td></tr>
    results_html = os.path.join(results_dir, "results.html")
    if os.path.isfile(results_html):
        with open(results_html, "r", encoding="utf-8") as f:
            html = f.read()
        for key, re_key in [
            ("unicity_norm", r"Unicity State Norm \(KODra\)</td><td[^>]*>([^<]+)"),
            ("status", r"Classical/QC Status</td><td[^>]*>([^<]+)"),
        ]:
            m = re.search(re_key, html)
            if m:
                val = m.group(1).strip()
                if key == "unicity_norm":
                    try:
                        out[key] = float(val)
                    except ValueError:
                        out[key] = val
                else:
                    out[key] = val
    # index.html : Durée (s), Norme Unicité
    index_html = os.path.join(results_dir, "index.html")
    if os.path.isfile(index_html):
        with open(index_html, "r", encoding="utf-8") as f:
            html = f.read()
        if "duration_sec" not in out:
            m = re.search(r"Durée \(s\)</td><td[^>]*>([^<]+)", html)
            if m:
                try:
                    out["duration_sec"] = float(m.group(1).strip())
                except ValueError:
                    out["duration_sec"] = m.group(1).strip()
        if "unicity_norm" not in out:
            m = re.search(r"Norme Unicité</td><td[^>]*>([^<]+)", html)
            if m:
                try:
                    out["unicity_norm"] = float(m.group(1).strip())
                except ValueError:
                    out["unicity_norm"] = m.group(1).strip()
    return out if out else None

def parse_report_txt(case_path):
    """Optionnel: extrait depuis *_REPORT.txt (ex. SELF_AWARENESS)."""
    for fname in os.listdir(case_path):
        if fname.endswith("_REPORT.txt") or fname == "SELF_AWARENESS_REPORT.txt":
            path = os.path.join(case_path, fname)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()
            except Exception:
                continue
            out = {}
            m = re.search(r"Final Unicity Norm:\s*([\d.]+)", text)
            if m:
                out["unicity_norm"] = float(m.group(1))
            m = re.search(r"Convergence Loop Time:\s*([\d.]+)\s*s", text)
            if m:
                out["duration_sec"] = float(m.group(1))
            m = re.search(r"Self-Recognition Score \(%\):\s*([\d.]+)", text)
            if m:
                out["self_recognition"] = float(m.group(1))
            if out:
                return out
    return None

def get_metrics_for_case(case_path):
    metrics = load_last_run_metrics(case_path)
    if metrics:
        return metrics
    metrics = parse_results_html(case_path)
    if metrics:
        return metrics
    return parse_report_txt(case_path)

def format_badge_value(val):
    if val is None:
        return "*Mettre à jour après run*"
    if isinstance(val, float):
        if val >= 1e6:
            return f"{val:,.0f}"
        if val >= 1:
            return f"{val:.4f}"
        return f"{val:.6f}"
    return str(val)

def update_readme_badge(readme_path, metrics, case_name):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    if "## 📊 Case Performance Badge" not in content:
        return False, "No badge section"

    norm_str = format_badge_value(metrics.get("unicity_norm") if metrics else None)
    duration = metrics.get("duration_sec") if metrics else None
    if duration is not None:
        exec_str = f"{float(duration):.4f} s"
    else:
        exec_str = "*Mettre à jour après run*"
    status_str = (metrics.get("status") or "✅ Classical: Résolu (KODra Hybrid)").strip()
    if status_str and not status_str.startswith("✅"):
        status_str = "✅ " + status_str

    # Remplacer les lignes du tableau: Stability (Norm), Exec Time, Status (remplacement de ligne entière)
    lines = content.split("\n")
    new_lines = []
    in_badge = False
    for line in lines:
        if "## 📊 Case Performance Badge" in line:
            in_badge = True
        if in_badge and line.strip().startswith("|") and "**Stability (Norm)**" in line:
            line = "| **Stability (Norm)** | " + norm_str + " |"
        elif in_badge and line.strip().startswith("|") and "**Exec Time**" in line:
            line = "| **Exec Time** | " + exec_str + " |"
        elif in_badge and line.strip().startswith("|") and "**Status**" in line:
            line = "| **Status** | " + status_str + " |"
        if in_badge and "*Mettre à jour les valeurs" in line:
            in_badge = False
        new_lines.append(line)
    new_content = "\n".join(new_lines)
    if new_content == content:
        return False, "No change"
    return True, new_content

def main():
    parser = argparse.ArgumentParser(description="Update Case Performance Badges in case READMEs from last run or results HTML.")
    parser.add_argument("--dry-run", action="store_true", help="Only print what would be updated")
    parser.add_argument("case_name", nargs="?", help="Optional: update only this case folder name")
    args = parser.parse_args()
    root = find_project_root()
    cases_dir = os.path.join(root, "Cases")
    if not os.path.isdir(cases_dir):
        print(f"[ERREUR] Dossier Cases introuvable: {cases_dir}")
        return 1
    to_scan = []
    if args.case_name:
        case_path = os.path.join(cases_dir, args.case_name)
        if os.path.isdir(case_path):
            to_scan.append((args.case_name, case_path))
        else:
            print(f"[ERREUR] Cas introuvable: {args.case_name}")
            return 1
    else:
        for name in sorted(os.listdir(cases_dir)):
            path = os.path.join(cases_dir, name)
            if not os.path.isdir(path):
                continue
            readme = os.path.join(path, "README.md")
            if os.path.isfile(readme):
                try:
                    with open(readme, "r", encoding="utf-8") as f:
                        if "Case Performance Badge" in f.read():
                            to_scan.append((name, path))
                except Exception:
                    pass
    updated = 0
    for name, case_path in to_scan:
        readme_path = os.path.join(case_path, "README.md")
        metrics = get_metrics_for_case(case_path)
        ok, result = update_readme_badge(readme_path, metrics, name)
        if ok is True:
            if not args.dry_run:
                with open(readme_path, "w", encoding="utf-8") as f:
                    f.write(result)
            print(f"  [OK] {name} (norm={format_badge_value(metrics.get('unicity_norm') if metrics else None)}, time={metrics.get('duration_sec') if metrics else '?'}s)")
            updated += 1
        elif ok is False and result == "No change":
            print(f"  [--] {name} (déjà à jour ou pas de données)")
        else:
            print(f"  [??] {name} ({result})")
    print(f"\nBadges mis à jour: {updated}" + (" (dry-run)" if args.dry_run else ""))
    return 0

if __name__ == "__main__":
    exit(main())
