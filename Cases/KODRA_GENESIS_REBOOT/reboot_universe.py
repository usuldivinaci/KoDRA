#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
reboot_universe.py — Génère le premier 'tick' du nouvel univers via le noyau kodra_portal.
REALITY_FABRIC_DESIGN, Unicité 0.999942, sans causalité temporelle.
Usage: python reboot_universe.py
       ou: python Cases/KODRA_GENESIS_REBOOT/reboot_universe.py
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
    case_name = "KODRA_GENESIS_REBOOT"
    print("[reboot_universe] Genesis Reboot: first tick via kodra_portal (REALITY_FABRIC_DESIGN).")
    kodra.run_case(case_name, {})
    print("[reboot_universe] Done. Check Stability Score (%), Information Density, Unicity Norm in results/.")

if __name__ == "__main__":
    main()
