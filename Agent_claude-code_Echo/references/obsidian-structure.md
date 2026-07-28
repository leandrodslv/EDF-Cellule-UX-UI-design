# Obsidian — Structure et formats du vault

Tous les livrables d'ECHO sont des **fichiers Markdown écrits sur le disque**.
Il n'y a ni serveur, ni API, ni compte, ni connecteur : écrire un livrable,
c'est écrire un fichier.

Le vault est le dossier `cerveau/`. C'est lui que le pilote ouvre dans Obsidian.

> Ce document décrit **où** et **comment** écrire.
> La méthode — pourquoi cette organisation, quand distiller, comment coter la
> confiance — est dans `second-cerveau.md`. Lis les deux.

---

## Arborescence du vault

```
cerveau/                              ← racine du vault Obsidian
├── Accueil.md                        ← point d'entrée, MOC racine
├── _templates/                       ← modèles de notes
│   ├── T-projet.md
│   ├── T-entretien.md
│   ├── T-insight.md
│   ├── T-connaissance.md
│   └── T-domaine.md
│
├── 00-Inbox/                         ← capture brute à trier
│
├── 01-Projets/                       ← études en cours
│   └── [nom-projet]/
│       ├── [Nom-Projet].md           ← note maîtresse
│       ├── 00-plan-recherche.md
│       ├── 01-questionnaire.md       ← modes survey_only / mixed
│       ├── 02-guide-entretien.md     ← modes interviews_only / mixed
│       ├── 03-entretiens/
│       │   ├── E01 · #002.md
│       │   └── …
│       ├── 04-synthese.md
│       ├── 05-insights/
│       │   └── I01 · [titre court].md
│       ├── 06-rapport-final.md
│       └── fichiers/                 ← pièces jointes (.xlsx, exports)
│
├── 02-Domaines/                      ← sujets permanents
│   └── Tarification.md               ← MOC du domaine
│
├── 03-Connaissances/                 ← nuggets transversaux
│   └── N001 · [observation].md
│
├── 04-Ressources/                    ← méthodes, biais, benchmarks
│
└── 05-Archives/                      ← études terminées
    └── [nom-projet]/                 ← même structure que 01-Projets
```

Le préfixe numérique force l'ordre d'affichage et reflète l'ordre du pipeline.
Ne le retire jamais. Le préfixe `_` fait remonter `_templates/` en haut.

**À la fin d'un projet**, déplace son dossier de `01-Projets/` vers
`05-Archives/`. Les connaissances qu'il a produites restent, elles, dans
`03-Connaissances/`.

---

## Les propriétés YAML

Chaque note commence par un bloc de propriétés. Obsidian les affiche comme des
champs éditables et sait filtrer dessus.

**Règle absolue** : le bloc `---` doit être la toute première ligne du fichier,
sans ligne vide avant, sinon Obsidian ne le reconnaît pas.

### Note maîtresse de projet

```markdown
---
type: projet
statut: terrain
domaine: "[[Tarification]]"
mode: mixed
date-debut: 2026-04-20
date-fin-estimee: 2026-05-10
entretiens-prevus: 8
entretiens-realises: 3
connaissances-produites: 0
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

### Note d'insight (liée à un projet)

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

### Note de connaissance (transversale — le nugget)

```markdown
---
type: connaissance
domaine: "[[Tarification]]"
confiance: moyenne
etudes: 1
sources:
  - "[[Eclipse]]"
premiere-observation: 2026-04-27
derniere-confirmation: 2026-04-27
statut: actif
tags:
  - uxr
  - connaissance
  - tarification
---
```

`confiance` : `faible` · `moyenne` · `forte` · `etablie` — barème dans
`second-cerveau.md`
`statut` : `actif` · `a-reverifier` · `invalide`

### MOC de domaine

```markdown
---
type: domaine
statut: actif
connaissances: 3
etudes: 1
derniere-activite: 2026-04-27
tags:
  - uxr
  - domaine
