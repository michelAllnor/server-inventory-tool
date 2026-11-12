# Funktioner för att kontrollera servrar med ping. 

import subprocess  # Använder ping-kommandot för att kontrollera serverstatus.
from datetime import datetime


# Kontrollerar om en server svarar på ping.
def kontrollera_server(server):
    kommando = ["ping", "-c", "1", server["adress"]]
    resultat = subprocess.run(kommando, capture_output=True, text=True)

    if resultat.returncode == 0:
        server["status"] = "up"
    else:
        server["status"] = "down"

    server["senast_kontrollerad"] = datetime.now().strftime("%Y-%m-%d %H:%M")

    print(f"{server['namn']}: {server['status']}")
    return server["status"] == "up"


# Kontrollerar ALLA servrar och returnerar True om alla svarar.
def kontrollera_alla_servrar(servrar):
    alla_svarar = True

    for server in servrar:
        if not kontrollera_server(server):
            alla_svarar = False

    return alla_svarar