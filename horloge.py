import msvcrt
from time import sleep, time

pause = False

def toggle_pause():
    global pause
    pause = not pause
    print("\nL'horloge est en pause" if pause else "\nReprise de l'horloge")

def pm_or_24h():
    clock_type = input("Entrez le type d'affichage de l'heure (AMPM/24H) : ")
    return clock_type.upper()

def dalarme(heure_alarme, minute_alarme, seconde_alarme, heure, minute, seconde):
    if heure_alarme == heure and minute_alarme == minute and seconde_alarme == seconde:
        print("\nL'alarme a sonné")

def afficher_heure(heure_base, alarme):
    heure, minute, seconde = heure_base
    heure_alarme, minute_alarme, seconde_alarme = alarme
    dernier_temps = time()
    affichage = pm_or_24h()

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8')
            if key.lower() == 'p':
                toggle_pause()

        if pause:
            sleep(1)
            continue

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
                am_pm_indicator = "PM" if heure >= 12 else "AM"
                heure_affichage = heure if heure <= 12 else heure - 12
                if heure_affichage == 0:
                    heure_affichage = 12

                print(f"\r\033[K{heure_affichage:02d}:{minute:02d}:{seconde:02d} {am_pm_indicator}", end="", flush=True)
            else:
                print(f"\r\033[K{heure:02d}:{minute:02d}:{seconde:02d}", end="", flush=True)

        dalarme(heure_alarme, minute_alarme, seconde_alarme, heure, minute, seconde)

        sleep(1)


heure = (13, 30, 0)
halarme = (13, 30, 10)
afficher_heure(heure, halarme)
