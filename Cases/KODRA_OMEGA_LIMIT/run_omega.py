#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
run_omega.py — Lance KODRA_OMEGA_LIMIT en mode ULTRA_PORTAL_STRESS.
Une itération pour défier la formule (état final entropie). Observer Speedup et RAM.
Usage: python run_omega.py
       ou: python Cases/KODRA_OMEGA_LIMIT/run_omega.py
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
    case_name = "KODRA_OMEGA_LIMIT"
    # Une itération = stress max (challenge "fin des temps en 1 iter")
    options = {"iter": "1"}
    print("[run_omega] ULTRA_PORTAL_STRESS: Running KODRA_OMEGA_LIMIT (1 iteration). Watch Speedup and RAM.")
    kodra.run_case(case_name, options)
    print("[run_omega] Done. Check console for Speedup; results/ for RAM plot and entropy.")

if __name__ == "__main__":
    main()
