# Textmenyn och funktioner för användarens val. 

from kontroller import kontrollera_server, kontrollera_alla_servrar
from lagring import exportera_csv, spara_servrar


# Lista över giltiga miljöer.
GILTIGA_MILJOER = ["dev", "test", "prod"]


# Frågar tills användaren anger en giltig miljö.
def hamta_giltig_miljo():
    while True:
        miljo = input("Ange miljö (dev/test/prod): ").strip().lower()

        if miljo in GILTIGA_MILJOER:
            return miljo

        print("Ogiltig miljö. Försök igen.")


# Söker efter en server med ett visst namn.
def hitta_server(servrar, namn):
    for server in servrar:
        if server["namn"] == namn:
            return server

    return None


# Lägger till en ny server om namnet är ledigt.
def lagg_till_server(servrar, datafil):
    namn = input("Ange serverns namn: ").strip()
    befintlig_server = hitta_server(servrar, namn)

    if befintlig_server is not None:
        print("Det finns redan en server med det namnet.")
        return

    adress = input("Ange serverns adress: ").strip()
    miljo = hamta_giltig_miljo()
    roll = input("Ange serverns roll: ").strip()

    # Skapar en ny server med användarens uppgifter. 
    # Status och senast_kontrollerad sätts till standardvärden.
    ny_server = {
        "namn": namn,
        "adress": adress,
        "miljo": miljo,
        "roll": roll, 
        "status": "unknown",
        "senast_kontrollerad": ""
    }

    servrar.append(ny_server)
    spara_servrar(servrar, datafil)
    print(f"Servern {namn} har lagts till.") 


# Skriver ut servrarna i tydliga kolumner.
def visa_servrar(servrar):
    if not servrar:
        print("Inga servrar att visa.")
        return

    print()
    print(
        f"{'Namn':<15} {'Adress':<20} {'Miljö':<10} "
        f"{'Roll':<20} {'Status':<10} {'Senast kontrollerad':<20}"
    )
    print("-" * 99)

    for server in servrar:
        print(
            f"{server['namn']:<15} {server['adress']:<20} "
            f"{server['miljo']:<10} {server['roll']:<20} "
            f"{server['status']:<10} {server['senast_kontrollerad']:<20}"
        )


# Returnerar servrar som tillhör en viss miljö.
def hamta_servrar_i_miljo(servrar, miljo):
    valda_servrar = []

    for server in servrar:
        if server["miljo"] == miljo:
            valda_servrar.append(server)

    return valda_servrar


# Frågar efter miljö och visar servrarna som tillhör den.
def visa_servrar_i_miljo(servrar):
    miljo = hamta_giltig_miljo()
    valda_servrar = hamta_servrar_i_miljo(servrar, miljo)
    visa_servrar(valda_servrar)


# Tar bort en server från serverlistan.
def ta_bort_server(servrar, datafil):
    namn = input("Ange namnet på servern som ska tas bort: ").strip()
    server = hitta_server(servrar, namn)

    if server is None:
        print("Det finns ingen server med det namnet.")
        return

    # Extra bekräftelse om servern tillhör prod.
    if server["miljo"] == "prod":
        bekraftelse = input(
            "Servern finns i prod. Vill du verkligen ta bort den? (ja/nej): "
        ).strip().lower()

        if bekraftelse != "ja":
            print("Borttagningen avbröts.")
            return

    servrar.remove(server)
    spara_servrar(servrar, datafil)
    print(f"Servern {namn} har tagits bort.")


# Frågar efter en server och kontrollerar om den svarar.
def kontrollera_vald_server(servrar, datafil):
    namn = input("Ange namnet på servern som ska kontrolleras: ").strip()
    server = hitta_server(servrar, namn)

    if server is None:
        print("Det finns ingen server med det namnet.")
        return False

    svarar = kontrollera_server(server)
    spara_servrar(servrar, datafil)
    return svarar


# Kontrollerar alla servrar och sparar resultaten.
def kontrollera_alla_och_spara(servrar, datafil):
    alla_svarar = kontrollera_alla_servrar(servrar)
    spara_servrar(servrar, datafil)
    return alla_svarar


# Visar textmenyn tills användaren väljer att avsluta.
def starta_meny(servrar, datafil):
    while True:
        print("\n--- Server Inventory Tool ---")
        print("1. Visa alla servrar")
        print("2. Visa servrar i en viss miljö")
        print("3. Lägg till en server")
        print("4. Ta bort en server")
        print("5. Kontrollera en server")
        print("6. Kontrollera alla servrar")
        print("7. Exportera rapport som CSV")
        print("8. Avsluta")

        val = input("Välj ett alternativ: ").strip()

        if val == "1":
            visa_servrar(servrar)
        elif val == "2":
            visa_servrar_i_miljo(servrar)
        elif val == "3":
            lagg_till_server(servrar, datafil)
        elif val == "4":
            ta_bort_server(servrar, datafil)
        elif val == "5":
            kontrollera_vald_server(servrar, datafil)
        elif val == "6":
            kontrollera_alla_och_spara(servrar, datafil)
        elif val == "7":
            exportera_csv(servrar)
        elif val == "8":
            print("Avslutar programmet...")
            break
        else:
            print("Ogiltigt val. Försök igen.")