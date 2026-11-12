#  Server Inventory Tool ⚡

## Om programmet

Server Inventory Tool är ett Pythonprogram som används för att hålla reda på olika servrar.
För varje server sparas namn, adress, miljö, roll, status och vilket datum och vilken tid servern senast kontrollerades.
Användaren kan visa servrarna, lägga till, ta bort, visa servrar med specifik miljö, kontrollera om servrarna svarar på ping samt exportera rapporter som CSV.

Serverdatan och användarens ändringar sparas i en JSON fil så att informationen finns kvar mellan programmets körningar.

## Krav för att köra programmet

För att köra programmet behöver Python 3 vara installerat på datorn.
Programmet kör kommandot ping -c, vilket fungerar på macOS och Linux. 
Inga extra Pythonpaket behöver installeras med pip, eftersom detta program endast använder standardbiblioteket.

## Starta textmenyn

För att starta textmenyn öppnar man terminalen i projektmappen.
Programmet startas sedan med:

```bash
python3 main.py
```

Därefter visas menyvalen 1 till 8.

Val 8 avslutar programmet.

## Använda CLI läget

CLI läget kan man beskriva som att använda genvägar. 
Det gör det möjligt att köra programmets funktioner direkt från terminalen utan att använda textmenyn.

- **Visa alla servrar:**

```bash
python3 main.py --lista
```

- **Visa servrar i miljön prod:**

```bash
python3 main.py --lista --miljo prod
```

*Värdet efter --miljo bestämmer vilken miljö som visas och kan vara dev, test eller prod.*

- **Kontrollera servern web01:**

```bash
python3 main.py --kontrollera web01
```

*Servernamnet `web01` kan bytas mot namnet på en annan server.*

- **Kontrollera alla servrar:**

```bash
python3 main.py --kontrollera-alla
```

- **Exportera en CSV-rapport:**

```bash
python3 main.py --export
```

*Rapportfilens namn innehåller datum och tid.*

- **Visa programmets hjälptext:**

```bash
python3 main.py --help
```

## Miljövariabeln INVENTORY_DATAFIL

`INVENTORY_DATAFIL` används för att välja vilken JSON fil programmet ska läsa och spara serverdata i. Om miljövariabeln inte anges används `servrar.json` som standard. En annan datafil kan väljas när programmet startas.

```bash
INVENTORY_DATAFIL=test_servrar.json python3 main.py
```

*I detta exempel används `test_servrar.json` endast under den aktuella körningen. Om filen inte finns startar programmet med en tom serverlista.*

## Projektstruktur

- **`main.py`**  programmets startpunkt. Läser kommandoradsargument med `argparse` och startar textmenyn när inga argument anges.

- **`meny.py`**  innehåller textmenyn och funktioner för att visa, lägga till, ta bort och välja servrar.

- **`lagring.py`**  läser och sparar serverdata i JSON, hämtar datafilens namn och exporterar CSV-rapporter.

- **`kontroller.py`**  kontrollerar servrar med ping och uppdaterar deras status och senaste kontrolltid.

- **`servrar.json`**  innehåller den sparade serverdatan som programmet läser in.

- **`README.md`**  beskriver programmet och hur det används.

- **`REDOGORELSE.md`**  innehåller förklaringar och motiveringar av programmets kod och struktur.

- **`.gitignore`**  anger vilka filer och kataloger som inte ska skickas till GitHub.

- **`rapporter/`**  skapas automatiskt och innehåller exporterade CSV-rapporter. Katalogen ignoreras av Git.
