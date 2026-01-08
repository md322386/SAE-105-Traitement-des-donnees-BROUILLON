import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

x_date = []
y_valeurs = []

with open("%C3%89volution_de_la_production_solaire_photovolta%C3%AFque_en_France__2025-12-18_13-22.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    next(reader)

    for row in reader:
        if len(row) >= 3 and "solaire" in row[1].lower():
            # Convertir la date en objet datetime
            date_obj = datetime.strptime(row[0], "%Y-%m")
            x_date.append(date_obj)

            # Convertir la valeur en float (remplacer virgule par point)
            valeur_str = row[2].strip()
            if valeur_str:
                valeur = float(valeur_str.replace(",", "."))
            else:
                valeur = 0.0
            y_valeurs.append(valeur)

# Tracer la courbe
plt.plot(x_date, y_valeurs, color="blue")
plt.xlabel("Année")
plt.ylabel("Production solaire (TWh)")
plt.title("Évolution de la production solaire en France en 2025")

# Format de l'axe X : années uniquement tous les 2 ans pour ne pas avoir beacoup de répetition
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
plt.gca().xaxis.set_major_locator(mdates.YearLocator(2))

plt.grid(True)
plt.tight_layout()
plt.show()