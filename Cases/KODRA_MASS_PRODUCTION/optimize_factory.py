#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
optimize_factory.py — Mappe la production de 120 millions de doses via KoDRA.
Affiche Production Yield (%) et Norme KODra (voir mini-site results/).
Usage: python optimize_factory.py
       ou: python Cases/KODRA_MASS_PRODUCTION/optimize_factory.py
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
    case_name = "KODRA_MASS_PRODUCTION"
    target_doses_millions = 120
    print(f"[optimize_factory] Running KoDRA to optimize production mapping for {target_doses_millions} million doses.")
    kodra.run_case(case_name, {})
    print(f"[optimize_factory] Done. Consulter results/ pour : Norme KODra, Safety Score (%), Production Yield (%).")

if __name__ == "__main__":
    main()
