# Funktioner för att läsa, spara och exportera serverdata. 

import csv                      # Skapar CSV rapporter.
import json                     # Läser och sparar JSON data.
import os                       # Läser miljövariabler. 
from datetime import datetime   # Hanterar datum och tid.
from pathlib import Path        # Hanterar filsökvägar och kontrollerar om filer finns.


# Hämtar datafilens namn från en miljövariabel eller använder standardvärdet.
def hamta_datafil():
    return os.getenv("INVENTORY_DATAFIL", "servrar.json")


# Läser serverdata från JSON och returnerar en lista.
def las_servrar(datafil):       
    fil = Path(datafil)

    if not fil.exists():
        return []

    with fil.open("r", encoding="utf-8") as json_fil:
        return json.load(json_fil) 


# Sparar serverlistan i JSON. 
def spara_servrar(servrar, datafil):
    fil = Path(datafil)

    with fil.open("w", encoding="utf-8") as json_fil:
        json.dump(servrar, json_fil, indent=2, ensure_ascii=False)


# Exporterar serverlistan till en CSV-rapport.
def exportera_csv(servrar):
    rapportkatalog = Path("rapporter")
    rapportkatalog.mkdir(exist_ok=True)

    tidpunkt = datetime.now().strftime("%Y-%m-%d_%H%M")
    rapportfil = rapportkatalog / f"inventering_{tidpunkt}.csv"
    faltnamn = [
        "namn",
        "adress",
        "miljo",
        "roll",
        "status",
        "senast_kontrollerad"
    ]
    
    with rapportfil.open("w", newline="", encoding="utf-8") as csv_fil:
        skrivare = csv.DictWriter(csv_fil, fieldnames=faltnamn)
        skrivare.writeheader()
        skrivare.writerows(servrar)

    print(f"CSV-rapport skapad: {rapportfil}")
    return rapportfil