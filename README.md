# EDF · Cellule UX/UI Design

Ce dépôt héberge **ECHO**, agent UXR autonome qui pilote un projet de recherche
utilisateur de A à Z — cadrage, questionnaire, entretiens, analyse, rapport.

ECHO existe en **deux implémentations indépendantes**, une par moteur.
Même méthode, même personnalité, même pipeline — seule la plomberie change.

---

## Choisir son agent

| | **Claude Code** | **Gemini CLI** |
|---|---|---|
| Dossier | [`claude-code/`](claude-code/) | [`gemini/`](gemini/) |
| Cerveau | `CLAUDE.md` | `GEMINI.md` |
| Commande | `.claude/commands/go.md` | `.gemini/commands/go.toml` |
| Config MCP | `claude mcp add …` | `.gemini/settings.json` |
| Lancement | `cd claude-code && claude` | `cd gemini && gemini` |

Les deux sont **autonomes** : chacun embarque ses propres `references/`,
`scripts/` et `uxr-state.json`. Tu peux en partager un seul à un collègue,
il fonctionnera sans le reste du dépôt.

> **Important** — lance toujours le CLI *depuis le dossier de l'agent*, jamais
> depuis la racine. Les deux outils cherchent leur fichier de contexte à partir
> du dossier courant : lancés d'ici, ils ne trouveraient rien.

---

## Arborescence

```
EDF-Cellule-UX-UI-design/
├── README.md                  ← ce fichier
│
├── claude-code/               ← agent ECHO · moteur Claude Code
│   ├── CLAUDE.md
│   ├── .claude/commands/go.md
│   ├── references/
│   ├── scripts/
│   ├── uxr-state.json
│   └── README.md              ← setup détaillé
│
├── gemini/                    ← agent ECHO · moteur Gemini CLI
│   ├── GEMINI.md
│   ├── .gemini/
│   │   ├── settings.json
│   │   └── commands/go.toml
│   ├── references/
│   ├── scripts/
│   ├── uxr-state.json
│   └── README.md              ← setup détaillé
│
└── projets/                   ← livrables, partagés entre les deux agents
    └── eclipse/
        ├── eclipse-questionnaire.xlsx
        ├── eclipse-responses.xlsx
        ├── eclipse-analyse.xlsx
        └── generate_eclipse_*.py
```

---

## Pourquoi `projets/` est partagé

Les livrables appartiennent au projet de recherche, pas au moteur qui les a
produits. Un questionnaire généré côté Gemini doit rester exploitable côté
Claude Code — et inversement. C'est le seul point de contact entre les deux
agents, et il est volontaire.

Côté Gemini, ce dossier est déclaré dans `.gemini/settings.json`
(`context.includeDirectories`) car Gemini CLI restreint par défaut ses accès
fichiers au dossier de lancement.

---

## Maintenir les deux en parallèle

`references/` est dupliqué dans chaque agent — c'est le prix de l'autonomie.
**Si tu modifies un template, reporte-le dans les deux dossiers.**

Vérifier qu'ils n'ont pas divergé :

```bash
diff -r claude-code/references gemini/references
diff -r claude-code/scripts    gemini/scripts
```

`scripts/` doit être strictement identique — aucune sortie attendue.

`references/` doit être identique **sauf `notion-structure.md`** : les commandes
de vérification du MCP diffèrent entre les deux CLI (`/mcp` côté Claude Code,
`/mcp list` + `/mcp auth notion` côté Gemini). C'est la seule divergence
légitime — toute autre différence est une dérive à corriger.

---

## Projet de référence — Eclipse

Projet UXR complet et terminé, mode `mixed` (questionnaire + entretiens) :
200 réponses au questionnaire, 8 entretiens, analyse et rapport livrés.
Sert d'exemple de bout en bout dans `projets/eclipse/`.

Les données participants sont **anonymisées** (identifiants `#001` à `#200`,
aucun nom, aucune donnée personnelle).

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
