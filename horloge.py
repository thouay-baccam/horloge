import msvcrt
from time import sleep, time

def toggle_pause(est_en_pause):
    return not est_en_pause

def obtenir_type_horloge():
    while True:
        type_horloge = input("Entrez le type d'affichage de l'heure (AMPM/24H) : ").upper()
        if type_horloge in ['AMPM', '24H']:
            return type_horloge
        else:
            print("Veuillez entrer une option valide (AMPM/24H).")

def alarme(heure_alarme, minute_alarme, seconde_alarme, heure, minute, seconde):
    if heure_alarme == heure and minute_alarme == minute and seconde_alarme == seconde:
        print("\nL'alarme a sonné")

def afficher_heure(heure_base, heure_alarme, est_en_pause):
    heure, minute, seconde = heure_base
    heure_alarme, minute_alarme, seconde_alarme = heure_alarme
    dernier_temps = time()
    affichage = obtenir_type_horloge()

    while True:
        if msvcrt.kbhit():
            touche = msvcrt.getch().decode('utf-8')
            if touche.lower() == 'p':
                est_en_pause = toggle_pause(est_en_pause)

        if est_en_pause:
            sleep(1)
            continue

        alarme(heure_alarme, minute_alarme, seconde_alarme, heure, minute, seconde)  # Vérifier l'alarme en premier

        temps_actuel = time()
        temps_ecoule = temps_actuel - dernier_temps

        if temps_ecoule >= 1:
            seconde += 1
            dernier_temps = temps_actuel

            if seconde >= 60:
                minute += seconde // 60
                seconde %= 60

                if minute >= 60:
                    heure += minute // 60
                    minute %= 60

                    if heure >= 24:
                        heure %= 24

            if affichage == "AMPM":
                indicateur_am_pm = "PM" if heure >= 12 else "AM"
                heure_affichage = heure if heure <= 12 else heure - 12
                if heure_affichage == 0:
                    heure_affichage = 12

                print(f"\r\033[K{heure_affichage:02d}:{minute:02d}:{seconde:02d} {indicateur_am_pm}", end="", flush=True)
            else:
                print(f"\r\033[K{heure:02d}:{minute:02d}:{seconde:02d}", end="", flush=True)

        sleep(1)

# Paramètres initiaux de l'heure
heure_base = (13, 30, 0)
heure_alarme = (13, 30, 5)
est_en_pause = False

# Démarrer l'horloge
afficher_heure(heure_base, heure_alarme, est_en_pause)