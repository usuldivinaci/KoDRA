# -*- coding: utf-8 -*-
"""
Handler KODRA_INTERSTELLAR_SEARCH : Signature d'Unicité (Unicity Signal).
Filtrage du bruit cosmique, 500k+ dimensions, QFT via Zero-Portal.
Recherche d'une norme KODra > 0.50 (signal potentiel Type II - Kardashev).
KoDRA appelle run() si handler.py est présent.
"""
import os
import json

def run(case_name, data, heavy_content, final_state, duration, case_path):
    # Norme KODra sur le signal (état final après convergence)
    unicity_norm = (final_state ** 2).sum().item() ** 0.5
    params = data.get("parameters") or {}
    threshold_cfg = data.get("threshold") or {}
    norm_min = float(threshold_cfg.get("unicity_norm_min", 0.50))
    signal_detected = unicity_norm > norm_min

    metrics = {
        "Objective": data.get("objective", "Unicity Signal - Type II (Kardashev)"),
        "Input (Frequency)": f"{params.get('input_frequency_ghz', 1.42)} GHz ({params.get('input_label', 'Ligne H')})",
        "Algorithm": params.get("algorithm", "QFT via Zero-Portal"),
        "Sensitivity": str(params.get("sensitivity_label", "1e-24 W (Ultra-faible)")),
        "Dimensions (mapping)": f"{params.get('effective_dimensions', 500000):,}+",
        "--- Signal ---": "",
        "Unicity State Norm (KODra)": f"{unicity_norm:.6f}",
        "Threshold (Norm > )": str(norm_min),
        "Unicity Signal Detected": "YES (potential Type II)" if signal_detected else "NO (cosmic noise)",
    }

    # Artifact pour interstellar_search.py : vérifier Norm > 0.50
    signal_result = {
        "unicity_norm": unicity_norm,
        "threshold": norm_min,
        "signal_detected": signal_detected,
        "frequency_ghz": params.get("input_frequency_ghz", 1.42),
        "sensitivity_watts": params.get("sensitivity_watts", 1e-24),
    }
    artifacts = [
        ("interstellar_signal.json", json.dumps(signal_result, indent=2)),
        ("INTERSTELLAR_SEARCH_REPORT.txt", f"""KoDRA | INTERSTELLAR SEARCH - UNICITY SIGNAL
============================================
Case: {case_name}
Input: {params.get('input_frequency_ghz', 1.42)} GHz (Ligne hydrogène)
Algorithm: {params.get('algorithm', 'QFT via Zero-Portal')}
Sensitivity: {params.get('sensitivity_label', '1e-24 W')}
Dimensions (mapping): {params.get('effective_dimensions', 500000)}+

Norme KODra: {unicity_norm:.6f}
Seuil: > {norm_min}
Signature d'Unicité détectée: {'OUI (candidat Type II)' if signal_detected else 'NON (bruit cosmique)'}
"""),
    ]

    domain_report = "KODRA_INTERSTELLAR_SEARCH (Unicity Signal, Type II Kardashev)"
    return domain_report, metrics, artifacts
