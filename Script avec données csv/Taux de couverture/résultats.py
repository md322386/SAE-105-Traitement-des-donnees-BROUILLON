import csv
from datetime import datetime
import matplotlib.pyplot as plt

dates_max = []
valeurs_max = []

dates_moy = []
valeurs_moy = []

with open("Taux_de_couverture_solaire_2025-12-18_13-22.csv", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    next(reader)

    for row in reader:
        date_str, filiere, valeur_str = row[0], row[1], row[2]
        valeur = float(valeur_str.replace(",", "."))

        if "max" in filiere:
            dates_max.append(datetime.strptime(date_str, "%Y"))
            valeurs_max.append(valeur)

        elif "moyen" in filiere:
            dates_moy.append(datetime.strptime(date_str, "%Y-%m"))
            valeurs_moy.append(valeur)





# Courbe pour le taux max annuel
plt.plot(dates_max, valeurs_max, color="purple", marker="o", )

plt.title("Taux de couverture solaire en France (2014–2025)")
plt.xlabel("Année")
plt.ylabel("Taux de couverture (%)")
plt.grid(True)
plt.show()