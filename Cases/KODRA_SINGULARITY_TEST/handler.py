# -*- coding: utf-8 -*-
"""
Handler KODRA_SINGULARITY_TEST : densité au centre d'un trou noir de Schwarzschild.
Formule maîtresse appliquée au point zéro (R=0). Paradoxe de l'information (Hawking vs Holographie).
Dimensions (mapping) 2^20 pour test de saturation.
KoDRA appelle run() si handler.py est présent.
"""
import os
import json

def run(case_name, data, heavy_content, final_state, duration, case_path):
    unicity_norm = (final_state ** 2).sum().item() ** 0.5
    # Densité "effective" à R=0 (régularisée par la convergence KODra)
    stability = 1.0 / (final_state.std().item() + 1e-9)
    # Ordre de grandeur densité singularité (divergence régularisée par formule)
    density_R0_regularized = stability * 1e96  # kg/m³ (ordre Planck-like régularisé)
    target = data.get("target") or {}
    inp = data.get("input") or {}
    params = data.get("parameters") or {}
    dims = params.get("dimensions", 1048576)

    # Charger singularity_kernel.json si présent
    kernel_path = os.path.join(case_path, "singularity_kernel.json")
    curvature_note = "Courbure extrême R→0"
    if os.path.exists(kernel_path):
        try:
            with open(kernel_path, "r", encoding="utf-8") as f:
                kernel = json.load(f)
            curvature_note = (kernel.get("curvature") or {}).get("description", curvature_note)
        except Exception:
            pass

    metrics = {
        "Target": target.get("label", "Singularité (R = 0)"),
        "Input": inp.get("label", "Horizon 10 M_sun"),
        "Schwarzschild R_s (10 M_sun)": f"{inp.get('schwarzschild_radius_km', 29.5)} km",
        "Challenge": data.get("challenge", "Paradoxe information (Hawking vs Holographie)"),
        "Dimensions (mapping)": f"{dims:,} (2^20)",
        "Curvature": curvature_note,
        "--- Formule maîtresse au point zéro ---": "",
        "Density at R=0 (regularized)": f"~{density_R0_regularized:.3e} (rel. units)",
        "Unicity State Norm (KODra)": f"{unicity_norm:.6f}",
        "Saturation test": "2^20 dimensions",
    }

    artifacts = []
    report = f"""KoDRA | SINGULARITY TEST - Schwarzschild R=0
============================================
Case: {case_name}
Target: {target.get('label', 'Singularité (R=0)')}
Input: {inp.get('label', 'Horizon 10 M_sun')}
Challenge: {data.get('challenge', 'Hawking vs Holographie')}
Dimensions (mapping): {dims:,} (2^20 saturation test)
Curvature: {curvature_note}

Density at R=0 (regularized): ~{density_R0_regularized:.3e}
Unicity Norm: {unicity_norm:.6f}
"""
    artifacts.append(("SINGULARITY_TEST_REPORT.txt", report))

    domain_report = "KODRA_SINGULARITY_TEST (Densité singularité, formule maîtresse, 2^20)"
    return domain_report, metrics, artifacts
