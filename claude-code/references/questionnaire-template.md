# Template — Questionnaire Excel → Microsoft Forms (Phase S1)

Génère le questionnaire ET crée le fichier Excel en Python (openpyxl).
Le format doit être directement importable dans Microsoft Forms.

---

## FORMAT MICROSOFT FORMS — COLONNES OBLIGATOIRES

Microsoft Forms accepte un Excel avec ces colonnes exactes :

| Colonne | Contenu | Obligatoire |
|---------|---------|-------------|
| `Question` | Texte de la question | ✅ |
| `Type` | Type de champ (voir types ci-dessous) | ✅ |
| `Options` | Choix séparés par `;` (pour QCM/Choix) | Si QCM |
| `Required` | `true` ou `false` | ✅ |
| `Subtitle` | Description / aide sous la question | Non |

**Types reconnus par Microsoft Forms :**
- `Choice` → QCM choix unique
- `MultipleChoice` → QCM choix multiple
- `Text` → Réponse texte courte
- `Paragraph` → Réponse texte longue
- `Rating` → Étoiles (1-5)
- `Likert` → Échelle d'accord (voir format spécial ci-dessous)
- `Date` → Sélecteur de date
- `Ranking` → Classement par glisser-déposer

---

## STRUCTURE DU QUESTIONNAIRE — 5 SECTIONS TYPE

### SECTION 1 · INTRODUCTION (pas de questions)
Ajouter une ligne avec :
- Type : `Section`
- Question : "À propos de vous"
- Subtitle : "[contexte + pourquoi ce questionnaire + durée estimée + confidentialité]"

### SECTION 2 · PROFIL (2-3 questions max)
Questions comportementales, PAS démographiques en priorité.

Exemples :
```
Question: "À quelle fréquence utilisez-vous [produit/service] ?"
Type: Choice
Options: Tous les jours;Plusieurs fois par semaine;Environ une fois par semaine;Moins d'une fois par semaine;Jamais
Required: true
```

```
Question: "Dans quel contexte utilisez-vous principalement [produit/service] ?"
Type: MultipleChoice
Options: Au travail;À la maison;En déplacement;Autre
Required: true
```

### SECTION 3 · EXPÉRIENCE ACTUELLE (4-6 questions)
Mix de Likert + questions ouvertes courtes.

Likert format spécial — une ligne par dimension :
```
Question: "Dans quelle mesure êtes-vous d'accord avec les affirmations suivantes ?"
Type: Likert
Options: [dimension 1];[dimension 2];[dimension 3]
Subtitle: Échelle : Pas du tout d'accord → Tout à fait d'accord
```

Chaque dimension devient une ligne dans Forms.
Exemple :
```
Options: Je trouve [X] facile à utiliser;Je trouve [X] utile au quotidien;Je recommanderais [X] à un collègue
```

### SECTION 4 · PROBLÈMES & BESOINS (3-4 questions)
Questions ouvertes courtes pour récupérer du qualitatif.

```
Question: "Quelle est la principale difficulté que vous rencontrez avec [X] ?"
Type: Paragraph
Required: true
```

```
Question: "Si vous pouviez changer une seule chose, ce serait quoi ?"
Type: Paragraph
Required: false
```

### SECTION 5 · CLÔTURE (1-2 questions)
```
Question: "Seriez-vous disponible pour un entretien de 45 minutes ?"
Type: Choice
Options: Oui, avec plaisir;Peut-être;Non, merci
Required: true
Subtitle: "Si oui, nous vous contacterons pour trouver un créneau."
```

```
Question: "Votre adresse email pour vous recontacter (optionnel)"
Type: Text
Required: false
```

---

## CODE PYTHON — GÉNÉRATION DE L'EXCEL

