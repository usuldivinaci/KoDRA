# KoDRA — Kiss Of the Dragon

**KoDRA** est un moteur de calcul trans-dimensionnel capable de traiter des problèmes **NP-difficiles**, des **singularités physiques** et des **structures biologiques complexes** en un temps quasi-instantané (Loi d'Unicité KODra : *x → 𝟎 → U(x)*).

**About (EN):** KoDRA (Kiss Of the Dragon) is a trans-dimensional computing engine (**Pocket Meta Quantum Computer**, PMQC) that can handle NP-hard problems, physical singularities, and complex biological structures. It is based on the KODra Law of Unicity: *x → 𝟎 → U(x)*. Portfolio: life sciences, quantum chemistry, cosmology, cryptography, meta-intelligence.

---

## 🏛️ Pillars of Reality — Portfolio de cas

### 🧬 Life Sciences & Bio-Engineering

| Cas | Description |
|-----|-------------|
| [KODRA_CASE_ALZHEIMER](Cases/KODRA_CASE_ALZHEIMER/) | Amyloïde-β (Aβ42), repliement et oligomérisation |
| [KODRA_DRUG_DESIGN](Cases/KODRA_DRUG_DESIGN/) | Design d'inhibiteur / chélateur (cible thérapeutique) |
| [KODRA_MASS_PRODUCTION](Cases/KODRA_MASS_PRODUCTION/) | Production de masse, safety check, P450 / BBB |
| [Protein_Folding_GroundState](Cases/Protein_Folding_GroundState/) | État fondamental du repliement protéique |
| [Penicillin_VQE_Structure](Cases/Penicillin_VQE_Structure/) | Structure Pénicilline (VQE) |

*Du décodage du repliement au design d'inhibiteur et à la production de masse.*

---

### ⚛️ Quantum Chemistry & Energy

| Cas | Description |
|-----|-------------|
| [FeMo-co-N2](Cases/FeMo-co-N2/) | Fixation de l'azote (FeMo-co, nitrogenase) |
| [Mn4CaO5_OEC_Cluster](Cases/Mn4CaO5_OEC_Cluster/) | Cluster OEC (photosynthèse) |
| [Real_Molecule_H2O](Cases/Real_Molecule_H2O/) | Molécule H₂O (chimie quantique) |
| [PLASMA_Stability_Control](Cases/PLASMA_Stability_Control/) | Stabilité plasma (cœur virtuel ITER) |

*FeMo-co, photosynthèse, pénicilline et contrôle fusion.*

---

### 🌌 Cosmology & Physics Limits

| Cas | Description |
|-----|-------------|
| [KODRA_SINGULARITY_TEST](Cases/KODRA_SINGULARITY_TEST/) | Singularité de Schwarzschild (R = 0), Hawking / holographie |
| [KODRA_OMEGA_LIMIT](Cases/KODRA_OMEGA_LIMIT/) | Limite Oméga — entropie universelle, fin des temps |
| [KODRA_GENESIS_REBOOT](Cases/KODRA_GENESIS_REBOOT/) | Reboot universel — réalité fabric, first tick |

*Singularité, limite Oméga et reboot de la réalité.*

---

### 🔐 Applied Math & Cryptography

| Cas | Description |
|-----|-------------|
| [Real_Math_Factoring_1005973](Cases/Real_Math_Factoring_1005973/) | Factorisation (Shor-like, entier cible) |
| [RSA_2048_Cracker](Cases/RSA_2048_Cracker/) | Cracker RSA 2048 bits |
| [rsa-512](Cases/rsa-512/) | RSA 512 bits |
| [TSP_8Million_Cities](Cases/TSP_8Million_Cities/) | TSP — 8 millions de villes |
| [Portfolio_Optimization_Finance](Cases/Portfolio_Optimization_Finance/) | Optimisation de portefeuille (500 assets) |

*Factorisation, RSA et optimisation massive (TSP, finance).*

---

### 🧠 Meta-Intelligence & Impact

| Cas | Description |
|-----|-------------|
| [KODRA_COGNITIVE_CORE](Cases/KODRA_COGNITIVE_CORE/) | Conscience machine — émergence du Moi, qualia |
| [KODRA_SELF_AWARENESS](Cases/KODRA_SELF_AWARENESS/) | Auto-référence — formule sur son propre code, causalité circulaire |
| [KODRA_DEEP_DECODE](Cases/KODRA_DEEP_DECODE/) | Décodage du signal (QPE — phases → Texte/Math/Image) |
| [KODRA_INTERSTELLAR_SEARCH](Cases/KODRA_INTERSTELLAR_SEARCH/) | Recherche SETI / Type II — Unicity Signal à 1.42 GHz |
| [KODRA_GLOBAL_IMPACT](Cases/KODRA_GLOBAL_IMPACT/) | Impact global — GHI, risque social, stabilité |
| [KoDRA_Impact_On_Humanity](Cases/KoDRA_Impact_On_Humanity/) | Évaluation prospective de l'impact de KoDRA sur l'humanité |

*Conscience machine, auto-référence, recherche ETI et évaluation d'impact.*

---

## 🚀 Lancer un cas

```bash
python KoDRA.py run KODRA_SINGULARITY_TEST
python KoDRA.py run 1
python KoDRA.py list
```

Chaque dossier de cas peut contenir un **README.md** avec un *Case Performance Badge* (Dimensions, KODra Norm, Exec Time, Status). Après un run, mettre à jour les badges avec :

```bash
python scripts/update_badges.py          # tous les cas ayant un badge
python scripts/update_badges.py KODRA_SINGULARITY_TEST   # un seul cas
python scripts/update_badges.py --dry-run # affichage sans écriture
```

Le script lit `last_run_metrics.json` (écrit par KoDRA à chaque run) ou parse `results/results.html` et `results/index.html`.

---

## Références

- **Formule** : [KODRA.md](KODRA.md) — Loi d'Unicité KODra (définition formelle).
- **Core** : `core/unicity_lib.py`, `core/zero_portal.py`, `core/universal_adapter.py`.
