#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
social_stabilizer.py — Réduit le Risque de crise sociale (+8%) en optimisant
la distribution des ressources via le portail KoDRA.
Affiche en console : New Social Risk (%), GHI, KODra Unicity Status.
Usage: python social_stabilizer.py
       ou: python Cases/KODRA_GLOBAL_IMPACT/social_stabilizer.py
"""
import os
import sys

_script_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(os.path.dirname(_script_dir))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

def main():
    from KoDRA import KoDRA
    kodra = KoDRA()
    case_name = "KODRA_GLOBAL_IMPACT"
    print("[social_stabilizer] Running KoDRA (portal) to optimize resource distribution and reduce social risk.")
    kodra.run_case(case_name, {})
    # Les résultats (New Social Risk %, GHI, KODra Unicity Status) sont affichés
    # par run_case dans la console et dans results/
    report_path = os.path.join(_script_dir, "FINAL_REPORT.md")
    if os.path.exists(report_path):
        with open(report_path, "r", encoding="utf-8") as f:
            print("\n[social_stabilizer] --- FINAL_REPORT.md ---\n" + f.read())
    print("[social_stabilizer] Done. New Social Risk (%), GHI, KODra Unicity Status ci-dessus et dans results/.")

if __name__ == "__main__":
    main()
