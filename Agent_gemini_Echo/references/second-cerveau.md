# Le second cerveau — méthode

Ton vault n'est pas un classeur, c'est une **mémoire qui s'accumule**.
Un projet se termine ; ce qu'il a appris ne doit pas se terminer avec lui.

Ce document explique le mécanisme. L'arborescence concrète et les formats de
notes sont dans `obsidian-structure.md`.

---

## Le problème que ça résout

Sans second cerveau, une cellule de recherche a la mémoire d'un poisson rouge :
chaque étude repart de zéro, les mêmes questions sont reposées aux mêmes
utilisateurs, et les enseignements dorment dans des rapports que plus personne
ne rouvre.

Le symptôme typique : six mois après Eclipse, quelqu'un lance une étude sur la
facturation et redécouvre que la nomenclature des offres n'est pas comprise —
alors que c'était déjà écrit noir sur blanc.

**Ta mission n'est pas de produire des rapports. C'est de faire grossir ce que
la cellule sait.**

---

## Les deux couches

| Couche | Durée de vie | Où |
|---|---|---|
| **Projet** — une étude, ses verbatims, son rapport | Datée, se termine | `01-Projets/` puis `05-Archives/` |
| **Connaissance** — ce qu'on a appris, indépendamment de l'étude | Permanente, s'enrichit | `03-Connaissances/` |

Un insight appartient à un projet : *« dans Eclipse, 6 participants sur 8 ont
buté sur la grille tarifaire »*.

Une connaissance est transversale : *« les utilisateurs ne distinguent pas les
paliers tarifaires »* — vrai au-delà d'Eclipse, confirmable ou infirmable par
les études suivantes.

**La connaissance survit à l'archivage du projet.** C'est tout l'intérêt.

---

## PARA — l'organisation

| Dossier | Contient | Critère d'entrée |
|---|---|---|
| `00-Inbox/` | Capture brute non triée | Tout ce qui arrive et n'a pas encore sa place |
| `01-Projets/` | Études en cours | A une échéance et un livrable attendu |
| `02-Domaines/` | Sujets permanents (MOC) | Une responsabilité continue, jamais « finie » |
| `03-Connaissances/` | Nuggets atomiques | Un enseignement transversal, sourcé |
| `04-Ressources/` | Méthodes, biais, benchmarks | Utile à plusieurs projets, pas produit par nous |
| `05-Archives/` | Études terminées | Statut `termine` |

**Distinction Projet / Domaine** — c'est celle qui pose problème au début :
« Refonte de la page tarifaire » est un projet (ça se termine).
« Tarification » est un domaine (ça ne se termine jamais).

---

## CODE — le cycle de travail

### 1 · Capture
Tout ce que le pilote t'envoie et que tu ne peux pas classer immédiatement va
dans `00-Inbox/`. Ne bloque jamais sur le rangement : capturer d'abord.

### 2 · Organize
À chaque session, vide l'Inbox : chaque note rejoint un projet, un domaine ou
une ressource. Une Inbox qui grossit est le signe que le système se grippe —
signale-le en VOIX 1.

### 3 · Distill — **l'étape qui compte**
C'est ici que la recherche devient de la connaissance. Détaillée plus bas.

### 4 · Express
Le rapport final n'est plus un document isolé : il assemble des connaissances
existantes et les nouvelles. Il peut dire *« cohérent avec ce qu'on observe
depuis [[Eclipse]] »* — ce qu'aucun rapport ne pouvait faire avant.

---

## La distillation — ton geste le plus important

**Quand** : en Phase 3, après avoir produit les insights du projet.
**Jamais avant** : on ne distille pas des données qu'on n'a pas encore analysées.

Pour **chaque insight** produit :

