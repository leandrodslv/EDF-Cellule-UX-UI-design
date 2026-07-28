---
type: index
tags:
  - uxr
---

# Projets de recherche · Cellule UX/UI EDF

Vault ECHO — moteur **Gemini CLI**.
Toutes les données de recherche vivent ici, sur ce disque. Rien n'est publié
en ligne.

## Projets

| Projet | Statut | Mode | Entretiens | Prochaine étape |
|---|---|---|---|---|
| [[Eclipse]] | termine | mixed | 8/8 | Présentation Steering Committee |

---

## Comment lire ce vault

Chaque projet a son dossier, et dans ce dossier les livrables sont numérotés
dans l'ordre du pipeline :

```
00-plan-recherche      → le cadrage validé
01-questionnaire       → le questionnaire diffusé (modes survey / mixed)
02-guide-entretien     → le guide utilisé sur le terrain
03-entretiens/         → les verbatims bruts, une note par entretien
04-synthese            → l'analyse transverse
05-insights/           → un insight = une note, reliée à ses verbatims
06-rapport-final       → le livrable présenté à l'équipe
fichiers/              → questionnaires et analyses Excel
```

**Le chemin utile** : depuis un insight, les liens `[[…]]` mènent aux
entretiens qui le fondent. Depuis un entretien, le panneau « Liens entrants »
d'Obsidian montre tous les insights qu'il a nourris. C'est la piste d'audit
de la recherche — on peut toujours remonter d'une conclusion à sa source.

---

## Conventions

- Les participants sont désignés par un identifiant (`#001`, `#002`) —
  jamais par leur nom
- Les verbatims ne sont **jamais** reformulés
- Les propriétés en haut de chaque note (`statut`, `confiance`, `occurrences`)
  sont filtrables et servent aux vues

## Modèles

`_templates/` contient les modèles de notes. Pour les utiliser dans Obsidian :
Paramètres → Modèles → dossier des modèles → `_templates`.
