# EDF · Cellule UX/UI Design

Ce dépôt héberge **ECHO**, agent UXR autonome qui pilote un projet de recherche
utilisateur de A à Z — cadrage, questionnaire, entretiens, analyse, rapport.

ECHO existe en **deux implémentations indépendantes**, une par moteur.
Même méthode, même personnalité, même pipeline — seule la plomberie change.

> **Tu débutes ?** Va directement à [Installation depuis zéro](#installation-depuis-zéro).
> Compte 20 à 30 minutes la première fois. Aucune connaissance en code n'est
> nécessaire : tu vas taper des commandes, pas en écrire.

---

## Installation depuis zéro

Ce guide part du principe que rien n'est installé sur ta machine.
Suis les étapes dans l'ordre — chacune dépend de la précédente.

### Étape 0 · Ouvrir un terminal

Tout se passe dans un terminal. C'est une fenêtre où l'on tape des commandes.

- **Windows** — touche `Windows`, tape `Terminal`, ouvre **Windows Terminal**
  (ou **PowerShell**)
- **macOS** — `Cmd + Espace`, tape `Terminal`, Entrée

Garde-le ouvert, tout le reste s'y passe. Après chaque installation, **ferme et
rouvre le terminal** : c'est ce qui lui permet de découvrir les nouveaux outils.

---

### Étape 1 · Les outils de base

Trois briques sont nécessaires quel que soit l'agent choisi : **Node.js**
(fait tourner les CLI), **Git** (récupère et versionne le dépôt) et **Python**
(génère les fichiers Excel des questionnaires).

**Sur Windows** — copie-colle ces trois lignes une par une :

```powershell
winget install OpenJS.NodeJS.LTS
winget install Git.Git
winget install Python.Python.3.12
```

**Sur macOS** — installe d'abord [Homebrew](https://brew.sh) si tu ne l'as pas,
puis :

```bash
brew install node git python
```

Ferme et rouvre le terminal, puis vérifie que tout répond :

```bash
node --version      # doit afficher v20.x ou plus
git --version
python --version    # macOS : essaie python3 --version
```

> ⚠️ **Piège classique sur Windows** — si `python --version` ouvre le Microsoft
> Store ou affiche *« Python was not found »*, c'est que Windows intercepte la
> commande avec un raccourci fantôme. Correction :
> **Paramètres → Applications → Paramètres avancés des applications →
> Alias d'exécution d'application** → désactive `python.exe` et `python3.exe`.
> Ferme et rouvre le terminal.

---

### Étape 2 · La bibliothèque Excel

ECHO génère les questionnaires au format Microsoft Forms. Il lui faut `openpyxl` :

```bash
pip install openpyxl
```

Sur macOS, si `pip` n'est pas reconnu, utilise `pip3 install openpyxl`.

Sans cette étape, tout fonctionne **sauf** la génération des `.xlsx` (Phase S1).

---

### Étape 3 · Récupérer le dépôt

```bash
git clone https://github.com/leandrodslv/EDF-Cellule-UX-UI-design.git
cd EDF-Cellule-UX-UI-design
```

Le dépôt est **privé** : Git te demandera de t'authentifier sur GitHub.
Si tu n'as pas accès, demande à être ajouté comme collaborateur.

---

### Étape 4 · Installer l'agent de ton choix

Tu n'as besoin **que d'un seul** des deux. Si tu hésites, prends celui pour
lequel la cellule a déjà un compte.

#### Option A — Claude Code

```bash
npm install -g @anthropic-ai/claude-code
cd Agent_claude-code_Echo
claude
```

Au premier lancement, Claude ouvre ton navigateur pour la connexion.
Il faut un **compte Claude** (Pro, Max ou Team) ou une clé API Anthropic.

#### Option B — Gemini CLI

```bash
npm install -g @google/gemini-cli
cd Agent_gemini_Echo
gemini
```

Au premier lancement, choisis **« Login with Google »** et connecte-toi avec
ton compte Google — c'est gratuit et suffisant pour ECHO. Une clé API
[Google AI Studio](https://aistudio.google.com/apikey) fonctionne aussi.

> 🔴 **L'erreur à ne pas faire** — lance toujours le CLI **depuis le dossier
> de l'agent** (`Agent_claude-code_Echo/` ou `Agent_gemini_Echo/`), jamais
> depuis la racine du dépôt.
> Les deux outils cherchent leur fichier de contexte à partir du dossier
> courant : lancés d'ailleurs, tu obtiendras un assistant générique et **ECHO
> ne se réveillera pas**.

---

### Étape 5 · Installer Obsidian

ECHO écrit tous ses livrables dans un **vault Obsidian** : le dossier `cerveau/`
de ton agent. Un vault n'est rien d'autre qu'un dossier de fichiers Markdown
sur ton disque — Obsidian ne fait que le rendre navigable.

**Sur Windows** :

```powershell
winget install Obsidian.Obsidian
```

**Sur macOS** :

```bash
brew install --cask obsidian
```

Puis, au lancement : **Ouvrir un dossier comme vault** → sélectionne le dossier
`cerveau/` de ton agent.

> **Cette étape est facultative.** Sans Obsidian, ECHO fonctionne exactement
> pareil et écrit les mêmes fichiers — tu les liras simplement dans un éditeur
> de texte. Obsidian apporte la navigation, les liens entre notes et les vues,
> pas le contenu.

#### Pourquoi ce choix plutôt qu'un outil en ligne

Aucune donnée de recherche ne quitte ton poste : ni compte, ni serveur, ni API,
ni jeton d'accès. Les verbatims d'entretien restent des fichiers locaux.

Si tu veux sauvegarder et partager avec la cellule, place le vault dans ton
**OneDrive ou SharePoint EDF** : tu récupères la synchronisation, l'historique
de versions et les politiques de sécurité du tenant, sans qu'ECHO n'ait besoin
du moindre accès réseau.

---

### Étape 6 · Vérifier que tout est en place

Depuis le dossier de ton agent, lance-le et tape `/go`.

Si tout est correct, ECHO affiche le tableau de bord du projet Eclipse et te
propose une prochaine étape. **C'est le signe que l'installation est bonne.**

Récapitulatif de contrôle :

| Vérification | Commande | Attendu |
|---|---|---|
| Node.js | `node --version` | `v20.x` ou plus |
| Git | `git --version` | un numéro de version |
| Python | `python --version` | `3.10` ou plus |
| openpyxl | `pip show openpyxl` | une fiche, pas une erreur |
| L'agent | `claude` ou `gemini` | l'interface s'ouvre |
| Le vault | ouvrir `cerveau/` dans Obsidian | `Accueil.md` s'affiche avec le domaine Tarification |
| ECHO | `/go` dans l'agent | le dashboard Eclipse s'affiche |

---

### En cas de blocage

| Symptôme | Cause probable | Correction |
|---|---|---|
| `command not found` après une install | Le terminal n'a pas rechargé le PATH | Ferme et rouvre le terminal |
| `python` ouvre le Microsoft Store | Alias d'exécution Windows | Voir le piège de l'étape 1 |
| `EACCES` / permission refusée sur `npm -g` | Droits d'écriture globaux | macOS/Linux : préfixe par `sudo`. Windows : ouvre le terminal en administrateur |
| ECHO répond comme un assistant générique | Lancé depuis le mauvais dossier | `cd Agent_claude-code_Echo` ou `cd Agent_gemini_Echo`, puis relance |
| Les propriétés YAML n'apparaissent pas dans Obsidian | Ligne vide avant le bloc `---` | Le `---` doit être la toute première ligne du fichier |
| `git clone` refusé | Pas d'accès au dépôt privé | Demande à être ajouté comme collaborateur |

---

## Choisir son agent

| | **Claude Code** | **Gemini CLI** |
|---|---|---|
| Dossier | [`Agent_claude-code_Echo/`](Agent_claude-code_Echo/) | [`Agent_gemini_Echo/`](Agent_gemini_Echo/) |
| Cerveau | `CLAUDE.md` | `GEMINI.md` |
| Commande | `.claude/commands/go.md` | `.gemini/commands/go.toml` |
| Config | `.claude/` | `.gemini/settings.json` |
| Lancement | `cd Agent_claude-code_Echo && claude` | `cd Agent_gemini_Echo && gemini` |

Les deux agents sont **totalement étanches**. Chacun embarque ses propres
`references/`, `scripts/`, `uxr-state.json` **et `cerveau/`**. Aucun fichier
n'est partagé, aucun chemin ne traverse d'un dossier à l'autre.

Concrètement : tu peux copier `Agent_gemini_Echo/` seul sur une clé USB et le
donner à un collègue — il fonctionnera tel quel, sans le reste du dépôt.

> **Important** — lance toujours le CLI *depuis le dossier de l'agent*, jamais
> depuis la racine. Les deux outils cherchent leur fichier de contexte à partir
> du dossier courant : lancés d'ici, ils ne trouveraient rien.

---

## Arborescence

```
EDF-Cellule-UX-UI-design/
├── README.md                       ← ce fichier
│
├── Agent_claude-code_Echo/         ← agent ECHO · moteur Claude Code
│   ├── CLAUDE.md
│   ├── .claude/commands/go.md
│   ├── references/
│   ├── scripts/
│   ├── cerveau/                    ← SON second cerveau (vault Obsidian)
│   │   ├── Accueil.md
│   │   ├── 00-Inbox/
│   │   ├── 01-Projets/
│   │   ├── 02-Domaines/
│   │   ├── 03-Connaissances/
│   │   ├── 04-Ressources/
│   │   └── 05-Archives/
│   ├── uxr-state.json
│   └── README.md                   ← setup détaillé
│
└── Agent_gemini_Echo/              ← agent ECHO · moteur Gemini CLI
    ├── GEMINI.md
    ├── .gemini/
    │   ├── settings.json
    │   └── commands/go.toml
    ├── references/
    ├── scripts/
    ├── cerveau/                    ← SON second cerveau (vault Obsidian)
    │   ├── Accueil.md
    │   ├── 00-Inbox/
    │   ├── 01-Projets/
    │   ├── 02-Domaines/
    │   ├── 03-Connaissances/
    │   ├── 04-Ressources/
    │   └── 05-Archives/
    ├── uxr-state.json
    └── README.md                   ← setup détaillé
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
à la main son dossier `cerveau/01-Projets/[nom]/` et son entrée dans
`uxr-state.json`.

**Et surtout** : les connaissances accumulées ne se partagent pas non plus.
Ce que l'agent Gemini a appris reste invisible à l'agent Claude Code. Un
second cerveau ne vaut que par ce qu'il accumule — le diviser en deux, c'est
diviser la mémoire de la cellule.

**Recommandation** : désigne un moteur principal pour la cellule et tiens-t'y.
Garde le second pour l'expérimentation, pas pour les études qui comptent.

Le projet Eclipse est présent dans les deux, à l'identique, comme exemple
de référence.

---

## Maintenir les deux en parallèle

`references/` et `scripts/` sont dupliqués dans chaque agent — c'est le prix
de l'étanchéité. **Si tu modifies un template, reporte-le dans les deux
dossiers.**

Vérifier qu'ils n'ont pas divergé :

```bash
diff -r Agent_claude-code_Echo/references Agent_gemini_Echo/references
diff -r Agent_claude-code_Echo/scripts    Agent_gemini_Echo/scripts
```

Les deux doivent être **strictement identiques** — aucune sortie attendue.

Depuis l'abandon de Notion, il n'y a plus aucune divergence légitime entre les
deux agents sur ces dossiers : la moindre différence est une dérive à corriger.

`cerveau/` en revanche **doit** diverger dès que tu travailles : chaque agent
mène ses propres recherches. Ne cherche pas à les synchroniser.

---

## Le second cerveau

ECHO ne se contente pas de mener des études : il **capitalise**.

Le problème qu'on cherche à éviter est classique en cellule de recherche —
chaque étude repart de zéro, les mêmes questions sont reposées, et les
enseignements dorment dans des rapports que plus personne ne rouvre. Six mois
après, quelqu'un redécouvre ce qui était déjà écrit.

Le vault de chaque agent est donc organisé en **PARA** (Tiago Forte), avec une
couche de connaissances inspirée de l'**Atomic Research** — chaque enseignement
devient un *nugget* : une observation, ses preuves, sa taxonomie.

```
00-Inbox/          capture brute à trier
01-Projets/        études en cours
02-Domaines/       sujets permanents — une carte par domaine
03-Connaissances/  ce que la cellule sait, indépendamment des projets
04-Ressources/     méthodes, biais, benchmarks
05-Archives/       études terminées
```

### Les deux couches

| | Insight | Connaissance |
|---|---|---|
| Portée | Un projet | Transversale |
| Durée de vie | Meurt avec le projet | S'enrichit à chaque étude |
| Exemple | « Dans Eclipse, 6/8 ont buté sur la grille » | « Les utilisateurs ne distinguent pas les paliers » |

Un projet se termine et s'archive. Une connaissance reste et se consolide.

### Ce que ça change concrètement

**Avant une étude** — ECHO lit le domaine concerné et te dit ce que la cellule
sait déjà, avec quel niveau de confiance, et ce qui n'a jamais été exploré.
Une étude qui redécouvre une connaissance établie est une étude gâchée : il
doit te le dire *avant* qu'elle ne démarre.

**Après une analyse** — chaque insight est distillé. S'il confirme une
connaissance existante, celle-ci gagne en confiance. S'il la contredit, la
connaissance passe en `a-reverifier` et la contradiction remonte au pilote —
elle n'est jamais effacée en silence.

**Au fil du temps** — une connaissance non reconfirmée depuis 12 mois est
signalée comme potentiellement périmée. Un produit qui bouge invalide ce
qu'on savait de lui.

### Niveaux de confiance

| Niveau | Critère |
|---|---|
| `faible` | 1 étude, ou moins de 3 participants |
| `moyenne` | 1 étude solide, 5+ participants, ou 2 études convergentes |
| `forte` | 2+ études indépendantes convergentes |
| `etablie` | 3+ études, dont une avec un dispositif différent |

Une connaissance issue d'un questionnaire déclaratif ne dépasse jamais
`moyenne` tant qu'elle n'a pas été confirmée en entretien : déclarer n'est
pas faire.

La méthode complète est dans `references/second-cerveau.md` de chaque agent.

---

## Sécurité des données

### Ce qui a changé

ECHO utilisait Notion, un service tiers hébergé hors du périmètre EDF.
Il n'en dépend plus. Les livrables sont désormais des fichiers Markdown écrits
dans un **vault Obsidian** local.

Concrètement, les agents n'ont plus **aucun connecteur réseau** : ni MCP, ni
API, ni jeton d'accès, ni compte à provisionner. Écrire un livrable revient à
écrire un fichier sur le disque.

| | Avant (Notion) | Maintenant (Obsidian) |
|---|---|---|
| Hébergement des livrables | Serveurs Notion | Disque du poste |
| Compte tiers requis | Oui | Non |
| Jeton d'accès à gérer | Oui (OAuth) | Aucun |
| Accès réseau de l'agent | Oui | **Aucun** |
| Gouvernance applicable | Celle de Notion | Celle d'EDF, si vault dans OneDrive |
| Fonctionne hors ligne | Non | Oui |

### Sauvegarde et partage

Un vault local n'est pas sauvegardé. Place le dossier `cerveau/` dans ton
**OneDrive ou SharePoint EDF** : tu obtiens la synchronisation, l'historique
de versions et les politiques de rétention du tenant — sans qu'ECHO n'accède
lui-même au réseau.

### Règles inscrites dans les agents

Les deux cerveaux interdisent explicitement :

- d'envoyer, publier ou téléverser une donnée de recherche où que ce soit
- d'écrire un nom, un employeur ou toute donnée identifiante dans un livrable
  — les participants sont désignés par un identifiant (`#001`, `#002`)
- d'écrire ou lire quoi que ce soit hors du dossier de l'agent

### Ce qui reste exposé — à savoir

Le stockage est désormais local, **le traitement ne l'est pas**. Quand tu
transmets des notes d'entretien à ECHO pour analyse, leur contenu est envoyé
au fournisseur du modèle (Anthropic ou Google) le temps de la requête.

La pseudonymisation systématique des participants limite la portée de cette
exposition, mais ne la supprime pas. Si la cellule traite un jour des verbatims
sensibles, c'est ce point — et non le stockage — qu'il faudra instruire avec la
sécurité EDF.

### Migration en cours

Le projet Eclipse a été produit dans Notion avant la bascule. Sa partie
rédactionnelle doit encore être exportée : la marche à suivre est dans
`cerveau/00-Inbox/_migration-notion.md`, dans chaque agent.

Tant que ce n'est pas fait, ces données existent encore chez Notion.

---

## Projet de référence — Eclipse

Projet UXR complet et terminé, mode `mixed` (questionnaire + entretiens) :
200 réponses au questionnaire, 8 entretiens, analyse et rapport livrés.
Sert d'exemple de bout en bout, présent à l'identique dans
`cerveau/05-Archives/eclipse/` de chaque agent — archivé, mais ce qu'il a
appris vit dans `cerveau/03-Connaissances/`.

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
