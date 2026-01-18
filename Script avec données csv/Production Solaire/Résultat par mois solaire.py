import csv
import matplotlib.pyplot as plt
from datetime import datetime

x_date = []
y_valeurs = []

with open("resultat_prod_elec_solaire.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    next(reader)

    for row in reader:
        if len(row) >= 3 and "solaire" in row[1].lower():
            # Convertir la date en objet datetime
            date_obj = datetime.strptime(row[0], "%Y-%m")

            # Convertir la valeur en float
            valeur_str = row[2].strip()
            if valeur_str:
                valeur = float(valeur_str.replace(",", "."))
            else:
                valeur = 0.0

            x_date.append(date_obj)
            y_valeurs.append(valeur)

# --- NOUVEAU : calcul de la production annuelle ---
production_annuelle = {}
for date, valeur in zip(x_date, y_valeurs):
    annee = date.year
    if annee not in production_annuelle:
        production_annuelle[annee] = 0
    production_annuelle[annee] += valeur

# Transformer en listes triées
annees = sorted(production_annuelle.keys())
valeurs_annuelles = [production_annuelle[a] for a in annees]

# --- Tracer la courbe annuelle ---
plt.figure(figsize=(10,5))
plt.plot(annees, valeurs_annuelles, marker="o", color="blue")

plt.xlabel("Année")
plt.ylabel("Production solaire (TWh)")
plt.title("Évolution annuelle de la production solaire en France")

plt.grid(True)
plt.tight_layout()
plt.show()