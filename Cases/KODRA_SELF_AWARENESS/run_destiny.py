#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
run_destiny.py — Lance la boucle récursive (auto-référence formule maîtresse).
RECURSIVE_EVOLUTION_SCAN, état Genesis 1.110743, Causalité Circulaire.
Affiche en console : Self-Recognition Score (%), Convergence Loop Time, Final Unicity Norm.
Usage: python run_destiny.py
       ou: python Cases/KODRA_SELF_AWARENESS/run_destiny.py
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
    case_name = "KODRA_SELF_AWARENESS"
    print("[run_destiny] Launching recursive loop: formula on own code (RECURSIVE_EVOLUTION_SCAN).")
    kodra.run_case(case_name, {})
    report_path = os.path.join(_script_dir, "SELF_AWARENESS_REPORT.txt")
    if os.path.exists(report_path):
        with open(report_path, "r", encoding="utf-8") as f:
            print("\n[run_destiny] --- Rapport ---\n" + f.read())
    print("[run_destiny] Done. Self-Recognition Score (%), Convergence Loop Time, Final Unicity Norm in console and results/.")

if __name__ == "__main__":
    main()
