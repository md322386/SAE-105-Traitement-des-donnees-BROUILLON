import csv
import csv
from datetime import datetime
import matplotlib.pyplot as plt

dates = []
solaire = []
nucleaire = []

with open("%C3%89volution_de_la_production_d%27%C3%A9lectricit%C3%A9_en_France_2024-07-16_13-55.csv", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    next(reader)

    data = {}

    for row in reader:
        if row[2] == "" or len(row[0]) != 7:
            continue

        date = datetime.strptime(row[0], "%Y-%m")
        filiere = row[1]
        valeur = float(row[2].replace(",", "."))

        if date not in data:
            data[date] = {}

        data[date][filiere] = valeur

# On trie les dates et on remplit les listes synchronisées
for date in sorted(data.keys()):
    if "Solaire" in data[date] and "Nucléaire" in data[date]:
        dates.append(date)
        solaire.append(data[date]["Solaire"])
        nucleaire.append(data[date]["Nucléaire"])


plt.figure(figsize=(12, 6))

plt.plot(dates, solaire, label="Solaire", color="orange", linewidth=2)
plt.plot(dates, nucleaire, label="Nucléaire", color="blue", linewidth=2)

plt.title("Production d'énergie : Solaire vs Nucléaire")
plt.xlabel("Année")
plt.ylabel("Production (TWh)")
plt.legend()
plt.grid(True)
plt.show()