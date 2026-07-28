# ECHO — Agent UXR · Setup & Usage (Claude Code)

Agent orchestrateur de recherche utilisateur. Pilote de A à Z le cycle de vie
d'un projet UXR qualitative et quantitative. Tourne dans **Claude Code**.

---

## Installation

1. Installe Claude Code :
   ```
   npm install -g @anthropic-ai/claude-code
   ```
2. Ouvre un terminal **dans ce dossier `claude-code/`** — c'est important,
   Claude Code cherche `CLAUDE.md` et `.claude/` à partir du dossier de lancement
3. Lance `claude`
4. Claude lit automatiquement `CLAUDE.md` au démarrage — ECHO est en place

> Les livrables projet (`.xlsx`) sont écrits dans `../projets/[nom-projet]/`,
> un dossier partagé avec l'agent Gemini.

---

## Prérequis

- **Node.js 18+**
- **Notion MCP** connecté (`https://mcp.notion.com/mcp`)
  → ajoute-le avec :
  ```
  claude mcp add --transport http notion https://mcp.notion.com/mcp
  ```
  → vérifie la connexion avec `/mcp`
- **Python + openpyxl** pour la génération des `.xlsx` (Phase S1) :
  ```
  pip install openpyxl
  ```
- Le fichier `uxr-state.json` présent (déjà inclus)

---

## Démarrer un nouveau projet

```
/go
```

ou

```
Lance une recherche sur [sujet]
```

ou

```
Nouveau projet UXR : [description en 1-2 phrases]
```

ECHO te posera les 5 questions de cadrage en une fois, créera tout dans Notion,
et te donnera le Human Task #1 (valider le plan).

---

## Reprendre un projet en cours

```
/go
```

ou

```
On reprend
```

ou

```
Où on en est sur [nom du projet] ?
```

ECHO lit `uxr-state.json`, affiche le dashboard, et reprend là où il s'est arrêté.

---

## Ajouter des notes d'entretien

```
J'ai fait l'entretien avec Sarah, voici les notes :
[notes brutes]
```

ECHO stocke dans Notion, met à jour le compteur, et te dit quoi faire ensuite.

---

## Fichiers

```
claude-code/                           ← lance `claude` DEPUIS ce dossier
├── CLAUDE.md                          ← cerveau de l'agent (lu automatiquement)
├── uxr-state.json                     ← mémoire persistante des projets
├── README.md                          ← ce fichier
├── .claude/
│   └── commands/
│       └── go.md                      ← commande /go
├── scripts/
│   └── generate_analysis.py           ← génération des analyses .xlsx
└── references/
    ├── state-schema.md                ← schéma JSON de l'état
    ├── guide-template.md              ← template Phase 1 (préparation)
    ├── questionnaire-template.md      ← template Phase S1 (questionnaire)
    ├── analyse-s2.md                  ← template Phase S2 (analyse réponses)
    ├── synthese-template.md           ← template Phase 3 (analyse)
    ├── rapport-template.md            ← template Phase 4 (rapport final)
    └── notion-structure.md            ← comment écrire dans Notion via MCP
```

---

## Commandes Claude Code utiles

| Commande | Effet |
|----------|-------|
| `/go` | Lance ou reprend la session ECHO |
| `/mcp` | Vérifie / autorise le serveur Notion |
| `/memory` | Édite le `CLAUDE.md` chargé |
| `/context` | Visualise l'occupation du contexte |
| `/resume` | Reprend une conversation précédente |
| `/cost` | Consommation de la session |

---

## Philosophie

L'agent prend les décisions. Toi, tu réponds à ses questions et tu fais les
actions physiques qu'il ne peut pas faire (mener l'entretien, recruter les
participants). Le reste : il s'en charge.

Human Tasks typiques par projet :
1. ✅ Valider le plan de recherche
2. ✅ Recruter les participants (message rédigé par l'agent)
3. 🔁 Mener les entretiens + transmettre les notes (répété N fois)
4. ✅ Valider les insights si ambiguïté
5. ✅ Présenter le rapport à l'équipe
