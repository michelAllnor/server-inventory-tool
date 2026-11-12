# Redogörelse - *Server Inventory Tool* 📝

## 1. Tre konstruktioner i koden

Ett exempel på ett villkor finns i funktionen `hamta_giltig_miljo()` i filen `meny.py`. 
Där har jag lagt in att endast *dev*,*test* och *prod* är giltiga miljöer som användaren får ange. 
`if miljo in GILTIGA_MILJOER:` kontrollerar ifall användaren anger (dev,test,prod). 
Om villkoret är `True` returnerar funktionen den angivna miljön. 
Ifall inte så skrivs det ut "*Ogiltig miljö. Försök igen*" och användaren får försöka på nytt.

Ett annat exempel kan vi hitta i funktionen `kontrollera_alla_servrar()` i `kontroller.py`.
Där har jag valt en for loop `for server in servrar:`. 
Loopen går igenom listan `servrar` en server i taget. Under varje varv innehåller variabeln `server` den aktuella serverns dictionary och funktionen `kontrollera_server(server)` anropas.
Om någon kontroll returnerar `False` ändras `alla_svarar` till `False`. 
Efter loopen returnerar funktionen `True` om alla servrar svarade, annars `False`.

Mitt tredje exempel är funktionen `hitta_server()` i filen `meny.py`. Funktionen tar emot parametrarna `servrar` och `namn`. 
`hitta_server()` är en hjälpfunktion som används bakom andra menyval när programmet behöver hitta en viss server. Den används exempelvis när användaren vill lägga till en server, ta bort eller kontrollera en särskild server. 

`servrar` är listan som funktionen söker igenom. `namn` är servernamnet som den letar efter. 
Om namnet hittas så returneras serverns dictionary.
Om ingen server har samma namn som användaren anger returneras `None`.

## 2. Lista med dictionaries 

Varför detta program använder en lista med dictionaries är på grund av det smidiga sättet att samla flera servrar och gå igenom dom med en loop.
Dictionaries gör att varje värde får ett tydligt namn, till exempel `server["adress"]`. 

Alla värden i en server är strängar. Det gäller `namn`, `adress`, `miljo`, `roll`, `status` och `senast_kontrollerad`. Detta syns i funktionen `lagg_till_server()` i `meny.py`, där en ny server skapas som en dictionary. 
En lista passar också bra eftersom programmet kan lägga till och ta bort servrar samt gå igenom dem med loopar.

## 3. JSON och CSV

I `lagring.py` används JSON för att spara programmets serverdata. Funktionerna `las_servrar()` och `spara_servrar()` gör att listan med dictionaries kan läsas och sparas mellan körningarna. CSV används i funktionen `exportera_csv()` för att skapa en lättläst rapport med rader och kolumner. JSON passar därför bra som programmets lagring, medan CSV passar bättre som en rapport som exempelvis kan öppnas i Excel. 

## 4. Moduler och funktioner

Programmet är uppdelat i flera filer med olika ansvar. `main.py` är programmets startpunkt, läser kommandoradsargument och startar textmenyn eller CLI-läget. `meny.py` innehåller textmenyn och funktioner för att visa, lägga till, ta bort och hitta servrar. `lagring.py` innehåller funktioner för att läsa och spara JSON samt exportera CSV. `kontroller.py` innehåller funktionerna `kontrollera_server()` och `kontrollera_alla_servrar()`, som kontrollerar servrar med ping. Uppdelningen gör koden tydligare och samma funktioner kan användas av både textmenyn och CLI-läget.

## 5. Standardbiblioteket

Programmet använder flera moduler från Pythons standardbibliotek. `argparse` används i `main.py` för att läsa kommandoradsargument och `sys` används för att avsluta programmet med rätt exitkod. I `lagring.py` används `json` för serverdatan, `csv` för rapporterna, `os` för miljövariabeln och `pathlib` för filer och kataloger. `datetime` används för datum och tid i kontroller och rapportnamn. I `kontroller.py` används `subprocess` för att köra kommandot `ping`.

## 6. God praxis

Ett exempel på god praxis är att funktionen `hitta_server()` i `meny.py` återanvänds på flera ställen. Det gör att samma söklogik inte behöver skrivas flera gånger. Ett annat exempel är att `hamta_giltig_miljo()` kontrollerar användarens inmatning, vilket förhindrar att en ogiltig miljö sparas. Ett tredje exempel är att funktionerna för att lägga till, ta bort och kontrollera servrar anropar `spara_servrar()` efter ändringar. Det minskar risken att serverdata försvinner om programmet avslutas.

## 7. Källor och hjälpmedel

Jag har använt kursens presentationer om filer, JSON, CSV och standardbiblioteket för att förstå hur de olika delarna fungerar. Uppgiftsbeskrivningen har använts som checklista för att kontrollera att programmets krav är uppfyllda. Jag har också använt AI-verktyget ChatGPT/Codex för att få förklaringar, hjälp med kodens struktur och återkoppling på det jag har skrivit. Visual Studio Code och terminalen har använts för att skriva och testa programmet.
