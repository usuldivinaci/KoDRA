#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
decode_content.py — Utilise le portail KoDRA pour traduire les phases quantiques
en données lisibles (Texte, Math, Image). Affiche en console : Message Type, Source Distance, KODra Sync Rate.
Usage: python decode_content.py
       ou: python Cases/KODRA_DEEP_DECODE/decode_content.py
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
    case_name = "KODRA_DEEP_DECODE"
    print("[decode_content] Running KoDRA (portal) to decode quantum phases → readable data.")
    kodra.run_case(case_name, {})
    # Afficher les résultats attendus (console)
    decoded_path = os.path.join(_script_dir, "decoded_data.json")
    if os.path.exists(decoded_path):
        with open(decoded_path, "r", encoding="utf-8") as f:
            d = json.load(f)
        print("\n" + "=" * 60)
        print("  RÉSULTATS DEEP DECODE (Console)")
        print("  Message Type      :", d.get("message_type", "N/A"))
        print("  Source Distance   :", str(d.get("source_distance_ly", "N/A")) + " années-lumière")
        print("  KODra Sync Rate   :", str(d.get("kodra_sync_rate_percent", "N/A")) + " %")
        print("=" * 60)
    else:
        print("[decode_content] Run terminé. Consulter results/ et decoded_data.json après exécution.")

if __name__ == "__main__":
    main()
