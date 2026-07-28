"""
Génère eclipse-responses.xlsx — 200 répondants simulés
Distribution calée sur les 15 lignes réelles fournies.
"""
import random
import openpyxl

random.seed(42)

HEADERS = ["ID", "Score Clarté (1-5)", "Score Valeur (1-5)",
           "Principal Frein", "Usage (h/semaine)", "Prêt pour Interview ?"]

# Données réelles (15 lignes)
REAL = [
    ("#001", 2, 4, "Engagement annuel trop long", 12, "OUI"),
    ("#002", 1, 5, "Grille tarifaire illisible", 20, "OUI"),
    ("#003", 4, 2, "Manque de fonctionnalités IA", 3, "NON"),
    ("#004", 2, 4, "Pas d'option mensuelle", 15, "OUI"),
    ("#005", 3, 3, "Trop cher pour un indé", 8, "NON"),
    ("#006", 1, 4, "Processus de validation interne", 25, "OUI"),
    ("#007", 5, 5, "Simple oubli de validation", 10, "NON"),
    ("#008", 2, 4, "Manque de preuves sociales", 14, "OUI"),
    ("#009", 3, 2, "Déjà satisfait du gratuit", 2, "NON"),
    ("#010", 2, 5, "Absence de support prioritaire", 18, "OUI"),
    ("#011", 1, 3, "Nomenclature floue (Pro vs Business)", 9, "OUI"),
    ("#012", 4, 4, "Budget Q3 non débloqué", 11, "NON"),
    ("#013", 2, 5, "Complexité du paiement Stripe", 16, "OUI"),
    ("#014", 3, 3, "Pas de mode sombre en Pro", 7, "NON"),
    ("#015", 1, 4, "Manque de clarté RGPD", 22, "OUI"),
]

# Distribution Clarté : 1→27%, 2→33%, 3→20%, 4→13%, 5→7%
CLARTE_DIST = [1]*27 + [2]*33 + [3]*20 + [4]*13 + [5]*7

# Distribution Valeur : 2→13%, 3→20%, 4→40%, 5→27%
VALEUR_DIST = [2]*13 + [3]*20 + [4]*40 + [5]*27

# Freins pool — pondérés selon distribution observée
FREINS = (
    ["Grille tarifaire illisible"] * 14 +
    ["Nomenclature floue (Pro vs Business)"] * 12 +
    ["Engagement annuel trop long"] * 11 +
    ["Pas d'option mensuelle"] * 10 +
    ["Manque de clarté RGPD"] * 9 +
    ["Complexité du paiement Stripe"] * 8 +
    ["Absence de support prioritaire"] * 8 +
    ["Processus de validation interne"] * 7 +
    ["Manque de preuves sociales"] * 6 +
    ["Trop cher pour un indé"] * 6 +
    ["Budget Q3 non débloqué"] * 5 +
    ["Manque de fonctionnalités IA"] * 4 +
    ["Déjà satisfait du gratuit"] * 4 +
    ["Simple oubli de validation"] * 3 +
    ["Pas de mode sombre en Pro"] * 3 +
    ["Autre"] * 10
)

# Usage h/sem — distribution normale autour de 12h, min 1h max 30h
def rand_usage():
    v = int(random.gauss(12, 6))
    return max(1, min(30, v))

# Prêt interview — 60% OUI (corrélé avec score clarté faible)
def rand_interview(clarte):
    if clarte <= 2:
        return "OUI" if random.random() < 0.72 else "NON"
    elif clarte == 3:
        return "OUI" if random.random() < 0.55 else "NON"
    else:
        return "OUI" if random.random() < 0.30 else "NON"

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Réponses"
ws.append(HEADERS)

# Lignes réelles
for row in REAL:
    ws.append(list(row))

# Lignes simulées
for i in range(16, 201):
    clarte = random.choice(CLARTE_DIST)
    valeur = random.choice(VALEUR_DIST)
    frein = random.choice(FREINS)
    usage = rand_usage()
    interview = rand_interview(clarte)
    ws.append([f"#{str(i).zfill(3)}", clarte, valeur, frein, usage, interview])

wb.save("eclipse-responses.xlsx")
print(f"Dataset généré : eclipse-responses.xlsx — {ws.max_row - 1} répondants")
