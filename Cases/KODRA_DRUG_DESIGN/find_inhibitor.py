#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
find_inhibitor.py — Lance KoDRA sur le cas KODRA_DRUG_DESIGN avec une tolérance 1e-12
pour une précision atomique (conception d'inhibiteur / chélateur anti-tunnel).
Usage: python find_inhibitor.py
       ou depuis la racine du projet: python Cases/KODRA_DRUG_DESIGN/find_inhibitor.py
"""
import os
import sys

# Racine du projet (kodra_PMQC) pour importer KoDRA
_script_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(os.path.dirname(_script_dir))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

def main():
    from KoDRA import KoDRA
    kodra = KoDRA()
    options = {"tolerance": "1e-12"}
    print("[find_inhibitor] Running KoDRA on KODRA_DRUG_DESIGN with tolerance=1e-12 (atomic precision).")
    kodra.run_case("KODRA_DRUG_DESIGN", options)
    print("[find_inhibitor] Done.")

if __name__ == "__main__":
    main()
