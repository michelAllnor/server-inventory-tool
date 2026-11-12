# Programmets startpunkt och hantering av kommandoradsargument.

import argparse                 # Läser argument från kommandoraden.
import sys                      # Avslutar programmet med rätt exitkod.

from lagring import exportera_csv, hamta_datafil, las_servrar, spara_servrar
from meny import hitta_server, hamta_servrar_i_miljo, starta_meny, visa_servrar
from kontroller import kontrollera_alla_servrar, kontrollera_server


# Skapar kommandoradsargumenten för programmet.
def skapa_parser():
    parser = argparse.ArgumentParser(
        description="Ett program som hanterar en lista med servrar."
    )
    parser.add_argument(
        "--lista",
        action="store_true",
        help="Visa alla servrar."
    )
    parser.add_argument(
        "--miljo",
        choices=["dev", "test", "prod"],
        help="Visa bara servrar i vald miljö."
    )
    parser.add_argument(
        "--kontrollera",
        metavar="NAMN",
        help="Kontrollera en server med angivet namn."
    )
    parser.add_argument(
        "--kontrollera-alla",
        action="store_true",
        help="Kontrollera alla servrar."
    )
    parser.add_argument(
        "--export",
        action="store_true",
        help="Exportera serverlistan som CSV."
    )
    return parser


# Läser in serverdata och startar textmenyn.
def main():
    parser = skapa_parser()
    args = parser.parse_args()

    datafil = hamta_datafil()
    servrar = las_servrar(datafil)

    if args.miljo and not args.lista:
        parser.error("--miljo måste användas tillsammans med --lista")

    if args.lista:
        if args.miljo:
            servrar = hamta_servrar_i_miljo(servrar, args.miljo)

        visa_servrar(servrar)
        sys.exit(0)

    if args.kontrollera:
        server = hitta_server(servrar, args.kontrollera)

        if server is None:
            print("Det finns ingen server med det namnet.")
            sys.exit(1)

        svarar = kontrollera_server(server)
        spara_servrar(servrar, datafil)

        if svarar:
            sys.exit(0)

        sys.exit(1)

    if args.kontrollera_alla:
        alla_svarar = kontrollera_alla_servrar(servrar)
        spara_servrar(servrar, datafil)

        if alla_svarar:
            sys.exit(0)

        sys.exit(1)


    if args.export:
        exportera_csv(servrar)
        sys.exit(0)            

    starta_meny(servrar, datafil)


# Startar programmet endast när main.py körs direkt.
if __name__ == "__main__":
    main()