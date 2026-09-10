# -*- coding: utf-8 -*-
"""
KoDRA - Kiss Of the Dragon
A Pocket Meta-Quantum Computer (PMQC)
Universal UTF-8. Cross-platform.

U = Unicity — the emergent, final and unified state (the 'unicity in the One').
FR: U = Unicité — l'état émergent, final et unifié (l'« unicité dans le 1 »).
Regardless of the multiple existential states of different x ∈ M, when they pass
through the Portal 𝟎 (the state-transition operator), those x converge toward
one unified state U(x). U is not the scalar 1; it denotes that unique, emergent,
unifying state.
"""
import os
import sys
import io
import json
import webbrowser
import time
import glob
import random
import secrets


def _format_speedup(speedup):
    """Format speedup: notation scientifique si >= 1e6."""
    import math
    if math.isnan(speedup) or speedup == float('inf'):
        return "x?"
    if speedup < 1:
        return f"{speedup:.4f}x"
    if speedup < 1e6:
        return f"x{int(speedup):,}"
    exp = int(math.log10(speedup))
    coef = speedup / (10 ** exp)
    sup = str(exp).translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))
    return f"~{coef:.1f}×10{sup}"


def _run_sympy_factorint(n):
    """Worker for ProcessPoolExecutor: mesure réelle du temps factorint."""
    import time
    from sympy import factorint
    start = time.time()
    factorint(n)
    return time.time() - start


def _classical_status_message(status, kodra_faster):
    """Message franc sur le statut classique/QC."""
    if status == "timeout":
        return "Algorithmes classiques: échec (timeout)"
    if status == "infeasible":
        return "Classique / QC / Supercalculateurs: hors portée — extrapolation KoDRA"
    if status == "solved":
        return "Classical: résolu | KoDRA avantage" if kodra_faster else "Classical: résolu (plus rapide pour ce N)"
    return "N/A"

[...]
# Force UTF-8 for stdout/stderr (Windows/Linux/macOS compatibility)
def _ensure_utf8():
    if hasattr(sys.stdout, 'buffer') and getattr(sys.stdout, 'encoding', '') != 'utf-8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    if hasattr(sys.stderr, 'buffer') and getattr(sys.stderr, 'encoding', '') != 'utf-8':
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

_ensure_utf8()

[...]
# (The rest of KoDRA.py remains unchanged apart from the added header docstring.)

