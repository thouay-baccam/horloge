from datetime import datetime
import time

def afficherheure_24h(heure_tuple):
    formatheure = f"{heure_tuple[0]:02d}:{heure_tuple[1]:02d}:{heure_tuple[2]:02d}"
    print(formatheure, end="\r")

def afficherheure_am_pm(heure_tuple):
    am_pm = "AM" if heure_tuple[0] < 12 else "PM"
    heure12h = (heure_tuple[0] % 12) or 12
    formatheure = f"{heure12h:02d}:{heure_tuple[1]:02d}:{heure_tuple[2]:02d} {am_pm}"
    print(formatheure, end="\r")

def alarme():
    choixformatheure = input("Choisissez le format de l'alarme ('AM/PM' ou '24H'): ").lower()
    
    if choixformatheure not in ['am/pm', '24h']:
        print("'AM/PM' ou '24H' rien d'autre, merci.")
        return

    if choixformatheure == 'am/pm':
        choix_am_pm = input("Choisissez AM ou PM pour l'alarme: ").upper()
        if choix_am_pm not in ['AM', 'PM']:
            print("Choix invalide pour AM/PM.")
            return
        heure_alarme = tuple(map(int, input(f"Entrez l'heure d'alarme (format sur 12H HH:MM:SS {choix_am_pm}): ").split(':')))
    else:
        heure_alarme = tuple(map(int, input(f"Entrez l'heure d'alarme (format sur 24H HH:MM:SS): ").split(':')))

    while True:
        heuremaintenant = datetime.now().time()

        if choixformatheure == 'am/pm':
            heure_alarme_24h = heure_alarme
            if choix_am_pm == 'PM':
                heure_alarme_24h = ((heure_alarme[0] + 12) % 24, heure_alarme[1], heure_alarme[2])

            afficherheure_am_pm((heuremaintenant.hour, heuremaintenant.minute, heuremaintenant.second))
        elif choixformatheure == '24h':
            heure_alarme_24h = heure_alarme
            afficherheure_24h((heuremaintenant.hour, heuremaintenant.minute, heuremaintenant.second))
        else:
            print("'AM/PM' ou '24H' rien d'autre, merci.")
            return
        
        if (heuremaintenant.hour, heuremaintenant.minute, heuremaintenant.second) == heure_alarme_24h:
            print("\nL'ALARME MARCHE, LET'S GO!")

        time.sleep(1)

alarme()