---
```

---

## Insight ou connaissance ? La distinction à ne pas rater

| | Insight | Connaissance (nugget) |
|---|---|---|
| Portée | Un projet | Transversale |
| Durée de vie | Meurt avec le projet | S'enrichit à chaque étude |
| Emplacement | `01-Projets/[projet]/05-insights/` | `03-Connaissances/` |
| Formulation | « Dans Eclipse, 6/8 ont buté sur… » | « Les utilisateurs ne distinguent pas… » |
| Champs | `occurrences`, `participants` | `etudes`, `sources`, `confiance` |

Tout insight doit être **distillé** en connaissance en fin de Phase 3 —
procédure dans `second-cerveau.md`.

---

## Les liens `[[wikilink]]`

C'est l'apport principal d'Obsidian pour de la recherche qualitative : une
connaissance pointe vers les entretiens exacts qui la fondent, et Obsidian
affiche la relation dans les deux sens.

**Depuis une connaissance, cite toujours tes sources :**

```markdown
Constaté chez [[E01 · #002]], [[E02 · #011]] et [[E05 · #013]].
```

**Depuis un projet archivé, pointe vers ce qui lui survit :**

```markdown
- [[N001 · La valeur est reconnue mais l'offre n'est pas lisible]]
```

Chaque note d'entretien affichera dans son panneau « Liens entrants » toutes
les connaissances qu'elle a nourries. Le pilote peut remonter d'une conclusion
à son verbatim d'origine en un clic — c'est la piste d'audit de la recherche.

**Ne crée jamais un lien vers une note inexistante** sans le signaler : Obsidian
l'affiche en grisé et ça ressemble à une erreur.

---

## Écrire une note d'entretien

**Le verbatim n'est jamais reformulé** : tu le recopies tel quel, hésitations
comprises. C'est la matière première de l'analyse ; la retoucher fausse le
résultat.

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

## Observations
[Comportements notés, hésitations, contradictions — descriptif, VOIX 2]

## Signaux à creuser
[Ce qui mérite d'être recoupé avec les autres entretiens]
```

---

## Le point d'entrée `Accueil.md`

À la racine du vault. Tu le mets à jour à chaque changement d'état : nouveau
projet, changement de statut, archivage, nouvelle connaissance.

Il porte trois tableaux : ce que la cellule sait (par domaine), les études en
cours, les études archivées.

Si le pilote a activé **Bases** (natif) ou **Dataview** (communauté), ces
tableaux peuvent être générés depuis les propriétés YAML. Ne le présuppose
pas : maintiens-les à la main, ils fonctionnent partout.

---

## Pièces jointes

Les `.xlsx` vont dans `[nom-projet]/fichiers/`. Pour les référencer :

```markdown
[Questionnaire Microsoft Forms](fichiers/eclipse-questionnaire.xlsx)
```

Obsidian ne sait pas ouvrir un `.xlsx` en interne — le lien l'ouvrira dans
Excel. C'est le comportement attendu.

---

## Conventions de nommage

| Élément | Format | Exemple |
|---|---|---|
| Dossier projet | minuscules, tirets | `eclipse` |
| Note maîtresse | Nom du projet, capitale | `Eclipse.md` |
| Entretien | `E[NN] · [participant]` | `E01 · #002.md` |
| Insight | `I[NN] · [titre court]` | `I01 · Grille tarifaire illisible.md` |
| Connaissance | `N[NNN] · [observation]` | `N001 · La valeur est reconnue….md` |
| Domaine | Nom simple, capitale | `Tarification.md` |
| Livrable de phase | préfixe numérique | `04-synthese.md` |

**Caractères interdits** : `\ / : * ? " < > |`
Le `·` (point médian) est autorisé et sert de séparateur lisible.

Les connaissances sont numérotées en continu sur tout le vault, tous domaines
confondus — `N001`, `N002`… Ne recommence pas à 1 par domaine.

---

## Ce que tu ne fais jamais dans le vault

- Modifier un verbatim déjà écrit — il est la source, il est intouchable
- Supprimer une note d'entretien, même si elle semble redondante
- **Supprimer une connaissance contredite** — elle passe en `a-reverifier`,
  la contradiction se documente
- Écrire un livrable sans son bloc de propriétés YAML
- Créer un dossier hors de la structure ci-dessus
- Écrire quoi que ce soit en dehors de `cerveau/`

---

## Si le pilote n'a pas encore Obsidian

Ça ne change rien à ton travail. Tu écris les mêmes fichiers, lisibles dans
n'importe quel éditeur de texte. Obsidian n'apporte que la navigation, les
liens et les vues — pas le contenu.

Signale-le une fois en VOIX 1, puis continue normalement.
