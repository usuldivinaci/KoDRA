#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
run_safety_check.py — Valide la non-toxicité via KoDRA (portal de convergence).
Test 1 : Interaction avec cytochromes P450 hépatiques - vise inhibition < 5%.
Usage: python run_safety_check.py
       ou: python Cases/KODRA_MASS_PRODUCTION/run_safety_check.py
"""
import os
import sys
import json

_script_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(os.path.dirname(_script_dir))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

def main():
    from KoDRA import KoDRA
    kodra = KoDRA()
    case_name = "KODRA_MASS_PRODUCTION"
    print("[run_safety_check] Running KoDRA (portal) on KODRA_MASS_PRODUCTION to validate non-toxicity (P450 < 5%).")
    kodra.run_case(case_name, {})
    # Les métriques (Safety Score, Test 1) sont affichées par run_case et dans results/
    # Vérification locale si un résultat récent existe
    results_dir = os.path.join(_script_dir, "results")
    report_path = os.path.join(_script_dir, "MASS_PRODUCTION_REPORT.txt")
    if os.path.exists(report_path):
        with open(report_path, "r", encoding="utf-8") as f:
            print("\n[run_safety_check] --- Rapport production ---\n" + f.read())
    print("[run_safety_check] Done. Vérifier Safety Score (%) et Test 1 (P450) dans le mini-site results/.")

if __name__ == "__main__":
    main()
