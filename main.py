import time

class robot:
    def __init__(self):
        self.nom = ''
        self.vie = 100
        self.viemax = 100
        self.energie = 5
        self.energiemax = 10
        self.malus = []
        self.xp = 0
        self.xp_lvlup = 20
        self.lvl = 1

Robot = robot()

class monstre:
    def __init__(self):
        self.nom = 'ouaisouais',
        self.vie = 0
        self.viemax = 0
        self.energie = 0
        self.energiemax = 0
        self.malus = []

Monstre = monstre()

def reset():

    Robot.nom = ''
    Robot.vie = 100
    Robot.viemax = 100
    Robot.energie = 5
    Robot.energiemax = 10
    Robot.malus = []

    menu_ecran_titre() #appeler menu titre

def xp():
    print("\nvous avez gagné", monstre.xp)
    if Robot.xp >= Robot.xp_lvl_up :
        Robot.xp = Robot.xp - Robot.xp_lvl_up
        Robot.lvl = Robot.lvl + 1
        Robot.viemax = Robot.viemax + 20
        Robot.energie = Robot.energie + 5
        Robot.energiemax = Robot.energiemax + 5
#A modifier
        Robot.xp_lvl_up = Robot.xp_lvl_up + 15
        print("gain de niveau")
        print("pv : ", Robot.vie, "/", Robot.viemax)
        print("energie", Robot.energie, "/", Robot.energiemax)

    print("prochain niveau : ", Robot.xp, "/", Robot.xp_lvl_up )


def aide():
    print("""\

        _   ___ ___  ___ 
       /_\ |_ _|   \| __|
      / _ \ | || |) | _| 
     /_/ \_\___|___/|___|             
                        """)
    print("Bienvenue dans CYBERFRIEND 2077 !")
    print("---------------------------------")
    print("Afin d'évoluer dans Cyberfriend, il est essentiel que tu uses du diplomate qui est en toi.")
    print("Tu devras dialoguer avec les personnes que tu rencontreras, cependant, les gens peuvent s'offusquer et.. devenir violent")
    print("Il te faudra alors user de la méthode forte pour t'en sortir !")
    print("Afin d'interagir, il faut utiliser des commandes valides proposées.")
    print("Essaye de finir le jeu de manière pacifique, attention tu n'as pas le droit à l'erreur !")
    print("Une fois que c'est compris, écris retour !")
    choix = (input("> "))
    while choix != "retour":
        print("Je n'ai pas bien compris... Tu dois écrire retour. Réessaye !")
        choix = (input("> "))
    if choix == "retour":
        menu_ecran_titre()

def credits():
    print(""")


   ___ ___ ___ ___ ___ _____ ___ 
  / __| _ \ __|   \_ _|_   _/ __|
 | (__|   / _|| |) | |  | | \__ \_
  \___|_|_\___|___/___| |_| |___/                                

                        """)
    print("CRÉDITS CYBERFRIEND 2077")
    print("---------------------------------")
    print("Créé avec amour (et beaucoup de rires/larmes) par trois joyeux lurons !")
    print("Axel ASSELOT")
    print("Romain BINOCHE")
    print("Travis DE ROGEZ")
    print("Merci d'y jouer !")
    print("Pour revenir au menu, écris 'retour'.")
    choix = (input("> "))
    while choix != "retour":
        print("Décidément, écrire retour est plus difficile que je le pensais... Tu dois écrire 'retour'. Réessaye !")
        choix = (input("> "))
    if choix == "retour":
        menu_ecran_titre()

def quitter():
    print("Merci d'avoir joué !")
    exit()



def combat():
    print(" 1 : Attaque")
    print(" 2 : Defense")
    print(" 3 : Inventaire")
    print(" 4 : Fuite")
    choix = int(input("> "))

    if choix == 1:
        attaque()
        attaque_monstre()
        fin_combat()


    if choix == 2:
        tg() #pour éviter l'erreur d'indent

    if choix == 3:
        inventaire()

    if choix == 4:
        fuite()

    else:
        combat()

def Debut_de_partie():
    p = robot()
    p.pseudo = input("Entrez votre pseudo : ")
    if p.pseudo == "":
        print("S'agirait de grandir... \n Allez on recommence : ")
        p.pseudo = input("Entrez votre pseudo : ")
    if p.pseudo == "":
        print("Vous êtes PUNIS."), time.sleep(0.5)
        print("Fermeture dans 3..."), time.sleep(1)
        print("Fermeture dans 2..."), time.sleep(1)
        print("Fermeture dans 1..."), time.sleep(1)
        time.sleep(1)
        quit()
    else : 
        print("Hé bien %s, c'est parti !" % (p.pseudo))
        time.sleep(3)
        print(":.....Oh ! Que se passe-t-il ? Où suis-je ?")
        print("Système: Bonjour", p.pseudo, ", votre système vient d'être reboot, vous vous trouvez en plein milieu de la forêt des Aesirs")
        
        deplacement()


