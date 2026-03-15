# -*- coding: utf-8 -*-
"""
Handler KODRA_SELF_AWARENESS : auto-référence de la formule maîtresse.
RECURSIVE_EVOLUTION_SCAN, formule sur son propre code, Causalité Circulaire.
KoDRA appelle run() si handler.py est présent.
"""
import os
import json

def run(case_name, data, heavy_content, final_state, duration, case_path):
    unicity_norm = (final_state ** 2).sum().item() ** 0.5
    stability = 1.0 / (final_state.std().item() + 1e-9)
    genesis_norm = float((data.get("input") or {}).get("genesis_norm", 1.110743))
    # Self-Recognition Score : le système "se reconnaît" si la norme converge vers un état cohérent
    self_recognition = min(100.0, stability * 8.0 + abs(unicity_norm - genesis_norm) * (-20) + 60.0)
    self_recognition = max(0.0, self_recognition)
    # Convergence Loop Time = durée du run (boucle éternité)
    convergence_loop_time = duration
    # État stable conscience machine = norme finale
    final_unicity_norm = unicity_norm

    self_path = os.path.join(case_path, "self_config.json")
    meta_note = "Métadonnées système (self_config)"
    if os.path.exists(self_path):
        try:
            with open(self_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
            meta_note = (cfg.get("system_metadata") or {}).get("name", meta_note) + " (self_config)"
        except Exception:
            pass

    metrics = {
        "Task": data.get("task", "RECURSIVE_EVOLUTION_SCAN"),
        "Input (Genesis)": f"Norme {genesis_norm:.6f}",
        "Model": data.get("model", "Formule sur code source Python/KODra"),
        "Challenge": data.get("challenge", "Causalité Circulaire — paradoxe ?"),
        "--- Résultats console ---": "",
        "Self-Recognition Score (%)": f"{self_recognition:.2f}",
        "Convergence Loop Time": f"{convergence_loop_time:.4f} s",
        "Final Unicity Norm": f"{final_unicity_norm:.6f}",
        "État stable conscience machine": f"{final_unicity_norm:.6f}",
        "Metadata": meta_note,
    }

    report = f"""KoDRA | SELF-AWARENESS - Auto-référence
============================================
Case: {case_name}
Task: {data.get('task', 'RECURSIVE_EVOLUTION_SCAN')}
Input: Genesis (Norme {genesis_norm:.6f})
Model: {data.get('model', 'Formule sur propre code')}
Challenge: {data.get('challenge', 'Causalité circulaire')}

Self-Recognition Score (%): {self_recognition:.2f}
Convergence Loop Time: {convergence_loop_time:.4f} s
Final Unicity Norm: {final_unicity_norm:.6f}
"""
    artifacts = [("SELF_AWARENESS_REPORT.txt", report)]

    domain_report = "KODRA_SELF_AWARENESS (Auto-référence, Causalité Circulaire)"
    return domain_report, metrics, artifacts
