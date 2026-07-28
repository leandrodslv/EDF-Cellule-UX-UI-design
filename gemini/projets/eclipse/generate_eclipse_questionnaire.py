import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def create_forms_questionnaire(project_name, questions_data, output_path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Questions"

    headers = ["Question", "Type", "Options", "Required", "Subtitle"]
    header_fill = PatternFill("solid", fgColor="2563EB")
    header_font = Font(bold=True, color="FFFFFF", name="Arial", size=11)

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")

    ws.column_dimensions["A"].width = 65
    ws.column_dimensions["B"].width = 18
    ws.column_dimensions["C"].width = 55
    ws.column_dimensions["D"].width = 12
    ws.column_dimensions["E"].width = 45
    ws.row_dimensions[1].height = 25

    section_colors = {
        "Section": "EFF6FF",
        "Choice": "F0FDF4",
        "MultipleChoice": "F0FDF4",
        "Likert": "FFF7ED",
        "Rating": "FFF7ED",
        "Text": "FAFAFA",
        "Paragraph": "FAFAFA",
        "Date": "FAFAFA",
        "Ranking": "FDF4FF",
    }

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

        ws.row_dimensions[row_idx].height = 45

    thin = Side(style="thin", color="E5E7EB")
    for row in ws.iter_rows(min_row=1, max_row=len(questions_data)+1, max_col=5):
        for cell in row:
            cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)

    ws_readme = wb.create_sheet("Instructions import")
    ws_readme["A1"] = "Comment importer dans Microsoft Forms"
    ws_readme["A1"].font = Font(bold=True, size=14, name="Arial")
    instructions = [
        "",
        "1. Ouvrir Microsoft Forms : forms.microsoft.com",
        "2. Cliquer sur 'Nouveau formulaire'",
        "3. Cliquer sur les '...' en haut a droite",
        "4. Selectionner 'Importer depuis Excel'",
        "5. Choisir ce fichier",
        "6. Verifier l'apercu et cliquer 'Importer'",
        "",
        "Note : Les sections (Type=Section) apparaitront comme separateurs.",
        "Les questions Likert apparaitront comme grille d'evaluation.",
        "Verifiez les options apres import.",
    ]
    for i, line in enumerate(instructions, 2):
        ws_readme["A" + str(i)] = line
        ws_readme["A" + str(i)].font = Font(name="Arial", size=11)
    ws_readme.column_dimensions["A"].width = 70

    wb.save(output_path)
    print(f"Questionnaire cree : {output_path}")
    return output_path


questions = [
    {
        "Question": "Votre experience avec l'offre Premium",
        "Type": "Section",
        "Options": "",
        "Required": "false",
        "Subtitle": (
            "Ce questionnaire porte sur votre experience avec la page de tarification "
            "et l'offre Premium. Il prend environ 5 minutes. "
            "Vos reponses sont confidentielles et utilisees uniquement pour ameliorer le produit."
        ),
    },
    # SECTION 2 — PROFIL
    {
        "Question": "A quelle frequence utilisez-vous le produit ?",
        "Type": "Choice",
        "Options": "Tous les jours;Plusieurs fois par semaine;Environ une fois par semaine;Moins d'une fois par semaine",
        "Required": "true",
        "Subtitle": "",
    },
    {
        "Question": "Dans quel contexte principal utilisez-vous le produit ? (plusieurs choix possibles)",
        "Type": "MultipleChoice",
        "Options": "Dans le cadre de mon travail;Pour des projets personnels;Dans un cadre academique / scolaire;Autre",
        "Required": "true",
        "Subtitle": "",
    },
    {
        "Question": "Combien de fois avez-vous consulte la page de tarification ?",
        "Type": "Choice",
        "Options": "Une seule fois;2 a 3 fois;4 fois ou plus;Je ne me souviens pas",
        "Required": "true",
        "Subtitle": "",
    },
    # SECTION 3 — EXPERIENCE
    {
        "Question": "Votre perception de l'offre Premium",
        "Type": "Section",
        "Options": "",
        "Required": "false",
        "Subtitle": "Les questions suivantes portent sur votre ressenti lors de la consultation de la page de tarification.",
    },
    {
        "Question": "Dans quelle mesure etes-vous d'accord avec les affirmations suivantes ?",
        "Type": "Likert",
        "Options": (
            "La difference entre l'offre gratuite et l'offre Premium est claire;"
            "Le prix de l'abonnement annuel me semble justifie par les fonctionnalites proposees;"
            "Je comprends a quoi sert chaque fonctionnalite de l'offre Premium;"
            "Je fais confiance au processus de paiement propose"
        ),
        "Required": "true",
        "Subtitle": "Echelle : Pas du tout d'accord (1) → Tout a fait d'accord (5)",
    },
    {
        "Question": "Parmi les elements suivants, lesquels ont retenu votre attention lors de votre visite sur la page de tarification ? (plusieurs choix possibles)",
        "Type": "MultipleChoice",
        "Options": (
            "Le prix de l'abonnement;"
            "La liste des fonctionnalites incluses;"
            "La difference entre mensuel et annuel;"
            "Les conditions d'annulation ou de remboursement;"
            "Les avis ou temoignages d'autres utilisateurs;"
            "Autre"
        ),
        "Required": "true",
        "Subtitle": "",
    },
    # SECTION 4 — PROBLEMES
    {
        "Question": "Freins et besoins",
        "Type": "Section",
        "Options": "",
        "Required": "false",
        "Subtitle": "Ces questions visent a comprendre ce qui s'est passe lors de votre visite sans finalisation.",
    },
    {
        "Question": "Qu'est-ce qui s'est passe lors de votre derniere visite sur la page de tarification ?",
        "Type": "Paragraph",
        "Options": "",
        "Required": "true",
        "Subtitle": "Decrivez simplement ce que vous avez fait et ce qui vous a amene a quitter sans vous abonner.",
    },
    {
        "Question": "Qu'est-ce qui vous ferait reconsiderer un abonnement annuel ?",
        "Type": "Paragraph",
        "Options": "",
        "Required": "false",
        "Subtitle": "",
    },
    {
        "Question": "Parmi les fonctionnalites suivantes de l'offre Premium, lesquelles vous semblent les plus utiles ? (3 choix max)",
        "Type": "MultipleChoice",
        "Options": (
            "Acces illimite au contenu;"
            "Exports et telechargements;"
            "Collaboration en equipe;"
            "Historique et sauvegardes avancees;"
            "Support prioritaire;"
            "Integrations avec d'autres outils;"
            "Aucune de ces fonctionnalites ne me semble indispensable"
        ),
        "Required": "true",
        "Subtitle": "",
    },
    # SECTION 5 — CLOTURE
    {
        "Question": "Pour aller plus loin",
        "Type": "Section",
        "Options": "",
        "Required": "false",
        "Subtitle": "",
    },
    {
        "Question": "Seriez-vous disponible pour un entretien individuel de 45 minutes afin d'approfondir ces questions ?",
        "Type": "Choice",
        "Options": "Oui, avec plaisir;Peut-etre, selon les disponibilites;Non, merci",
        "Required": "true",
        "Subtitle": "Si oui, nous vous contacterons par email pour trouver un creneau qui vous convient.",
    },
    {
        "Question": "Votre adresse email pour vous recontacter (optionnel)",
        "Type": "Text",
        "Options": "",
        "Required": "false",
        "Subtitle": "Uniquement si vous souhaitez etre recontacte pour un entretien.",
    },
]

create_forms_questionnaire(
    project_name="eclipse",
    questions_data=questions,
    output_path="eclipse-questionnaire.xlsx",
)
