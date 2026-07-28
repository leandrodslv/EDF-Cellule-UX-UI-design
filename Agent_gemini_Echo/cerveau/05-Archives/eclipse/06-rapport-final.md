---
type: livrable
phase: 4
projet: "[[Eclipse]]"
statut: valide
date: 2026-04-20
entretiens: 8
repondants-questionnaire: 200
tags:
  - uxr
  - rapport
---

# Rapport de recherche · Eclipse

**8 entretiens · 200 réponses au questionnaire · Mode mixed**

---

## 1 · Contexte et objectifs

45 % des utilisateurs freemium actifs quittent le tunnel d'abonnement sans
convertir après avoir consulté la page de tarification au moins deux fois.
Cette recherche vise à comprendre les mécanismes de décision à l'origine de cet
abandon, pour alimenter la priorisation de la roadmap Q3 et l'ajustement du
design de la page de tarification.

**Ce qu'on cherchait à comprendre**
- Les freins psychologiques et pratiques au moment de la décision de paiement
- Le niveau de clarté perçue de la grille tarifaire et de la nomenclature
- La valeur perçue des fonctionnalités Pro et ses déterminants

**Hors périmètre :** évaluer la satisfaction globale, valider un nouveau design,
comparer le produit à la concurrence.

---

## 2 · Méthodologie

Questionnaire quantitatif (S1/S2) puis entretiens semi-directifs (phases 1 à 3).
Durée par entretien : ~45 min. Terrain : 20 avril 2026.

**Questionnaire** — 200 répondants · Clarté 2,58/5 · Valeur 3,74/5 ·
64 % disponibles pour un entretien.

**Participants rencontrés**

