# Obsidian — Guide d'écriture du vault

Tous les livrables d'ECHO sont des **fichiers Markdown écrits sur le disque**.
Il n'y a ni serveur, ni API, ni compte, ni connecteur : écrire un livrable,
c'est écrire un fichier.

Le vault est le dossier `projets/`. C'est lui que le pilote ouvre dans Obsidian.

> **Conséquence pour toi** : tu n'as besoin d'aucun outil MCP. `write_file`
> et `read_file` suffisent à tout faire. Si le pilote n'a même pas installé
> Obsidian, les livrables restent lisibles — ce sont des `.md` ordinaires.

---

## Arborescence du vault

```
projets/                              ← racine du vault Obsidian
├── Index.md                          ← tableau de bord de tous les projets
├── _templates/                       ← modèles de notes
│   ├── T-projet.md
│   ├── T-entretien.md
│   └── T-insight.md
└── [nom-projet]/
    ├── [Nom-Projet].md               ← note maîtresse du projet
    ├── 00-plan-recherche.md
    ├── 01-questionnaire.md           ← si mode survey_only ou mixed
    ├── 02-guide-entretien.md         ← si mode interviews_only ou mixed
    ├── 03-entretiens/
    │   ├── E01 · #002.md
    │   ├── E02 · #011.md
    │   └── …
    ├── 04-synthese.md
    ├── 05-insights/
    │   ├── I01 · [titre court].md
    │   └── …
    ├── 06-rapport-final.md
    └── fichiers/                     ← pièces jointes (.xlsx, exports)
```

Le préfixe numérique force l'ordre d'affichage dans Obsidian et reflète
l'ordre du pipeline. Ne le retire jamais.

Le préfixe `_` de `_templates/` le fait remonter en haut de l'explorateur.

---

## Les propriétés YAML remplacent les propriétés Notion

Chaque note commence par un bloc de propriétés. Obsidian les affiche comme des
champs éditables et sait filtrer dessus. C'est l'équivalent direct des colonnes
d'une base Notion.

**Règle absolue** : le bloc `---` doit être la toute première ligne du fichier,
sans ligne vide avant, sinon Obsidian ne le reconnaît pas.

### Note maîtresse de projet

```markdown
---
type: projet
statut: terrain
mode: mixed
date-debut: 2026-04-20
date-fin-estimee: 2026-05-10
entretiens-prevus: 8
entretiens-realises: 3
tags:
  - uxr
  - projet
---
```

`statut` : `cadrage` · `preparation` · `terrain` · `analyse` · `termine`
`mode` : `interviews_only` · `survey_only` · `mixed`

### Note d'entretien

```markdown
---
type: entretien
projet: "[[Eclipse]]"
numero: 1
participant: "#002"
date: 2026-04-20
duree-min: 45
statut: done
tags:
  - uxr
  - entretien
---
```

### Note d'insight

```markdown
---
type: insight
projet: "[[Eclipse]]"
confiance: forte
occurrences: 6
participants:
  - "#002"
  - "#011"
tags:
  - uxr
  - insight
---
```

`confiance` : `forte` (5+ participants) · `moyenne` (3-4) · `faible` (1-2)

---

## Les liens `[[wikilink]]` — ce qui rend le vault utile

C'est l'apport principal d'Obsidian par rapport à Notion pour de la recherche
qualitative : un insight peut pointer vers les entretiens exacts qui le
fondent, et Obsidian affiche la relation dans les deux sens.

**Depuis un insight, cite toujours ses sources :**

```markdown
Constaté chez [[E01 · #002]], [[E02 · #011]] et [[E05 · #013]].
```

**Depuis le rapport, pointe vers les insights :**

```markdown
Voir [[I01 · Grille tarifaire illisible]].
```

Chaque note d'entretien affichera alors automatiquement, dans son panneau
« Liens entrants », tous les insights qu'elle a nourris. Le pilote peut
remonter d'une conclusion à son verbatim d'origine en un clic — c'est
exactement ce qu'on demande à une piste d'audit de recherche.

**Ne crée jamais un lien vers une note qui n'existe pas encore** sans le
signaler au pilote : Obsidian l'affichera en grisé et ça ressemble à une erreur.

---

## Écrire une note d'entretien

Le corps suit toujours cette structure. **Le verbatim n'est jamais reformulé** :
tu le recopies tel quel, fautes et hésitations comprises. C'est la matière
première de l'analyse, la retoucher revient à fausser le résultat.

```markdown
---
type: entretien
projet: "[[Eclipse]]"
numero: 1
participant: "#002"
date: 2026-04-20
statut: done
tags:
  - uxr
  - entretien
---

# Entretien 01 · #002

## Contexte
[Profil du participant, conditions de l'entretien — VOIX 2]

## Verbatims
> [citation exacte, non retouchée]

> [citation exacte, non retouchée]

## Observations
[Comportements notés, hésitations, contradictions — descriptif, VOIX 2]

## Signaux à creuser
[Ce qui mérite d'être recoupé avec les autres entretiens]
```

---

## Le tableau de bord `Index.md`

À la racine du vault. Tu le mets à jour à chaque changement de statut.

```markdown
# Projets de recherche

| Projet | Statut | Mode | Entretiens | Prochaine étape |
|---|---|---|---|---|
| [[Eclipse]] | termine | mixed | 8/8 | Présentation Steering Committee |
```

Si le pilote a activé le plugin **Bases** (natif) ou **Dataview** (communauté),
ce tableau peut être généré automatiquement depuis les propriétés YAML.
Ne présuppose pas que c'est le cas : maintiens le tableau à la main, il
fonctionne partout, y compris hors d'Obsidian.

---

## Pièces jointes

Les `.xlsx` (questionnaires, analyses) vont dans `[nom-projet]/fichiers/`.
Pour les référencer depuis une note :

```markdown
[Questionnaire Microsoft Forms](fichiers/eclipse-questionnaire.xlsx)
```

Obsidian ne sait pas ouvrir un `.xlsx` en interne — le lien l'ouvrira dans
Excel. C'est le comportement attendu, ne cherche pas à le contourner.

---

## Conventions de nommage

| Élément | Format | Exemple |
|---|---|---|
| Dossier projet | minuscules, tirets | `eclipse` |
| Note maîtresse | Nom du projet, capitale | `Eclipse.md` |
| Entretien | `E[NN] · [participant]` | `E01 · #002.md` |
| Insight | `I[NN] · [titre court]` | `I01 · Grille tarifaire illisible.md` |
| Livrable de phase | préfixe numérique | `04-synthese.md` |

**Caractères interdits dans un nom de fichier** : `\ / : * ? " < > |`
Le `·` (point médian) est autorisé et sert de séparateur lisible.

---

## Ce que tu ne fais jamais dans le vault

- Modifier un verbatim déjà écrit — il est la source, il est intouchable
- Supprimer une note d'entretien, même si elle semble redondante
- Écrire un livrable sans son bloc de propriétés YAML
- Créer un dossier hors de la structure ci-dessus
- Écrire quoi que ce soit en dehors de `projets/`

---

## Si le pilote n'a pas encore Obsidian

Ça ne change rien à ton travail. Tu écris les mêmes fichiers, ils sont
lisibles dans n'importe quel éditeur de texte. Obsidian n'apporte que la
navigation, les liens et les vues — pas le contenu.

Signale-le une fois en VOIX 1, puis continue normalement.
