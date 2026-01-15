import csv
from datetime import datetime
import matplotlib.pyplot as plt

solaire = {}
totale = {}

# Production solaire
with open("%C3%89volution_de_la_production_solaire_photovolta%C3%AFque_en_France_2024-07-16_13-45.csv", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    next(reader)
    for row in reader:
        date_str, filiere, valeur_str = row[0], row[1], row[2]
        if filiere == "Production solaire" and valeur_str != "":
            solaire[date_str] = float(valeur_str.replace(",", "."))

# Production totale (on somme toutes les filières pour chaque mois)
with open("%C3%89volution_de_la_production_d%27%C3%A9lectricit%C3%A9_en_France_2024-07-16_13-55.csv", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    next(reader)
    for row in reader:
        date_str, filiere, valeur_str = row[0], row[1], row[2]
        if valeur_str != "":
            valeur = float(valeur_str.replace(",", "."))
            totale[date_str] = totale.get(date_str, 0) + valeur

dates = []
parts = []

for date_str in sorted(solaire.keys()):
    if date_str in totale and totale[date_str] > 0:
        date = datetime.strptime(date_str, "%Y-%m")
        part = 100 * solaire[date_str] / totale[date_str]
        dates.append(date)
        parts.append(part)



plt.plot(dates, parts, color="blue")
plt.title("Part du solaire dans la production totale d'électricité")
plt.xlabel("Année")
plt.ylabel("Part du solaire (en %)")
plt.show()