def menu_ecran_titre():
    print('\n'
          '          Bienvenue dans Cyberfriend 2077\n'
          '              1 - Nouvelle partie        \n'
          '              2 - Charger                \n'
          '              3 - Aide                   \n'
          '              4 - Crédits                \n'
          '              5 - Quitter                \n'
          )
    choix = int(input("> "))
    if choix==1:
        Debut_de_partie()

    elif choix==2:
        print("tkt mon sos") #faire le chargement une fois que ce sera codé si on code ça
        menu_ecran_titre()

    elif choix==3:
        aide()

    elif choix==4:
        credits()

    elif choix==5:
        quitter()

class Inventaire():
    def __init__(self):
        self.processeur = 1
        self.carte_graphique = 1
        self.barrette_de_ram = 0
        self.disque_dur = 0
        self.soin = ['processeur','carte_graphique','exit']

Inventaire = Inventaire()
#_______________________________________________________________________________________________________________________
#À REVOIR SANS PYGAME !!
def deplacement():
    print("Système: Où voulez vous allez ?\n"), time.sleep(0.5)
    print("Vers le Nord \n"
          "Vers l'Est \n"
          "Vers le Sud \n"
          "Vers l'Ouest \n"
          )
    choix = input(">")

    if choix == "nord" and "Nord" :
        Nord()

    elif choix == "est" and "Est":
        Est()

    elif choix == "sud" and "Sud":
        Sud()

    elif choix == "ouest" and "Ouest":
        Ouest()

    while choix != "nord" and "Nord" or "est" and "Est" or "sud" and "Sud" or "ouest" and "Ouest" :
        print("Tu dois écrire une direction si tu veux avancer dans l'aventure (ex: nord)")
        choix = input(">")

        if choix == "nord" and "Nord" :
            Nord()

        elif choix == "est" and "Est":
            Est()

        elif choix == "sud" and "Sud":
            Sud()

        elif choix == "ouest" and "Ouest":
            Ouest()

def Nord():
    print("Vous vous dirigez vers le Nord et arrivez #emplacement")

def Est():
    print("Vous vous dirigez vers le Est et arrivez #emplacement")

def Sud():
    print("Vous vous dirigez vers le Sud et arrivez #emplacement")

def Ouest():
    print("Vous vous dirigez vers le Ouest et arrivez #emplacement")
#etc...


#_______________________________________________________________________________________________________________________


def inventaire_soin():

    print("\n")
    if Inventaire.processeur >= 1:
        print(Inventaire.soin.index('processeur') + 1," : Processeur = +10 pv ( x", Inventaire.processeur, ")")

    if Inventaire.carte_graphique >= 1:
        print(Inventaire.soin.index('carte_graphique') + 1, " : carte graphique = +20 pv ( x", Inventaire.carte_graphique, ")")

    if Inventaire.processeur == 0 and Inventaire.carte_graphique == 0 and Inventaire.barrette_de_ram == 0 and Inventaire.disque_dur == 0:
        print("exit")
    print(Inventaire.soin.index('exit') +1, " : exit")
    choix = int(input("\nQue souhaitez-vous faire ? : "))

    if Inventaire.processeur >= 1:
        if choix == Inventaire.soin.index('processeur') + 1:
            Inventaire.processeur = Inventaire.processeur - 1
            Robot.vie = Robot.vie + 10
            print("+10pv")
            if Robot.vie > Robot.viemax:
                Robot.vie = Robot.viemax
            if Inventaire.processeur == 0:
                Inventaire.soin.remove('processeur')
        return

    if Inventaire.carte_graphique >= 1:
        if choix == Inventaire.soin.index('carte_graphique') + 1:
            Inventaire.carte_graphique = Inventaire.carte_graphique - 1
            Robot.vie = Robot.vie + 20
            print("+20pv")
            if Robot.vie > Robot.viemax:
                Robot.vie = Robot.viemax
            if Inventaire.carte_graphique == 0:
                Inventaire.soin.remove('carte_graphique')
        return



    if choix == Inventaire.soin.index('exit') + 1:
        print("exit")

    else:
        inventaire_soin()

def intro_titre():
    print("          ____________________________"), time.sleep(0.1)
    print("         !\_________________________/!\ "), time.sleep(0.1)
    print("         !!     CYBERFRIEND         !! \ "), time.sleep(0.1)
    print("         !!                2077     !!  \ "), time.sleep(0.1)
    print("         !!                         !!  !"), time.sleep(0.1)
    print("         !!      CHARGEMENT         !!  !"), time.sleep(0.1)
    print("         !!       .......           !!  !"), time.sleep(0.1)
    print("         !!                         !!  !"), time.sleep(0.1)
    print("         !!                         !!  !"), time.sleep(0.1)
    print("         !!                         !!  /"), time.sleep(0.1)
    print("         !!_________________________!! /"), time.sleep(0.1)
    print("         !/_________________________\!/"), time.sleep(0.1)
    print("            __\_________________/__/!_"), time.sleep(0.1)
    print("           !_______________________!/"), time.sleep(0.1)
    print("         ________________________"), time.sleep(0.1)
    print("        /oooo  oooo  oooo  oooo /!"), time.sleep(0.1)
    print("       /ooooooooooooooooooooooo/ /"), time.sleep(0.1)
    print("      /ooooooooooooooooooooooo/ /"), time.sleep(0.1)
    print("     /C=_____________________/_/"), time.sleep(0.1)
    time.sleep(3)
    menu_ecran_titre()
intro_titre()
