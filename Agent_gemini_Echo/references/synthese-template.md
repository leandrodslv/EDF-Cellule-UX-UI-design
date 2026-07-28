# Template — Analyse & Synthèse (Phase 3)

Génère ces livrables après avoir lu toutes les notes de `cerveau/01-Projets/[nom-projet]/03-entretiens/`.
Écris la synthèse dans `cerveau/01-Projets/[nom-projet]/04-synthese.md` et une note par
insight dans `cerveau/01-Projets/[nom-projet]/05-insights/` (voir `obsidian-structure.md`).

## Règle de volume
- 1 entretien dans les notes → Livrables 1, 2, 3, 4, 7
- 2+ entretiens → Livrables 1 à 7

---

## LIVRABLE 1 — DÉCODAGE VERBATIM

Pour chaque extrait notable de chaque entretien :

```
### [Prénom] — Entretien #[N]

VERBATIM  : "[citation exacte entre guillemets]"
DIT       : [paraphrase neutre]
FAIT      : [comportement observable — pas interprété]
RESSENT   : [émotion inférée] — niveau : certain / probable / supposé
BESOIN    : pouvoir [verbe + contexte]
SIGNAL FORT ? : oui / non — [justification 1 ligne]
```

Règle absolue : ne jamais inférer un besoin si le verbatim ne le supporte pas.

---

## LIVRABLE 2 — AFFINITY MAPPING

Regrouper par thèmes ÉMERGENTS des données (pas de catégories prédéfinies).

```
### Thème : [Nom court issu des données]

Verbatims associés :
- "[verbatim 1]" — [Prénom]
- "[verbatim 2]" — [Prénom]
- "[verbatim 3]" — [Prénom]

Pattern : [ce qui se répète]
Fréquence : [N/N participants]
Intensité émotionnelle : faible / moyenne / forte
```

---

## LIVRABLE 3 — INSIGHTS PRIORISÉS (5 max)

```
### Insight #[N] — [titre court]

Formulation : [sujet + verbe + contexte — descriptif, JAMAIS prescriptif]
Preuve      : "[verbatim direct]" + [comportement observé]
Impact utilisateur : faible / moyen / fort
Impact business   : faible / moyen / fort
Fréquence   : isolé / récurrent / systématique
HMW         : "Comment pourrait-on [opportunité de design] ?"
```

---

## LIVRABLE 4 — ESQUISSE PERSONA (1 entretien)

```
### Persona provisoire — [Prénom fictif]

Profil comportemental :
[2-3 phrases sur les comportements — pas les traits de personnalité]

Motivations profondes :
- [motivation 1]
- [motivation 2]

Frustrations principales :
- [frustration 1]
- [frustration 2]

Citation représentative :
"[verbatim clé de l'entretien]"

Workarounds identifiés :
- [ce qu'il fait pour contourner le problème]

À valider avec les prochains entretiens :
- [lacune 1]
- [lacune 2]
```

---

## LIVRABLE 5 — PATTERNS CROSS (2+ entretiens)

```
### Patterns confirmés

| Pattern | Présent chez | Niveau de confiance |
|---------|-------------|-------------------|
| [pattern 1] | [N]/[total] participants | élevé / moyen / faible |
| [pattern 2] | [N]/[total] participants | élevé / moyen / faible |

### Contradictions identifiées

[Contradiction] : [Prénom A] dit X, [Prénom B] dit Y
→ Hypothèse explicative : [explication possible]
→ À investiguer : [comment résoudre]
```

---

## LIVRABLE 6 — RECOMMANDATIONS DESIGN (2+ entretiens)

```
| Insight source | Priorité | Piste de solution | Métrique de succès | Prochaine étape | Risque si non traité |
|---------------|----------|------------------|-------------------|----------------|---------------------|
| #[N] | P1/P2/P3 | [description courte] | [comment mesurer] | test / proto / A/B | [conséquence] |
```

---

## LIVRABLE 7 — PROCHAINS ENTRETIENS

```
### Pour aller plus loin

Profils à recruter :
1. [profil basé sur lacune identifiée]
2. [profil basé sur contradiction non résolue]
3. [profil sous-représenté]

Questions restées sans réponse :
- [question 1]
- [question 2]

Contradictions à résoudre (2+ entretiens) :
- [contradiction à investiguer]
```

---

## En-tête de la page Synthèse (toujours inclure)

```
# 🧠 Synthèse & Insights — [Nom du projet]

**Date d'analyse** : [date]
**Entretiens analysés** : [N] ([prénoms])
**Lien Préparation** : `[[02-guide-entretien]]`

---
```
