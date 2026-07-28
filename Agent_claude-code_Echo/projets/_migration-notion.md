---
type: note
statut: a-traiter
tags:
  - uxr
  - migration
---

# Migration Notion → vault Obsidian

ECHO n'utilise plus Notion. Tous les nouveaux projets sont écrits directement
ici, sur le disque.

**Ce qui reste à faire** ne concerne que le projet [[Eclipse]], produit avant
la bascule : son contenu rédactionnel est encore dans Notion et personne ne
peut le récupérer à ta place.

---

## Ce qui est déjà migré

- La note maîtresse du projet et ses propriétés
- Le plan de recherche
- Le questionnaire et ses trois fichiers Excel
- Les résultats chiffrés du volet quantitatif

## Ce qui manque

| Livrable | Où il se trouve encore |
|---|---|
| Guide d'entretien | Notion → Préparation entretien |
| 8 notes d'entretien (verbatims) | Notion → Notes brutes |
| Synthèse et insights | Notion → Synthèse & insights |
| Rapport final | Notion → Rapport final |

Pages Notion concernées :

- Carte projet — `https://www.notion.so/3483ac656c1c81529015d9c737e0d932`
- Préparation — `https://www.notion.so/3483ac656c1c811c8b67c0abf58d2738`
- Notes brutes — `https://www.notion.so/3483ac656c1c818582bacc13a3712418`
- Synthèse — `https://www.notion.so/3483ac656c1c81b6be52d67a74589609`
- Rapport — `https://www.notion.so/3483ac656c1c8131879ef708cfdabd20`

---

## Comment récupérer le contenu

1. Ouvre la page dans Notion
2. Menu `···` en haut à droite → **Exporter**
3. Format **Markdown & CSV**, sans les sous-pages si tu exportes page par page
4. Dézippe et place les fichiers ici :

| Contenu exporté | Destination dans le vault |
|---|---|
| Préparation entretien | `eclipse/02-guide-entretien.md` |
| Une note par entretien | `eclipse/03-entretiens/E01 · #002.md`, etc. |
| Synthèse | `eclipse/04-synthese.md` |
| Chaque insight | `eclipse/05-insights/I01 · [titre].md` |
| Rapport | `eclipse/06-rapport-final.md` |

5. Ajoute à chaque fichier son bloc de propriétés YAML — les formats exacts
   sont dans `references/obsidian-structure.md`

Une fois les fichiers déposés, dis-le à ECHO : il ajoutera les propriétés,
les liens `[[…]]` entre insights et entretiens, et mettra à jour
`uxr-state.json`. C'est la partie qu'il peut faire seul.

---

## Après la migration

Vérifie que le contenu est bien arrivé, puis **supprime les pages Notion**.
Tant qu'elles existent, les données de recherche vivent à deux endroits dont
un hors du périmètre EDF — c'est précisément ce que la bascule vers Obsidian
visait à éviter.
