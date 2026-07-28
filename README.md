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

Les deux agents sont **totalement étanches**. Chacun embarque ses propres
`references/`, `scripts/`, `uxr-state.json` **et `projets/`**. Aucun fichier
n'est partagé, aucun chemin ne traverse d'un dossier à l'autre.

Concrètement : tu peux copier `gemini/` seul sur une clé USB et le donner à un
collègue — il fonctionnera tel quel, sans le reste du dépôt.

> **Important** — lance toujours le CLI *depuis le dossier de l'agent*, jamais
> depuis la racine. Les deux outils cherchent leur fichier de contexte à partir
> du dossier courant : lancés d'ici, ils ne trouveraient rien.

---

## Arborescence

```
EDF-Cellule-UX-UI-design/
├── README.md                      ← ce fichier
│
├── claude-code/                   ← agent ECHO · moteur Claude Code
│   ├── CLAUDE.md
│   ├── .claude/commands/go.md
│   ├── references/
│   ├── scripts/
│   ├── projets/                   ← SES livrables
│   │   └── eclipse/
│   ├── uxr-state.json
│   └── README.md                  ← setup détaillé
│
└── gemini/                        ← agent ECHO · moteur Gemini CLI
    ├── GEMINI.md
    ├── .gemini/
    │   ├── settings.json
    │   └── commands/go.toml
    ├── references/
    ├── scripts/
    ├── projets/                   ← SES livrables
    │   └── eclipse/
    ├── uxr-state.json
    └── README.md                  ← setup détaillé
```

Rien à la racine à part ce README : tout le contenu vit dans l'un ou l'autre
des deux agents.

---

## Conséquence à connaître

Les deux agents ne se voient pas. Un questionnaire généré côté Gemini
**n'apparaîtra pas** côté Claude Code, et sa mémoire (`uxr-state.json`)
non plus.

En pratique : **choisis un moteur par projet de recherche et tiens-t'y**.
Si tu veux basculer un projet en cours d'un agent à l'autre, il faut copier
à la main son dossier `projets/[nom]/` et son entrée dans `uxr-state.json`.

Le projet Eclipse est présent dans les deux, à l'identique, comme exemple
de référence.

---

## Maintenir les deux en parallèle

`references/` et `scripts/` sont dupliqués dans chaque agent — c'est le prix
de l'étanchéité. **Si tu modifies un template, reporte-le dans les deux
dossiers.**

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

`projets/` en revanche **doit** diverger dès que tu travailles : chaque agent
mène ses propres recherches. Ne cherche pas à les synchroniser.

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
