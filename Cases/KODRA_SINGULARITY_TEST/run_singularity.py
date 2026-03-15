#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
run_singularity.py — Injecte la formule maîtresse sur le point zéro (R=0) via le portail KoDRA.
Trou noir de Schwarzschild, 10 M_sun, singularité. Dimensions 2^20 (saturation).
Usage: python run_singularity.py
       ou: python Cases/KODRA_SINGULARITY_TEST/run_singularity.py
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
    case_name = "KODRA_SINGULARITY_TEST"
    print("[run_singularity] Running KoDRA (portal) on singularity: formula at R=0, 2^20 dimensions.")
    kodra.run_case(case_name, {})
    print("[run_singularity] Done. See results/ for density at R=0 and Unicity Norm.")

if __name__ == "__main__":
    main()
