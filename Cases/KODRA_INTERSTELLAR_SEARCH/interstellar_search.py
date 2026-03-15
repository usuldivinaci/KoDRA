#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
interstellar_search.py — Lance KoDRA sur KODRA_INTERSTELLAR_SEARCH et cherche
une Norme KODra > 0.50 dans le signal reçu (Signature d'Unicité - Type II Kardashev).
Usage: python interstellar_search.py
       ou: python Cases/KODRA_INTERSTELLAR_SEARCH/interstellar_search.py
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
    case_name = "KODRA_INTERSTELLAR_SEARCH"
    print("[interstellar_search] Running KoDRA: 500k+ dimensions, 1.42 GHz, QFT via Zero-Portal, sensitivity 1e-24 W.")
    kodra.run_case(case_name, {})
    # Lire le résultat (Norm > 0.50 ?)
    signal_path = os.path.join(_script_dir, "interstellar_signal.json")
    if os.path.exists(signal_path):
        with open(signal_path, "r", encoding="utf-8") as f:
            result = json.load(f)
        norm = result.get("unicity_norm", 0)
        threshold = result.get("threshold", 0.50)
        detected = result.get("signal_detected", False)
        print("\n" + "=" * 60)
        print("  RÉSULTAT INTERSTELLAR SEARCH")
        print("  Norme KODra reçue : {:.6f}".format(norm))
        print("  Seuil (Type II)   : > {:.2f}".format(threshold))
        if detected:
            print("  >>> Signature d'Unicité DÉTECTÉE (candidat Type II - Kardashev)")
        else:
            print("  >>> Pas de signal au-dessus du seuil (bruit cosmique)")
        print("=" * 60)
    else:
        print("[interstellar_search] Run terminé. Consulter results/ pour la Norme KODra.")

if __name__ == "__main__":
    main()
