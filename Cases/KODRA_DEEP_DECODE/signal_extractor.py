#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
signal_extractor.py — Isole les harmoniques du signal à norme 0.85 (1.42 GHz).
Lance KoDRA sur KODRA_DEEP_DECODE pour extraire les composantes spectrales.
Usage: python signal_extractor.py
       ou: python Cases/KODRA_DEEP_DECODE/signal_extractor.py
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
    case_name = "KODRA_DEEP_DECODE"
    print("[signal_extractor] Extracting harmonics from Unicity Signal (Norm 0.85, 1.42 GHz) via KoDRA.")
    kodra.run_case(case_name, {})
    print("[signal_extractor] Done. Harmoniques isolées; run decode_content.py for Message Type, Distance, Sync Rate.")

if __name__ == "__main__":
    main()