```python
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def create_forms_questionnaire(project_name, questions_data, output_path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Questions"

    # En-têtes — format exact attendu par Microsoft Forms
    headers = ["Question", "Type", "Options", "Required", "Subtitle"]
    header_fill = PatternFill("solid", fgColor="2563EB")  # Bleu UXR
    header_font = Font(bold=True, color="FFFFFF", name="Arial", size=11)

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")

    # Largeurs de colonnes
    ws.column_dimensions["A"].width = 60  # Question
    ws.column_dimensions["B"].width = 18  # Type
    ws.column_dimensions["C"].width = 50  # Options
    ws.column_dimensions["D"].width = 12  # Required
    ws.column_dimensions["E"].width = 40  # Subtitle
    ws.row_dimensions[1].height = 25

    # Couleurs alternées par section
    section_colors = {
        "Section": "EFF6FF",   # Bleu très clair
        "Choice": "F0FDF4",    # Vert clair
        "MultipleChoice": "F0FDF4",
        "Likert": "FFF7ED",    # Orange clair
        "Rating": "FFF7ED",
        "Text": "FAFAFA",      # Gris clair
        "Paragraph": "FAFAFA",
        "Date": "FAFAFA",
        "Ranking": "FDF4FF",   # Violet clair
    }

    # Remplir les questions
    for row_idx, q in enumerate(questions_data, 2):
        row_color = section_colors.get(q.get("Type", "Text"), "FFFFFF")
        fill = PatternFill("solid", fgColor=row_color)

        values = [
            q.get("Question", ""),
            q.get("Type", "Text"),
            q.get("Options", ""),
            str(q.get("Required", "true")).lower(),
            q.get("Subtitle", ""),
        ]

        for col, value in enumerate(values, 1):
            cell = ws.cell(row=row_idx, column=col, value=value)
            cell.fill = fill
            cell.font = Font(name="Arial", size=10)
            cell.alignment = Alignment(wrap_text=True, vertical="top")

        ws.row_dimensions[row_idx].height = 40

    # Bordures légères
    thin = Side(style="thin", color="E5E7EB")
    for row in ws.iter_rows(min_row=1, max_row=len(questions_data)+1, max_col=5):
        for cell in row:
            cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)

    # Feuille README pour l'import
    ws_readme = wb.create_sheet("Instructions import")
    ws_readme["A1"] = "Comment importer dans Microsoft Forms"
    ws_readme["A1"].font = Font(bold=True, size=14, name="Arial")
    instructions = [
        "",
        "1. Ouvrir Microsoft Forms : forms.microsoft.com",
        "2. Cliquer sur 'Nouveau formulaire'",
        "3. Cliquer sur les '...' en haut à droite",
        "4. Sélectionner 'Importer depuis Excel'",
        "5. Choisir ce fichier",
        "6. Vérifier l'aperçu et cliquer 'Importer'",
        "",
        "Note : Les sections (Type=Section) apparaîtront comme séparateurs.",
        "Les questions Likert apparaîtront comme grille d'évaluation.",
        "Vérifiez les options après import — certains caractères spéciaux peuvent varier.",
    ]
    for i, line in enumerate(instructions, 2):
        ws_readme["A" + str(i)] = line
        ws_readme["A" + str(i)].font = Font(name="Arial", size=11)
    ws_readme.column_dimensions["A"].width = 70

    wb.save(output_path)
    print(f"✅ Questionnaire créé : {output_path}")
    return output_path
```

---

## APPEL TYPE EN PHASE S1

```python
questions = [
    {
        "Question": "À propos de vous",
        "Type": "Section",
        "Subtitle": "Ce questionnaire prend environ 5 minutes. Vos réponses sont anonymes.",
        "Required": "false"
    },
    {
        "Question": "À quelle fréquence utilisez-vous [X] ?",
        "Type": "Choice",
        "Options": "Tous les jours;Plusieurs fois par semaine;Une fois par semaine;Rarement;Jamais",
        "Required": "true"
    },
    {
        "Question": "Dans quelle mesure êtes-vous d'accord avec les affirmations suivantes ?",
        "Type": "Likert",
        "Options": "[X] est facile à utiliser;[X] me fait gagner du temps;Je recommanderais [X]",
        "Required": "true"
    },
    {
        "Question": "Quelle est votre principale difficulté avec [X] ?",
        "Type": "Paragraph",
        "Required": "true"
    },
    {
        "Question": "Seriez-vous disponible pour un entretien de 45 minutes ?",
        "Type": "Choice",
        "Options": "Oui, avec plaisir;Peut-être;Non merci",
        "Required": "true"
    },
    {
        "Question": "Votre email pour vous recontacter (optionnel)",
        "Type": "Text",
        "Required": "false"
    }
]

create_forms_questionnaire(
    project_name="onboarding-edf",
    questions_data=questions,
    output_path="onboarding-edf-questionnaire.xlsx"
)
```

---

## RÈGLES DE CONCEPTION DU QUESTIONNAIRE

**Longueur** : 8-12 questions max — au-delà le taux de complétion chute
**Ordre** : profil → expérience → problèmes → clôture (toujours cette logique)
**Questions fermées** : toujours proposer "Autre" comme option dans les QCM
**Likert** : toujours 5 points, toujours libellés aux deux extrêmes
**Questions ouvertes** : max 2-3 dans un questionnaire, sinon c'est un entretien
**Question de recrutement** : TOUJOURS inclure "Disponible pour un entretien ?" si mode mixed

**Jamais dans un questionnaire :**
- "Êtes-vous satisfait de..." (orienté positif)
- Doubles négations
- Deux idées dans une seule question
- Plus de 7 options dans un QCM

---

## PHASE S2 — APPEL DU SCRIPT D'ANALYSE

Quand l'humain transmet le fichier d'export Forms, exécuter :

```bash
python scripts/generate_analysis.py <export-forms.xlsx> "<Nom du projet>"
```

Le script génère automatiquement `<nom-projet>-analyse.xlsx` avec :
- 📊 Dashboard — KPIs + navigation + alertes automatiques
- 📋 Données brutes — export intact
- 👤 Profils — distribution des QCM + camemberts
- ⭐ Satisfaction — scores Likert, écart-type, polarisation, graphique barres
- ⚡ Problèmes — matrice impact × fréquence, priorité P1→P4 auto
- 🔗 Corrélations — croisements profil × satisfaction

Après génération, fournir le fichier à l'humain et synthétiser les 3 signaux
forts identifiés (VOIX 1).