| # | ID | Profil | Usage | Frein déclaré |
|---|---|---|---|---|
| 1 | [[E01 · #002]] | Power user, structure individuelle | 20h/sem | Grille tarifaire illisible |
| 2 | [[E02 · #011]] | Freelance en croissance | 9h/sem | Nomenclature floue Pro/Business |
| 3 | [[E03 · #015]] | Lead Data, PME | 22h/sem | Manque de clarté RGPD |
| 4 | [[E04 · #006]] | Manager équipe 15 pers. | 25h/sem | Validation interne |
| 5 | [[E05 · #013]] | Lead Tech, développeur | 16h/sem | Complexité paiement Stripe |
| 6 | [[E06 · #010]] | Exigeant sur le support | 18h/sem | Absence de support prioritaire |
| 7 | [[E07 · #004]] | Indépendant par missions | 15h/sem | Pas d'option mensuelle |
| 8 | [[E08 · #008]] | Orienté preuve sociale | 14h/sem | Manque de preuves sociales |

**Biais surveillés** — désirabilité autour du prix, contamination par les
résultats du questionnaire, rationalisation a posteriori, biais de confirmation.
Contre-mesures détaillées dans [[02-guide-entretien]].

---

## 3 · Insights clés

> Descriptifs, pas prescriptifs : ils décrivent ce qui existe, pas ce qu'il
> faudrait faire.

| # | Insight | Priorité | Fréquence |
|---|---|---|---|
| 1 | [[I01 · Intention de payer présente, conversion bloquée par frictions cumulées]] | P1 | 8/8 |
| 2 | [[I02 · La nomenclature des plans bloque la décision avant le checkout]] | P1 | 2/8 explicite, 53 % questionnaire |
| 3 | [[I03 · L'absence d'option mensuelle est un frein structurel]] | P1 | 2/8 |
| 4 | [[I04 · Un bug reproductible dans le tunnel de paiement bloque la conversion]] | P1 | 1/8, sous-déclaré |
| 5 | [[I05 · L'absence d'infrastructure commerciale B2B exclut les acheteurs en entreprise]] | P1 | 2/8 |

---

## 4 · Patterns transversaux

La totalité des participants exprime une valeur perçue positive et une intention
de payer documentée. **Aucun n'a cité le prix comme frein principal.** Le taux
d'abandon de 45 % n'est pas causé par un rejet du produit, mais par
l'accumulation de frictions distinctes, chacune suffisante à elle seule.

Un vocabulaire émotionnel négatif fort apparaît chez 5/8 participants —
« piéger », « paralysant », « gadget pas sérieux », « frustrant », « vide ».
Cette intensité signale que la page ne génère pas seulement de
l'incompréhension : elle génère une perte de confiance.

**Cause racine** — la page est conçue pour un acheteur individuel payant par
carte en self-service. Le profil réel des non-convertis rencontrés est
professionnel, avec des contraintes d'achat structurées.

**Résultat inattendu** — le frein le plus directement actionnable est un défaut
technique absent des hypothèses initiales, probablement invisible dans les
analytics produit actuels.

Analyse détaillée : [[04-synthese]]

---

## 5 · Recommandations

> Priorisées par impact utilisateur × faisabilité estimée.

| Priorité | Recommandation | Source | Métrique de succès |
|---|---|---|---|
| P1 | Corriger le bug Stripe × autocomplétion ; ajouter un feedback visuel de traitement | I04 | Taux d'erreur checkout → 0 |
| P1 | Renommer les plans à partir des cas d'usage ; remplacer les descriptions par un tableau fonctionnel Oui/Non | I02 | Taux de sélection du plan au 1er passage |
| P1 | Introduire un plan mensuel ; rendre le switch mensuel/annuel visible au checkout | I03 | Taux de conversion mensuel ; abandon checkout |
| P1 | Ajouter « Contacter l'équipe commerciale » ; intégrer le champ TVA au checkout | I05 | Leads B2B ; complétion checkout PME |
| P2 | Créer une section « Confiance & conformité » (hébergement, certifications, SLA) | I01 | Conversion segment entreprise |
| P2 | Ajouter logos clients, témoignages ROI et cas d'usage par profil | I01 | Scroll depth, temps sur page |

---

## 6 · Ce qu'on ne sait pas encore

**Questions ouvertes**
- Quelle est la part du bug Stripe dans les 45 % d'abandons ? Le défaut est-il
  récent ou systémique ?
- Quelle est la part réelle de l'absence d'option mensuelle à l'échelle de la
  base entière ?
- Existe-t-il des utilisateurs pour lesquels le prix est le frein principal ?
  Ils ne sont pas représentés ici — le critère de sélection S2 (Clarté ≤ 2) les
  a exclus de fait.

**Profils à investiguer si la recherche se poursuit**
- Utilisateur ayant converti puis annulé — conditions de la conversion initiale
  et raisons de résiliation
- Utilisateur freemium à faible usage n'ayant jamais consulté la page de
  tarification — la friction existe-t-elle en amont ?
- Acheteur en entreprise ayant finalement converti — quelles conditions ont
  permis le passage à l'acte ?

**Recommandation pour la suite**
Les recommandations P1 sont toutes actionnables sans nouvelle vague de
recherche. Une vague quantitative courte (5 questions post-correctifs)
permettra de mesurer l'impact sur le taux de complétion du checkout à 30 jours.

---

## Ce que cette étude laisse au second cerveau

| Connaissance | Confiance | Statut |
|---|---|---|
| [[N001 · La valeur est reconnue mais l'offre n'est pas lisible]] | moyenne | confirmée |
| [[N002 · La nomenclature des paliers ne permet pas de les distinguer]] | moyenne | confirmée |
| [[N003 · L'engagement annuel sans alternative mensuelle freine la conversion]] | moyenne | confirmée |
| [[N004 · L'absence d'infrastructure d'achat B2B exclut les acheteurs en entreprise]] | moyenne | créée |
| [[N005 · Les signaux de crédibilité professionnelle manquent sur la page de tarification]] | moyenne | créée |

Domaine : [[Tarification]]

---

## Annexes

- [[02-guide-entretien]] — cadrage, guide, biais surveillés
- [[04-synthese]] — affinity mapping, patterns, contradictions, personas
- `03-entretiens/` — les 8 notes brutes
- [Questionnaire](fichiers/eclipse-questionnaire.xlsx) ·
  [Réponses](fichiers/eclipse-responses.xlsx) ·
  [Analyse](fichiers/eclipse-analyse.xlsx)
