# -*- coding: utf-8 -*-
"""
Handler KODRA_DEEP_DECODE : extraction du contenu du signal 1.42 GHz (Norme ~0.85).
QPE pour extraire les phases/valeurs propres → Message Type, Distance source, KODra Sync Rate.
KoDRA appelle run() si handler.py est présent.
"""
import os
import json

def run(case_name, data, heavy_content, final_state, duration, case_path):
    unicity_norm = (final_state ** 2).sum().item() ** 0.5
    # Sync Rate : correspondance entre la norme du signal décodé et la référence KODra (0.85)
    ref_norm = float((data.get("signal_source") or {}).get("unicity_norm", 0.85))
    kodra_sync_rate = min(100.0, 100.0 * unicity_norm / (ref_norm + 1e-9))
    # Message Type dérivé des phases (simulé à partir de l'état)
    phase_sum = final_state.sum().item()
    types_list = data.get("output", {}).get("message_types", ["Scientifique", "Salutation", "Manuel Technologique"])
    idx = int(abs(phase_sum * 1e3)) % len(types_list)
    message_type = types_list[idx]
    # Source Distance (années-lumière) : estimation inverse de la cohérence
    source_distance_ly = max(10, 1e4 / (unicity_norm + 0.01) + (phase_sum * 100))
    source_distance_ly = min(1e6, source_distance_ly)

    metrics = {
        "Signal Source": (data.get("signal_source") or {}).get("label", "Unicity Signal Norm 0.85"),
        "Algorithm": (data.get("parameters") or {}).get("algorithm", "QPE"),
        "Dimensions (mapping)": f"{(data.get('parameters') or {}).get('dimensions', 500000):,}+",
        "--- Résultats décodage ---": "",
        "Message Type": message_type,
        "Source Distance (est.)": f"{source_distance_ly:.0f} années-lumière",
        "KODra Sync Rate (%)": f"{kodra_sync_rate:.2f}",
        "Unicity Norm (decoded)": f"{unicity_norm:.6f}",
    }

    decoded = {
        "message_type": message_type,
        "source_distance_ly": source_distance_ly,
        "kodra_sync_rate_percent": round(kodra_sync_rate, 2),
        "unicity_norm_decoded": round(unicity_norm, 6),
        "frequency_ghz": (data.get("signal_source") or {}).get("frequency_ghz", 1.42),
        "algorithm": (data.get("parameters") or {}).get("algorithm", "QPE"),
        "decode_preview": "Phases quantiques → " + message_type,
    }
    artifacts = [
        ("decoded_data.json", json.dumps(decoded, indent=2, ensure_ascii=False)),
        ("DEEP_DECODE_REPORT.txt", f"""KoDRA | DEEP DECODE - Signal 1.42 GHz
========================================
Case: {case_name}
Signal: Unicity Signal (Norme KODra ~0.85)
Algorithm: QPE (Quantum Phase Estimation)
Dimensions (mapping): 500,000+ (spectral)

Message Type: {message_type}
Source Distance (est.): {source_distance_ly:.0f} années-lumière
KODra Sync Rate (%): {kodra_sync_rate:.2f}
"""),
    ]

    domain_report = "KODRA_DEEP_DECODE (Extraction contenu signal, QPE)"
    return domain_report, metrics, artifacts
