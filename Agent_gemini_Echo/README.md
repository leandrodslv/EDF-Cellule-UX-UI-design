# ECHO — Agent UXR · Setup & Usage (Gemini CLI)

Agent orchestrateur de recherche utilisateur. Pilote de A à Z le cycle de vie
d'un projet UXR qualitative et quantitative. Tourne dans **Gemini CLI**.

---

## Installation

> **Tu pars de zéro (pas de Node, pas de Python, pas de Git) ?**
> Suis le guide complet du [README racine](../README.md#installation-depuis-zéro),
> il couvre Windows et macOS étape par étape. La procédure ci-dessous suppose
> que les outils de base sont déjà en place.

1. Installe Gemini CLI :
   ```
   npm install -g @google/gemini-cli
   ```
2. Ouvre un terminal **dans ce dossier `Agent_gemini_Echo/`** — c'est important,
   Gemini CLI cherche `GEMINI.md` et `.gemini/` à partir du dossier de lancement
3. Lance `gemini`
4. Gemini lit automatiquement `GEMINI.md` au démarrage — ECHO est en place

> Cet agent est autonome : il ne lit et n'écrit **rien** en dehors de
> `Agent_gemini_Echo/`. Ses livrables vont dans `projets/[nom-projet]/`.
> Tu peux copier ce seul dossier ailleurs, il fonctionnera tel quel.

---

## Prérequis

- **Node.js 20+** (requis par Gemini CLI)
- **Notion MCP** déclaré dans `.gemini/settings.json` (déjà configuré)
  → au premier lancement, autorise-le avec `/mcp auth notion`
  → vérifie la connexion avec `/mcp list`
- **Python + openpyxl** pour la génération des `.xlsx` (Phase S1) :
  ```
  pip install openpyxl
  ```
- Le fichier `uxr-state.json` présent (déjà inclus)

### Alternative Notion en local (si le MCP distant ne convient pas)

Remplace le bloc `notion` de `.gemini/settings.json` par :

```json
"notion": {
  "command": "npx",
  "args": ["-y", "@notionhq/notion-mcp-server"],
  "env": { "NOTION_TOKEN": "$NOTION_TOKEN" }
}
```

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
Agent_gemini_Echo/                     ← lance `gemini` DEPUIS ce dossier
├── GEMINI.md                          ← cerveau de l'agent (lu automatiquement)
├── uxr-state.json                     ← mémoire persistante des projets
├── README.md                          ← ce fichier
├── .gemini/
│   ├── settings.json                  ← config MCP Notion + contexte
│   └── commands/
│       └── go.toml                    ← commande /go
├── scripts/
│   └── generate_analysis.py           ← génération des analyses .xlsx
├── projets/                           ← TES livrables (propres à cet agent)
│   └── eclipse/
│       ├── eclipse-questionnaire.xlsx
│       ├── eclipse-responses.xlsx
│       ├── eclipse-analyse.xlsx
│       └── generate_eclipse_*.py
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

## Commandes Gemini CLI utiles

| Commande | Effet |
|----------|-------|
| `/go` | Lance ou reprend la session ECHO |
| `/mcp list` | Vérifie que le serveur Notion est connecté |
| `/mcp auth notion` | Autorise le MCP Notion (OAuth) |
| `/memory show` | Affiche le contexte `GEMINI.md` chargé |
| `/memory refresh` | Recharge `GEMINI.md` après édition |
| `/chat save <nom>` | Sauvegarde la conversation en cours |
| `/chat resume <nom>` | Reprend une conversation sauvegardée |
| `/stats` | Consommation de tokens de la session |

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
