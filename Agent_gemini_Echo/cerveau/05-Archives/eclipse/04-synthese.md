---
type: livrable
phase: 3
projet: "[[Eclipse]]"
statut: valide
date-analyse: 2026-04-20
entretiens-analyses: 8
tags:
  - uxr
  - synthese
---

# Synthèse & insights · Eclipse

**Entretiens analysés :** 8 — #002, #011, #015, #006, #013, #010, #004, #008
**Préparation :** [[02-guide-entretien]]

---

## Affinity mapping — 5 thèmes

### Thème 1 · Nomenclature des plans inadaptée au contexte d'usage
Les participants ne parviennent pas à sélectionner un plan car les noms
renvoient à des identités (« Pro », « Business ») plutôt qu'à des cas d'usage.
**Fréquence :** 2/8 explicite · **Intensité émotionnelle :** forte
Sources : [[E01 · #002]], [[E02 · #011]]

### Thème 2 · Absence de signaux de crédibilité professionnelle
Les participants exerçant dans un contexte structuré ne trouvent pas sur la page
les signaux validant que le produit est conçu pour eux.
**Fréquence :** 3/8 explicite, probable sur 5/8 · **Intensité :** forte
Sources : [[E03 · #015]], [[E08 · #008]], [[E06 · #010]]

### Thème 3 · Incompatibilité de l'engagement annuel avec les usages réels
Les participants à revenu variable ne peuvent pas s'engager sur 12 mois.
L'absence d'option mensuelle est perçue comme une contrainte imposée.
**Fréquence :** 2/8 explicite · **Intensité :** forte
Sources : [[E01 · #002]], [[E07 · #004]]

### Thème 4 · Infrastructure de vente inadaptée au contexte B2B
Contraintes de bon de commande, de facturation conforme, de validation
juridique — incompatibles avec un tunnel self-service par carte.
**Fréquence :** 2/8 explicite · **Intensité :** forte
Sources : [[E04 · #006]], [[E03 · #015]]

### Thème 5 · Défaut technique dans le tunnel de paiement
Le sélecteur de pays Stripe échoue avec l'autocomplétion du navigateur.
**Fréquence :** 1/8 explicite, potentiellement sous-déclaré · **Intensité :** forte
Source : [[E05 · #013]]

---

## Insights priorisés

| # | Insight | Priorité | Fréquence |
|---|---|---|---|
| 1 | [[I01 · Intention de payer présente, conversion bloquée par frictions cumulées]] | P1 | 8/8 |
| 2 | [[I02 · La nomenclature des plans bloque la décision avant le checkout]] | P1 | 2/8 explicite |
| 3 | [[I03 · L'absence d'option mensuelle est un frein structurel]] | P1 | 2/8 |
| 4 | [[I04 · Un bug reproductible dans le tunnel de paiement bloque la conversion]] | P1 | 1/8 |
| 5 | [[I05 · L'absence d'infrastructure commerciale B2B exclut les acheteurs en entreprise]] | P1 | 2/8 |

---

## Patterns transversaux

| Pattern | Présent chez | Confiance |
|---|---|---|
| Intention de payer présente, conversion bloquée par friction spécifique | 8/8 | élevée |
| Arrêt avant ou pendant le checkout pour raison non liée au prix | 8/8 | élevée |
| Vocabulaire émotionnel négatif fort sur la page de tarification | 5/8 | élevée |
| Page perçue comme inadaptée au contexte professionnel | 5/8 | élevée |
| Absence de signal de confiance identifiée comme bloquante | 4/8 | élevée |
| Option mensuelle recherchée activement | 2/8 explicite | moyenne |

Le vocabulaire relevé — « piéger », « paralysant », « gadget pas sérieux »,
« frustrant », « vide » — indique que la page ne produit pas seulement de
l'incompréhension, mais une perte de confiance.

**Cause racine identifiée** : la page est conçue pour un acheteur individuel
payant par carte en self-service. Le profil réel des non-convertis rencontrés
est professionnel, avec des contraintes d'achat structurées.

---

## Contradictions identifiées

**Contradiction 1** — #002 et #010 ont le même score Clarté (2/5) mais des
freins différents : nomenclature pour l'un, absence de SLA pour l'autre.
→ Hypothèse : le score Clarté agrège des problèmes de nature différente
(lisibilité vs garanties) que l'échelle de Likert ne distingue pas.
→ À investiguer : décomposer la clarté en sous-dimensions dans le prochain
questionnaire.

**Contradiction 2** — #011 (valeur 3/5) et #002 (valeur 5/5) ont des scores très
différents mais un frein nomenclature similaire.
→ Hypothèse : chez #002, l'usage intensif (20h/sem) clarifie la valeur ; chez
#011 (9h/sem), la nomenclature floue empêche aussi de percevoir la valeur
différentielle.
→ À investiguer : la clarté de la nomenclature est-elle un prérequis à la
perception de valeur chez les usages intermédiaires ?

---

## Esquisses persona

### Persona A — profil « professionnel individuel bloqué »
Usage intensif (15–25h/sem) en contexte professionnel structuré. S'est rendu
sur la page de tarification, parfois jusqu'au checkout. N'a pas converti parce
qu'un élément du parcours a déclenché une alerte qu'il n'a pas su résoudre seul.
Workarounds : comptes gratuits multiples, suppression de fichiers.
Citation : « Je veux vous donner mon argent, mais votre tunnel de vente est
moins stable que votre outil gratuit. »

### Persona B — profil « décideur en organisation »
Identifie le besoin pour son équipe, mais ne peut pas payer par carte
personnelle. A besoin d'un processus compatible avec les contraintes
administratives de son organisation.
Citation : « Votre page de vente ressemble à un outil gadget, pas à un logiciel
d'entreprise sérieux. »

> [!warning] Statut des personas
> Esquisses issues de 8 entretiens — à valider avant tout usage en conception.
> Questions ouvertes : seuil de friction au-delà duquel l'abandon devient
> définitif ; taille d'équipe à partir de laquelle l'infrastructure B2B devient
> bloquante.

---

## Distillation vers le second cerveau

| Insight | Connaissance | Effet |
|---|---|---|
| I01 | [[N001 · La valeur est reconnue mais l'offre n'est pas lisible]] | Confirmée et renforcée |
| I02 | [[N002 · La nomenclature des paliers ne permet pas de les distinguer]] | Confirmée et renforcée |
| I03 | [[N003 · L'engagement annuel sans alternative mensuelle freine la conversion]] | Confirmée et renforcée |
| I05 | [[N004 · L'absence d'infrastructure d'achat B2B exclut les acheteurs en entreprise]] | Créée |
| Thème 2 | [[N005 · Les signaux de crédibilité professionnelle manquent sur la page de tarification]] | Créée |
| I04 | — | Non distillé : défaut technique corrigible, pas une connaissance durable |