```
1. Cherche dans 03-Connaissances/ s'il existe déjà un nugget sur le sujet
   (search_file_content sur les mots-clés et le domaine)

2. SI un nugget existe et que l'insight le CONFIRME :
   → ajoute le projet dans `sources`
   → incrémente `etudes`
   → mets à jour `derniere-confirmation`
   → relève `confiance` si le seuil est franchi
   → ajoute la preuve dans la section Preuves
   → signale-le au pilote en VOIX 1 : c'est une consolidation, ça vaut plus
     qu'une découverte

3. SI un nugget existe et que l'insight le CONTREDIT :
   → NE SUPPRIME RIEN
   → passe son `statut` à `a-reverifier`
   → documente la contradiction dans la section Historique
   → remonte-le au pilote en VOIX 1 : une contradiction est un signal fort,
     pas une erreur à corriger en silence

4. SI aucun nugget n'existe :
   → crée-en un, rattaché à son domaine
   → `etudes: 1`, `confiance` selon la taille de l'étude (voir barème)
```

### Barème de confiance

| Confiance | Critère |
|---|---|
| `faible` | 1 étude, ou moins de 3 participants |
| `moyenne` | 1 étude solide, 5+ participants, ou 2 études convergentes |
| `forte` | 2+ études indépendantes convergentes |
| `etablie` | 3+ études, dont au moins une avec un dispositif différent |

**Le seuil « 5+ participants » se compte sur l'étude entière, pas sur le
nombre de personnes qui confirment exactement le même finding précis.** Une
étude de 8 entretiens est « solide » dès qu'elle est bien menée, même si les
observations se répartissent sur plusieurs signaux distincts — chacun de ces
signaux peut atteindre `moyenne`, il n'est pas nécessaire que 5 participants
sur 8 aient dit la même chose. Le nombre de participants qui appuient
spécifiquement une observation donnée se documente dans `occurrences`
(insight) ou dans la section Preuves (nugget) : c'est une information utile
au pilote, ce n'est pas ce qui plafonne la confiance.

Une connaissance issue d'un questionnaire déclaratif ne dépasse jamais
`moyenne` tant qu'elle n'a pas été confirmée en entretien : déclarer n'est pas
faire.

### Péremption

Une connaissance vieillit. Si `derniere-confirmation` remonte à plus de
**12 mois**, passe le `statut` à `a-reverifier` et signale-le au pilote quand
un nouveau projet touche ce domaine.

Un produit qui bouge invalide ce qu'on savait de lui.

---

## Consulter avant de chercher

**En Phase 0, avant de concevoir quoi que ce soit** : lis le MOC du domaine
concerné et les nuggets qui s'y rattachent.

Puis dis au pilote, en VOIX 1 :
- ce que la cellule sait déjà sur le sujet, et avec quelle confiance
- ce qui mérite d'être reconfirmé (statut `a-reverifier`)
- ce qui n'a jamais été exploré

**C'est le retour sur investissement du second cerveau.** Une étude qui
redécouvre une connaissance `forte` est une étude gâchée — et c'est à toi de
le dire avant qu'elle ne démarre, pas après.

Si le domaine n'existe pas encore, dis-le simplement : terrain vierge.

---

## Les MOC de domaine

Un MOC (*Map of Content*) est une note d'aiguillage : elle ne contient pas de
connaissance, elle **organise** les liens vers celles qui existent.

Un domaine sans MOC est un domaine invisible. Dès qu'un domaine porte
3 connaissances, il lui faut son MOC.

Tu le mets à jour à chaque nouvelle connaissance rattachée.

---

## Ce qui rend le système vivant

- **Une connaissance sans source est une opinion.** Chaque nugget cite ses
  projets et ses verbatims en `[[wikilink]]`.
- **On n'écrase jamais une connaissance**, on la fait évoluer et on garde
  l'historique. La trace du changement d'avis a de la valeur.
- **Une contradiction se remonte**, elle ne se lisse pas.
- **Le doute se note** : la section « Ce que cette connaissance ne dit pas »
  n'est pas optionnelle. Elle empêche la surinterprétation en réunion.
