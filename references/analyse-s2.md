# Analyse des réponses — Phase S2

Quand le copilote transmet l'export Forms (.xlsx ou .csv), ECHO génère automatiquement
le classeur d'analyse complet en appelant le script Python.

---

## ÉTAPE 1 — Sauvegarder le fichier reçu

Sauvegarder le fichier reçu dans le dossier du projet :
```
[nom-projet]-reponses.xlsx
```

---

## ÉTAPE 2 — Lancer l'analyse

```bash
pip install pandas openpyxl --break-system-packages -q
python scripts/generate_analysis.py [nom-projet]-reponses.xlsx "[Nom du projet]"
```

Le script génère automatiquement : `[nom-projet]-analyse.xlsx`

---

## CE QUE LE SCRIPT FAIT AUTOMATIQUEMENT

### Détection intelligente des colonnes
- **Likert** : colonnes avec valeurs 1-5 ou libellés d'accord/fréquence/satisfaction
- **QCM** : colonnes catégorielles avec ≤ 10 valeurs uniques
- **Texte libre** : colonnes avec réponses longues et variées
- **ID/Meta** : colonnes date, email, identifiant (exclues des calculs)

### 7 onglets générés — tous liés au Raw Data

| Onglet | Contenu | Calculs |
|--------|---------|---------|
| 📊 Dashboard | KPIs visuels, scores moyens, distributions top QCM | Score moyen global, signaux forts |
| 📋 Raw Data | Données brutes intouchables | — |
| 😊 Satisfaction | Distribution 1-5, score net, questions polarisées | Moy, médiane, écart-type, score net |
| 👤 Profil & Segmentation | Distribution des QCM avec barres visuelles | % par choix |
| 🎯 Priorisation | Matrice impact × fréquence, P1/P2/P3/P4 | Score = (5-moy) × fréq |
| 🔗 Corrélations | Matrice de corrélation + paires significatives | Pearson r |
| ⚖️ Comparaisons | Moyennes Likert par segment QCM, delta max-min | Moyenne par groupe |

---

## SIGNAUX AUTOMATIQUES (Dashboard + Satisfaction)

| Signal | Critère | Couleur |
|--------|---------|---------|
| ✅ Fort | Moyenne ≥ 4.2 | Vert |
| ⚡ Polarisée | Écart-type > 1.5 | Orange |
| ⚠️ À surveiller | % négatif (≤2) > 30% | Orange |
| 🔴 Critique | Moyenne ≤ 2.5 | Rouge |

---

## SCORE DE PRIORISATION

```
Score = (5 − Moyenne satisfaction) × Fréquence d'occurrence
```

- **P1 Critique** : score > 1.5 → Investiguer en entretien immédiatement
- **P2 Important** : score > 0.8 → Inclure dans la prochaine itération design
- **P3 À monitorer** : score > 0.3 → Observer sur la prochaine vague
- **P4 Faible** : score ≤ 0.3 → Documenter, pas d'action immédiate

---

## APRÈS GÉNÉRATION — CE QU'ECHO COMMUNIQUE AU COPILOTE (VOIX 1)

```
ECHO ·  [NOM PROJET] — Phase S2 terminée
────────────────────────────────────────
✅ 7 onglets d'analyse générés
✅ [N] variables Likert analysées
✅ [N] variables QCM segmentées
✅ Corrélations calculées sur [N] paires

📊 Signaux forts détectés :
  🔴 [question critique] — moy. [X]/5
  ⚡ [question polarisée] — σ = [X]
  ✅ [point fort] — moy. [X]/5

🎯 Top priorité P1 : [dimension]
   Score [X] — Action recommandée : [action]

→ Fichier : [nom]-analyse.xlsx
→ Prochaine étape : [selon le mode — rapport final ou Phase 1 entretiens]
```

---

## MODE MIXED — SÉLECTION POUR LES ENTRETIENS

Si `research_mode = "mixed"`, après l'analyse :

1. Identifier les répondants ayant répondu "Oui" à la question de disponibilité
2. Croiser avec les profils P1/P2 de la priorisation
3. Sélectionner [N] profils prioritaires pour les entretiens
4. Émettre le Human Task de recrutement avec la liste et les raisons du choix

```
⏸  ECHO · HUMAN TASK #S2 — Recruter les participants pour les entretiens
────────────────────────────────────────────────────────────────────────
J'ai identifié [N] profils prioritaires parmi les répondants :

→ [Profil A] : [raison basée sur les données]
→ [Profil B] : [raison basée sur les données]

Ces profils ont répondu "disponible" et présentent les patterns
les plus intéressants à explorer en entretien (voir onglet Priorisation).

Ce que j'ai besoin que tu fasses :
→ Contacter ces répondants avec le message ci-dessous
→ Planifier les créneaux d'entretien

Message de contact :
"[message rédigé par ECHO — VOIX 2, neutre]"

Quand c'est fait, dis-moi :
"recrutement confirmé, voici les dates"
```
