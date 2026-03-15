# -*- coding: utf-8 -*-
"""
Handler: run factoriser <N>
Crée un dossier Cases/Factoriser_<N>/ avec input.json, puis KoDRA exécute le cas.
"""
import os
import json
import time


def run(args, cases_dir):
    """
    Args: ["1005973"] ou ["12345"]
    Retourne le nom du cas créé, ou None en cas d'erreur.
    """
    if not args:
        print("[USAGE] run factoriser <nombre>")
        print("        Ex: run factoriser 1005973")
        return None

    try:
        N = int(args[0])
    except ValueError:
        print("[ERREUR] Le premier argument doit être un entier.")
        return None

    if N < 2:
        print("[ERREUR] N doit être >= 2.")
        return None

    case_name = f"Factoriser_{N}"
    case_path = os.path.join(cases_dir, case_name)
    os.makedirs(case_path, exist_ok=True)

    data = {
        "case_type": "QUANTUM_MATH_REAL",
        "target_integer": N,
        "source": f"Commande: run factoriser {N}",
        "description": f"Factorisation de l'entier {N} via KoDRA",
        "created": time.ctime()
    }

    input_path = os.path.join(case_path, "input.json")
    with open(input_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return case_name
