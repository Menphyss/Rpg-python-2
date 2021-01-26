import time, sys
from random import randint

class robot:
    def __init__(self):
        self.nom = ''
        self.vie = 100
        self.viemax = 100
        self.energie = 5
        self.energiemax = 10
        self.bonus = []
        self.xp = 0
        self.xp_lvlup = 20
        self.lvl = 1
        self.armure = 5
        self.attaque = 10
        self.ennemistues = []
        self.boostattaque = 0
        self.boostarmure = 0

Robot = robot()

class monstre:
    def __init__(self):
        self.nom = ''
        self.vie = 0
        self.viemax = 0
        self.energie = 0
        self.energiemax = 0
        self.bonus = []
        self.attaque = 0
        self.xpdonne = 0
        self.argent = 0

Monstre = monstre()

class Inventaire():
    def __init__(self):
        self.processeur = 1
        self.argent = 200
        self.carte_graphique = 1
        self.barrette_de_ram = 1
        self.huile_de_moteur = 1
        self.soin = ['processeur', 'carte_graphique', 'barrette_de_ram', 'huile_de_moteur', 'exit']

def inventaire_soin():
    print("\n")
    if Inventaire.processeur >= 1:
        print(Inventaire.soin.index('processeur') + 1, " : Processeur = +10 PV ( x", Inventaire.processeur, ")")

    if Inventaire.carte_graphique >= 1:
        print(Inventaire.soin.index('carte_graphique') + 1, " : Carte graphique = +20 PV ( x",
              Inventaire.carte_graphique, ")")

    if Inventaire.barrette_de_ram >= 1:
        print(Inventaire.soin.index('barrette_de_ram') + 1, " : Barrette de ram = +15 d'Attaque ( x",
              Inventaire.barrette_de_ram, ")")

    if Inventaire.huile_de_moteur >= 1:
        print(Inventaire.soin.index('huile_de_moteur') + 1, " : Huile de moteur = +5 d'Attaque +10 d'Armure ( x",
              Inventaire.huile_de_moteur, ")")

    if Inventaire.processeur == 0 and Inventaire.carte_graphique == 0 and Inventaire.barrette_de_ram == 0 and Inventaire.huile_de_moteur == 0:
        print("exit")
    print(Inventaire.soin.index('exit') + 1, " : exit")
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

    if Inventaire.barrette_de_ram >= 1:
        if choix == Inventaire.soin.index('barrette_de_ram') + 1:
            Inventaire.barrette_de_ram = Inventaire.barrette_de_ram - 1
            Robot.attaque += 15
            Robot.boostattaque += 15
            print("Tu as gagné 15 d'Attaque !")
            if Inventaire.barrette_de_ram == 0:
                Inventaire.soin.remove('barrette_de_ram')
        return

    if Inventaire.huile_de_moteur >= 1:
        if choix == Inventaire.soin.index('huile_de_moteur') + 1:
            Inventaire.huile_de_moteur = Inventaire.huile_de_moteur - 1
            Robot.Attaque += 5
            Robot.boostattaque += 5
            Robot.armure += 10
            Robot.boostarmure += 10
            print("Tu as gagné 5 d'Attaque et 10 d'Armure ")
            if Inventaire.huile_de_moteur == 0:
                Inventaire.soin.remove('huile_de_moteur')
        return

    if choix == Inventaire.soin.index('exit') + 1:
        print("exit")

    else:
        inventaire_soin()

def argent():
    Inventaire.argent += Monstre.argent
    print("Vous récoltez", Monstre.argent, "Euro-Dollars")

Inventaire = Inventaire()

def printlent(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.2)

def reset():
        Robot.nom = ''
        Robot.vie = 100
        Robot.viemax = 100
        Robot.energie = 5
        Robot.energiemax = 10
        Robot.bonus = []
        Robot.xp = 0
        Robot.xp_lvlup = 20
        Robot.lvl = 1
        Robot.armure = 5
        Robot.ennemistues = []
        Robot.attaque = 10
        Robot.boostattaque = 0
        Robot.boostarmure = 0

def xp():
    print("\nVous avez gagné", Monstre.xpdonne, "points d'expérience.")
    Robot.xp = Robot.xp + Monstre.xpdonne
    lvlup()

def lvlup():
    while Robot.xp >= Robot.xp_lvlup:
        Robot.xp = Robot.xp - Robot.xp_lvlup
        Robot.lvl = Robot.lvl + 1
        Robot.viemax = Robot.viemax + 20 # AJOUTER LE FAIT DE CHECK SI YA PAS UN SECOND LVL UP APRES
        Robot.vie = Robot.viemax
        Robot.energie = Robot.energie + 5
        Robot.energiemax = Robot.energiemax + 5
        Robot.attaque = Robot.attaque + 5
        Robot.armure = Robot.armure + 2
        # A modifier
        Robot.xp_lvl_up = Robot.xp_lvlup + 15
        print("Vous avez gagné un niveau ! Vos stats augmentent.")
        print("PV : ", Robot.vie, "/", Robot.viemax)
        print("Energie : ", Robot.energie, "/", Robot.energiemax)
        print("Attaque : ", Robot.attaque)
        print("Armure : ", Robot.armure)
        print("Vous êtes maintenant niveau", Robot.lvl, "!")
        print("Prochain niveau dans", (Robot.xp_lvlup - Robot.xp), "XP.")

def MichelleStats():
    Pacifique = False
    Monstre.nom = 'Michelle'
    Monstre.vie = int(Robot.viemax * 0.80)
    Monstre.attaque = int(Robot.attaque * 0.20)
    Monstre.armure = int(Robot.armure * 0.25)
    Monstre.xpdonne = int(Robot.xp_lvlup * 0.5)
    Monstre.argent = 250
    combat()

def KiyuStats():
    Pacifique = False
    Monstre.nom = 'Kiyu'
    Monstre.vie = int(Robot.viemax * 0.60)
    Monstre.attaque = int(Robot.attaque * 0.40)
    Monstre.armure = int(Robot.armure * 0.50)
    Monstre.xpdonne = int(Robot.xp_lvlup * 0.33)
    Monstre.argent = 250
    combat()

def SCP600Stats():
    Pacifique = False
    Monstre.nom = 'SCP-600'
    Monstre.vie = int(Robot.viemax * 0.50)
    Monstre.attaque = int(Robot.attaque * 0.33)
    Monstre.armure = int(Robot.armure * 0.50)
    Monstre.xpdonne = int(Robot.xp_lvlup * 0.25)
    Monstre.argent = 250
    combat()


def CelestabellebethabelleStats():
    Pacifique = False
    Monstre.nom = 'Celestabellebethabelle'
    Monstre.vie = int(Robot.viemax * 0.50)
    Monstre.attaque = int(Robot.attaque * 0.40)
    Monstre.armure = int(Robot.armure * 0.25)
    Monstre.xpdonne = int(Robot.xp_lvlup * 0.66)
    Monstre.argent = 250
    combat()


def BobStats():
    Pacifique = False
    Monstre.nom = 'Bob le chien'
    Monstre.vie = int(Robot.viemax * 0.50)
    Monstre.attaque = int(Robot.attaque * 0.35)
    Monstre.armure = int(Robot.armure * 0.80)
    Monstre.xpdonne = int(Robot.xp_lvlup * 0.66)
    Monstre.argent = 250
    combat()

def DogeStats():
    Pacifique = False
    Monstre.nom = 'Doge'
    Monstre.vie = int(Robot.viemax * 0.75)
    Monstre.attaque = int(Robot.attaque * 0.25)
    Monstre.armure = int(Robot.armure * 0.25)
    Monstre.xpdonne = int(Robot.xp_lvlup * 0.5)
    Monstre.argent = 250
    combat()

def Boss1Stats():
    Pacifique = False
    Monstre.nom = 'Cyberfriend 2020'
    Monstre.vie = int(Robot.viemax)
    Monstre.attaque = int(Robot.attaque * 0.80)
    Monstre.armure = int(Robot.armure)
    Monstre.xpdonne = int(Robot.xp_lvlup * 1.25)
    Monstre.argent = 250
    combat()

def Boss2Stats():
    Pacifique = False
    Monstre.nom = 'Cyberfriend-19'
    Monstre.vie = int(Robot.viemax * 1.25)
    Monstre.attaque = int(Robot.attaque * 0.80)
    Monstre.armure = int(Robot.armure * 0.5)
    Monstre.xpdonne = int(Robot.xp_lvlup * 1.25)
    Monstre.argent = 250
    combat()

def Boss3Stats():
    Pacifique = False
    Monstre.nom = 'Cyberfriend PreAlphaEarly'
    Monstre.vie = int(Robot.viemax * 1.10)
    Monstre.attaque = int(Robot.attaque * 0.80)
    Monstre.armure = int(Robot.armure * 2)
    Monstre.xpdonne = int(Robot.xp_lvlup * 1.25)
    Monstre.argent = 250
    combat()

def BossFinalStats():
    Pacifique = False
    Monstre.nom = 'Cyberfriend 2077'
    Monstre.vie = int(Robot.viemax * 1.5)
    Monstre.attaque = int(Robot.attaque * 0.90)
    Monstre.armure = int(Robot.armure)
    Monstre.xpdonne = int(Robot.xp_lvlup * 2.00)
    Monstre.argent = 250
    combat()

def defense():
    print(Robot.nom, "se prépare à se défendre !")
    if Robot.armure * 1.5 > Monstre.attaque:
        print("Même pas mal, tu n'as reçu aucun dégât ! L'ennemi se heurte face à ta défense de fer")
        Monstre.vie -= Monstre.attaque
        print("Le monstre a perdu", Monstre.attaque, "PV !")
        combat()
    else:
        Robot.vie = Robot.vie - (Monstre.attaque - Robot.armure * 1.5)
        print("Bien encaissé, vous n'avez perdu que ", (Monstre.attaque - Robot.armure * 1.5), "\n",
                  "il vous reste",
                  Robot.vie)


def attaque():
    Coupcritique = randint(1, 100)
    if Coupcritique <= 15:
        print("BAM ! Tu as infligé un coup critique !")
        Monstre.vie = Monstre.vie - Robot.attaque * 1.5
        print(Monstre.nom, "a perdu", Robot.attaque * 1.5, "points de vie\n", "Il lui reste", Monstre.vie,
              "points de vie !\n")

    else:
        Monstre.vie = Monstre.vie - Robot.attaque
        print(Monstre.nom, "a perdu", Robot.attaque, "points de vie\n", "Il lui reste", Monstre.vie,
              "points de vie !\n")


def attaque_monstre():
    print(Monstre.nom, "vous attaque")
    Coupcritique = randint(1, 100)
    if Coupcritique <= 15:
        print("Aïe, ", Monstre.nom, " vient de faire un coup critique !")
        Robot.vie = Robot.vie - Monstre.attaque * 1.5
        print("Tu as perdu", Monstre.attaque * 1.5, "points de vie\n")
        print("Il te reste", Robot.vie, "points de vie !\n")
    else:
        Robot.vie = Robot.vie - Monstre.attaque
        print("Tu as perdu", Monstre.attaque, "points de vie\n", "Il te reste", Robot.vie, "points de vie !\n")


def fuite():
    testfuite = randint(1, 100)
    if testfuite <= 25:
        print("Vous avez réussi à fuir et semer votre ennemi !")
        deplacement()
    else:
        print("Aie, vous n'avez pas réussi à esquiver, l'ennemi vous frappe de plein fouet")
        attaque_monstre()
        if Robot.vie <= 0:
            gameover()
        else:
            combat()

def gameover():
    print("------------------------------------")
    print("          Vous avez perdu...        ")
    print("      Souhaitez-vous réessayer ?    ")
    print("          Oui     /       Non       ")
    print("------------------------------------")

    choix_valide = False
    while not choix_valide:
        choix = input(">")
        if choix.lower() == "oui":
            choix_valide = True
            menu_ecran_titre()
        elif choix.lower() == "non":
            quitter()


def combattermine():
    print("Bravo, vous avez vaincu", Monstre.nom)
    Robot.ennemistues.append(Monstre.nom)
    print(Robot.ennemistues)
    Robot.attaque -= Robot.boostattaque
    Robot.armure -= Robot.boostarmure
    Robot.boostattaque = 0
    Robot.boostarmure = 0
    argent()
    xp()
    deplacement()


def combat():
    print(Robot.nom, ": ", Robot.vie, "/", Robot.viemax, "PV")
    print(Monstre.nom, ": ", Monstre.vie, "PV\n")
    print("------------------------------------")
    print(" 1 : Attaque")
    print(" 2 : Defense")
    print(" 3 : Inventaire")
    print(" 4 : Fuite")
    choix = int(input("> "))

    if choix == 1:
        attaque()
        if Monstre.vie <= 0:
            combattermine()
        else:
            attaque_monstre()
            if Robot.vie <= 0:
                gameover()
            else:
                combat()

    if choix == 2:
        defense()

    if choix == 3:
        inventaire_soin()

    if choix == 4:
        fuite()

    else:
        combat()

def shop():

    print("Vous entrez dans l'échoppe... Votre bourse contient", Inventaire.argent, "Euro-Dollars")
    print("1. Processeur - +10 PV - 200 Euro-Dollars")
    print("2. Carte graphique - Restaure 50% des PV - 200 Euro-Dollars ")
    print("3. Disque dur - ! Amélioration permanente ! Gagne 15 d'Attaque - 200 Euro-Dollars")
    print("4. Barette de ram - +10 attaque  - 200 Euro-Dollars")
    print("5. Huile de moteur - +5 attaque +10 armure - 500 Euro-Dollars ")
    print("6. Sortir")
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1" and Inventaire.argent >= 200:
            print(Inventaire.soin)
            choix_valide = True
            Inventaire.soin.append('processeur')
            Inventaire.processeur += 1
            Inventaire.argent -= 200

            print(Inventaire.soin)
            print("Autre chose ?")
            choix_valide = False
            while not choix_valide:
                choix = input(">")
                if choix.lower() == "oui":
                    choix_valide = True
                    shop()
                elif choix.lower() == "non":
                    choix_valide = True
                    deplacement()



        elif choix.lower() == "2" and Inventaire.argent >= 200:
            print(Inventaire.soin)
            choix_valide = True
            Inventaire.soin.append('carte_graphique')
            Inventaire.carte_graphique = +1
            Inventaire.argent -= 200
            print(Inventaire.soin)
            print("Autre chose ?")
            choix_valide = False
            while not choix_valide:
                choix = input(">")
                if choix.lower() == "oui":
                    choix_valide = True
                    shop()
                elif choix.lower() == "non":
                    choix_valide = True
                    deplacement()


        elif choix.lower() == "3" and Inventaire.argent >= 200:
            choix_valide = True
            Inventaire.argent -= 200
            Robot.attaque += 10
            printlent('Installation du disque dur...\n')
            print("DD installé ! Des anciens fichiers vidéos de leçons d'arts martiaux sont installés\n")
            print("Les leçons étaient intéressantes, vous gagnez 15 d'Attaque !")
            print("Votre attaque est maintenant de ", Robot.attaque, ".")
            print("Autre chose ?")
            choix_valide = False
            while not choix_valide:
                choix = input(">")
                if choix.lower() == "oui":
                    choix_valide = True
                    shop()
                elif choix.lower() == "non":
                    choix_valide = True
                    deplacement()


        elif choix.lower() == "4" and Inventaire.argent >= 200:
            print(Inventaire.soin)
            choix_valide = True
            Inventaire.soin.append('barrette_de_ram')
            Inventaire.argent -= 200
            print(Inventaire.soin)
            print("Autre chose ?")
            choix_valide = False
            while not choix_valide:
                choix = input(">")
                if choix.lower() == "oui":
                    choix_valide = True
                    shop()
                elif choix.lower() == "non":
                    choix_valide = True
                    deplacement()


        elif choix.lower() == "5" and Robot.argent >= 200:
            print(Inventaire.soin)
            choix_valide = True
            Inventaire.soin.append('huile_de_moteur')
            print(Inventaire.soin)
            Inventaire.argent -= 200
            print("Autre chose ?")
            choix_valide = False
            while not choix_valide:
                choix = input(">")
                if choix.lower() == "oui":
                    choix_valide = True
                    shop()
                elif choix.lower() == "non":
                    choix_valide = True
                    deplacement()
        elif choix.lower() == "6":
            print("Tu sors de l'échoppe..")
            deplacement()
        else:
            print("Aie, pas assez... Choisis autre chose, ou reviens avec plus d'argent !")

def aide():
    print("""\

        _   ___ ___  ___ 
       /_\ |_ _|   \| __|
      / _ \ | || |) | _| 
     /_/ \_\___|___/|___|             
                        """)
    print("Bienvenue dans CYBERFRIEND 2077 !")
    print("---------------------------------")
    print("Vous êtes un cyber chien ou chien technologiquement amélioré, votre but sera de retrouver votre maître.")
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

def Ending_pacifique():
    print(Robot.nom, "Après avoir bravé ces paysages inconnus, discuté avec tant de personnes..."), time.sleep(0.3)
    print("Tu as finalement retrouvé ton constructeur...")
    print("Constructeur : Je suis fier de toi", Robot.nom, "tu es ma plus belle création."), time.sleep(1)
    printlent('Tiens, prends ça, il est pour toi.')
    print("\n", Robot.nom, " reçoit un Gelano 1PA 1PM tout neuf !")
    printlent('Heureux, Cyberfriend se repose enfin... \n')
    print("Fin de Cyberfriend 2077. Merci d'avoir joué !"), time.sleep(3)
    credits()


def credits():
    print("""\

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

#_______________________________________________________________________________________________________________________

def dogepnj():
    if 'boss2' in Robot.ennemistues:
        print("Un ange passe")
        boss3()
    else:
        print("Ouaf ouaf !"), time.sleep(0.5)
        clairiere()

def boblechienpnj():
    if 'boss1' in Robot.ennemistues :
        print("Système: Qu'est ce que...")
        boss2()
    else :
        print("Bob le chien vous salue"), time.sleep(0.5)
        clairiere()

def celestabellebethabellepnj():
    if 'boss3' in Robot.ennemistues :
        print("Système: Je distingue une source d'énergie très puissante par ici"), time.sleep(0.2)
        bossfinal()
    else :
        print("L'endroit est vide, l'eau de la cascade scintille"), time.sleep(0.5)
        clairiere()


def SCP600pnj():
    print("Re bonjour à toi mon ami.")
    clairiere()

def michelpnj():
    print("Salut toi ^^"), time.sleep(1)
    clairiere()

def kiyupnj():
    print("Skouizi skouizi"), time.sleep(1)
    clairiere()

def michellepnj():
    print("Michelle: Toujours pas de clopes ?! Bon bah tant pis."), time.sleep(1)
    print("Système: Dans quelle direction voulez-vous aller ?")
    print("1. Clairière\n"
          "2. Vers le boss\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            clairiere()

        elif choix.lower() == "2":
            choix_valide = True
            boss1()

def panneau():
    print("Système: Hmm.. Voici le panneau, mais le nom du lieu est brouillé: \n")
    print(" __________________________________________________________________ "), time.sleep(0.1)
    print("|                   [_Bois de Bouxx lx xoxgne_]                    |"), time.sleep(0.1)
    print("|         __________          ____           ________              |"), time.sleep(0.1)
    print("|        |Nord-Ouest|        |Nord|         |Nord-Est|             |"), time.sleep(0.1)
    print("|         ----------          ----           --------              |"), time.sleep(0.1)
    print("|                                                                  |"), time.sleep(0.1)
    print("|            _____          _________          ___                 |"), time.sleep(0.1)
    print("|           |Ouest|        |Clairière|        |Est|                |"), time.sleep(0.1)
    print("|            -----          ---------          ---                 |"), time.sleep(0.1)
    print("|                                                                  |"), time.sleep(0.1)
    print("|         _________            ___           _______               |"), time.sleep(0.1)
    print("|        |Sud-Ouest|          |Sud|         |Sud-Est|              |"), time.sleep(0.1)
    print("|         ---------            ---           -------               |"), time.sleep(0.1)
    print("|                                                                  |"), time.sleep(0.1)
    print("|__________________________________________________________________|"), time.sleep(0.1)

    deplacement()


def centre():
        print("Système: J'ai détecté une clairière à proximité... j'y détecte également une présence"), time.sleep(0.5)
        print("Système: Voulez-vous y aller ?\n"
              "Oui\n"
              "Non (attention cela va engendrer votre retour en mode sommeil)\n"
              )
        choix_valide = False
        while not choix_valide:
            choix = input(">")

            if choix.lower() == "oui":
                choix_valide = True
                clairierem()

            elif choix.lower() == "non":
                choix_valide = True
                non()

def clairierem():
    print("Système: Vous vous dirigez vers la clairière")
    print("Système: Vous arrivez dans une clairière lumineuse où se situe un panneau avec une carte")
    michel()

def clairiere():
    print("Système: Vous vous dirigez vers la clairière")
    print("Système: Vous arrivez dans une clairière lumineuse où se situe un panneau avec une carte")
    print("Que voulez-vous faire ?\n"
          "1. Allez voir Michel\n"
          "2. Allez voir le panneau\n"
          "3. Se déplacer\n"
          "4. Allez au shop\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Vous allez voir Michel")
            michelpnj()

        elif choix.lower() == "2":
            choix_valide = True
            print("Vous vous dirigez vers le panneau")
            panneau()

        elif choix.lower() == "3":
            choix_valide = True
            print("Vous vous déplacez")
            deplacement()

        elif choix.lower() == "4":
            choix_valide = True
            print("Vous allez au shop")
            shop()

def non():
    print("Système: Attention, je vais vous replonger en mode Sommeil profond")
    time.sleep(0.5)
    quitter()

def micheld2():
    print("J'ai vu des gens super intéressants aux 4 coins du bois, tu devrais leur demander.")
    print("1. Ouaf ouaf\n"
          "2. Merci !\n"
          "3. JAMAIS DE LA VIE OUAF !\n"
          "4. Je vais faire ça ouaf.\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print(Robot.nom,": Ouaf ouaf")
            panneau()

        elif choix.lower() == "2":
            choix_valide = True
            print(Robot.nom,": Merci !")
            panneau()

        elif choix.lower() == "3":
            choix_valide = True
            print(Robot.nom,": JAMAIS DE LA VIE OUAF !")
            gameover()

        elif choix.lower() == "4":
            choix_valide = True
            print(Robot.nom,": Je vais faire ça ouaf.")
            panneau()

def micheld1():
    print("Ah ! Tu as besoin d'aide ?")
    print(" 1. Ouaf Ouaf \n"
          " 2. Je cherche mon constructeur ouaf \n"
          " 3. Je crouaf que je vais me balader dans le bois pour en ouafprendre plus.\n" 
          " 4. Je crouaf que TU VAS LA FERMER DÉJÀ !\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print(Robot.nom,": Ouaf Ouaf")
            micheld2()

        elif choix.lower() == "2":
            choix_valide = True
            print(Robot.nom,": Je cherche mon constructeur ouaf")
            micheld2()

        elif choix.lower() == "3":
            choix_valide = True
            print("Je crouaf que je vais me balader dans le bois pour en ouafprendre plus.")
            micheld2()

        elif choix.lower() == "4":
            choix_valide = True
            print("Je crouaf que TU VAS LA FERMER DÉJÀ !")
            gameover()

def michel():
    print("Système: Je détecte aussi une présence. \n"
          "C'est un homme d'après mes analyses thermiques et biologiques.\n"), time.sleep(1)
    print("Michel : Bonjour vous ! Qu'est-ce que vous êtes ? \n"), time.sleep(0.5)
    print("1. Ouaf ouaf\n"
          "2. Je crouaf que je m'appelle",Robot.nom,"\n"
          "3. Je ne sais pas. ouaf !\n"
          "4. JE SUIS UN CHIEN DE L'ENFER ouaf !\n"
          )

    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            micheld1()

        elif choix.lower() == "2":
            choix_valide = True
            micheld1()

        elif choix.lower() == "3":
            choix_valide = True
            micheld1()

        elif choix.lower() == "4":
            choix_valide = True
            gameover()

def kiyud3():
    print("SKOUIZIIIIIIIIIIIIIIIIIIIIIIIII"), time.sleep(0.2)
    print("1. Ouaf Ouaf\n"
          "2. Skouizi skouizi !\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Système: Je crois que la réponse lui a convenu"), time.sleep(0.5)
            print("Système: Hmm.. un dialogue intéressant, nous n'avons pas appris grand chose mais au moins nous sommes en vie")
            print("Système: Je pense que l'on devrait se déplacer")
            Robot.ennemistues.append('Kiyu')
            deplacement()

        elif choix.lower() == "2":
            choix_valide = True
            printlent('Kiyu n aime pas qu on le copie')
            Robot.ennemistues.append('Kiyu')
            KiyuStats()

def kiyud2():
    print("Kiyu: skouizi..."), time.sleep(0.2)
    print("1. Ouaf Ouaf\n"
          "2. Aide-mouaf, s'il te plaît\n"
          "3. Tu es calmé ouaf ?\n"
          "4. Skouizi... Skouizi ?\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Système: Je crois que la réponse lui a convenu")
            kiyud3()

        elif choix.lower() == "2":
            choix_valide = True
            print("Kiyu s'en fout")
            KiyuStats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "3":
            choix_valide = True
            print("Kiyu s'en fout")
            KiyuStats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "4":
            choix_valide = True
            printlent('Kiyu n aime pas qu on le copie')
            KiyuStats()  # en vrai c'est combat mais tmtc travis


def kiyud1():
    print("Kiyu: SKOUIZI ! SKOUIZI SKOUIZI !"), time.sleep(0.2)
    print("1. Ouaf Ouaf\n"
          "2. Je cherche mon constructeur ouaf\n"
          "3. Je cherche mon chemin ouaf\n"
          "4. Skouizi...?\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Système: Je crois que la réponse lui a convenu")
            kiyud2()

        elif choix.lower() == "2":
            choix_valide = True
            print("Kiyu s'en fout")
            KiyuStats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "3":
            choix_valide = True
            print("Kiyu s'en fout")
            KiyuStats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "4":
            choix_valide = True
            printlent('Kiyu n aime pas qu on le copie')
            KiyuStats()  # en vrai c'est combat mais tmtc travis


def kiyu():
    print("Système: Attention je détecte une présence un peu plus loin sur le chemin.\n"), time.sleep(0.2)
    print("Bizarre, je ne détecte aucune signature thermique mais la présence semble venir de ce rocher\n"), time.sleep(0.2)
    print("(Vous vous approchez doucement du rocher) OH ! Cela viendrait de cette peluche ?\n"), time.sleep(0.2)
    print("(Vous examinez la peluche) C'est une peluche de petit chat tout rond avec une petite fleur sur le tête.\n"), time.sleep(0.2)
    print("L'étiquette sur elle semble indiquer: 'Kiyu - POSSESSION DE PAULOK. \n"), time.sleep(1)
    print("Kiyu: Skouizi skouizi ?"), time.sleep(0.2)
    print("1. Ouaf Ouaf\n"
          "2. T'es qui ouaf ?\n"
          "3. Pourquouaf t'es là ?\n"
          "4. Skouizi skouizi ?\n"
          )

    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Bonne réponse !!")
            kiyud1()

        elif choix.lower() == "2":
            choix_valide = True
            print("Kiyu n'aime pas répondre aux questions")
            KiyuStats()#en vrai c'est combat mais tmtc travis

        elif choix.lower() == "3":
            choix_valide = True
            print("Kiyu n'aime pas répondre aux questions")
            KiyuStats()#en vrai c'est combat mais tmtc travis

        elif choix.lower() == "4":
            choix_valide = True
            printlent('Kiyu n aime pas qu on le copie')
            KiyuStats()#en vrai c'est combat mais tmtc travis


def michelled3():
    print("AH ! J'ai entendu un robot qui te ressemblait, parler de constructeur un peu au Nord d'ici si tu veux...")
    print("1. Ouaf Ouaf\n"
          "2. Merci, je demanderai au robot s'il ouaf une clope, en passant !\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Tu t'fous d'moi ?!")
            Robot.ennemistues.append('Michelle')
            MichelleStats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "2":
            choix_valide = True
            print("Système: Je crois que la réponse lui convient"), time.sleep(0.5)
            print("Système: Ce fût fastidieux, nous n'avons pas appris grand chose mais au moins nous sommes en vie")
            print("Système: Je pense que l'on devrait se déplacer")
            Robot.ennemistues.append('Michelle')
            deplacement()



def michelled2():
    print("Michelle: Tu veux quoi, t'as de ferraille ?")
    print("1. Ouaf Ouaf\n"
          "2. Je cherche mon constructeur ouaf\n"
          "3. D'où tu me traîte de touaf de ferraille déjà ?? "
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Tu t'fous d'moi ?!")
            MichelleStats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "2":
            choix_valide = True
            print("Système: Je crois que la réponse lui convient")
            michelled3()

        elif choix.lower() == "3":
            choix_valide = True
            print("Tu t'fous d'moi ?!")
            MichelleStats()  # en vrai c'est combat mais tmtc travis

def michelled1():
    print("Michelle: Qui ? Moi ? J'm'appelle Michelle, ça fait une paye qu'on m'a pas demandé mon nom, tiens !")
    print("1. Ouaf Ouaf\n"
          "2. J'ai pas de clope ouaf.\n"
          "3. Bonjour Michelle ! Mouaf c'est",Robot.nom,"\n"
          "4. Pourquouaf vous avez la voix grave ? \n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Tu t'fous d'moi ?!")
            MichelleStats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "2":
            choix_valide = True
            print("Alors barre-toi !")
            MichelleStats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "3":
            choix_valide = True
            print("Système: Je crois que la réponse lui convient")
            michelled2()

        elif choix.lower() == "4":
            choix_valide = True
            print("Tu t'fous d'moi ?!")
            MichelleStats()  # en vrai c'est combat mais tmtc travis

def michelle():
    print("Système: Tu sais, je ne crois pas qu'il y ait de bonne ou de mauvaise direc...")
    print("Inconnue: Hé tas de ferraille ! T'aurais pas une clope ?")
    print("1. Ouaf Ouaf\n"
          "2. Vous êtes qui ouaf ?\n"
          "3. Je cherche mon constructeur ouaf\n"
          "4. Aidez-mouaf, s'il vous plaît\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Tu t'fous d'moi ?!")
            MichelleStats() # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "2":
            choix_valide = True
            print("Système: Je crois que la réponse lui convient")
            michelled1()

        elif choix.lower() == "3":
            choix_valide = True
            print("Tu crois que j'en ai quelque chose à f*utre ?!")
            MichelleStats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "4":
            choix_valide = True
            print("Tu crois que j'en ai quelque chose à f*utre ?!")
            MichelleStats()  # en vrai c'est combat mais tmtc travis

def celestabellebethabelled2():
    print("(La corne de la licorne Celestabellebethabelle se met à briller d'un rose vif et à produire de la musique techno franchement pas terrible)\n"
          "Celestabellebethabelled: Tu trouveras tes réponses en allant encore à l'ouest..."
          )
    print("1. Ouaf Ouaf\n"
          "2. Merci !\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Système: Je crois que la réponse lui convient"), time.sleep(0.5)
            print("Système: Ce fût fastidieux, nous n'avons pas appris grand chose mais au moins nous sommes en vie")
            print(
                "Système: Je pense que l'on devrait se déplacer")
            Robot.ennemistues.append('Celestabellebethabelle')
            deplacement()


        elif choix.lower() == "2":
            choix_valide = True
            print("Système: Je crois que la réponse lui convient"), time.sleep(0.5)
            print("Système: Ce fût fastidieux, nous n'avons pas appris grand chose mais au moins nous sommes en vie")
            print(
                "Système: Je pense que l'on devrait se déplacer")
            Robot.ennemistues.append('Celestabellebethabelle')
            deplacement()


def celestabellebethabelled1():
    print("Celestabellebethabelled: Je- euh- hum. Que veux-tu SAVOIIIIIR ? (le mot 'savoir' est aussi formulé avec un hennissement)")
    print("1. Ouaf Ouaf\n"
          "2. Je cherche mon constructeur ouaf\n"
          "3. Je vouaf que ses hennissements arrête, s'il te plaît\n"
          "4. Je vouaf savoir comment tu fais pour autant m'insupporter\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("(Hennissement de rage)")
            CelestabellebethabelleStats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "2":
            choix_valide = True
            print("Système: Je crois que la réponse lui convient")
            celestabellebethabelled2()

        elif choix.lower() == "3":
            choix_valide = True
            print("(Hennissement de rage)")
            CelestabellebethabelleStats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "4":
            choix_valide = True
            print("(Hennissement de rage)")
            CelestabellebethabelleStats()  # en vrai c'est combat mais tmtc travis

def celestabellebethabelle():
    print("Système: En suivant cette rivière en sens inverse, on devrait forcément trouver quelqu'un.. ou quelque chose"), time.sleep(2)
    print("Système: J'entends qu'on se rapproche d'une cascade et.. Wooaah.. Une licorne !\n"
          "Une licorne à la crinière multicolore et aux yeux scintillant, prenant la pose devant une cascade ? Elle laisse paraître un arc-en-ciel en contrechamp \n"
          "C'est magnifique !"
          )
    print("Celestabellebethabelle: (Hennissement vaguement supportable) Je suis Celestabellebethabelle.\n"
          "Je peux répondre à tes questions, mais seulement si tu as le coeur PUUUUUUUUUR (le mot 'pur' est formulé avec un hennissement)")
    print("1. Ouaf Ouaf\n"
          "2. Je n'ai pouaf de coeur, je suis un robot.\n"
          "3. Je suis sûr d'avoir le coeur pur ouaf !\n"
          "4. Je te trouve insupportable\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("(Hennissement de rage)")
            CelestabellebethabelleStats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "2":
            choix_valide = True
            print("Système: Je crois que la réponse lui convient")
            celestabellebethabelled1()

        elif choix.lower() == "3":
            choix_valide = True
            print("(Hennissement de rage)")
            CelestabellebethabelleStats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "4":
            choix_valide = True
            print("(Hennissement de rage)")
            CelestabellebethabelleStats()  # en vrai c'est combat mais tmtc travis

def SCP600d3():
    print("Ton nouveau processeur a l'air d'enfer ! T'es passé aux AMD Ryzen finalement ?")
    print("1. Ouaf Ouaf\n"
          "2. Oui\n"
          "3. Bof\n"
          "4. Non\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Système: ^^")
            Robot.ennemistues.append('SCP-600')
            deplacement()

        elif choix.lower() == "2":
            choix_valide = True
            print("Système: ^^")
            Robot.ennemistues.append('SCP-600')
            deplacement()

        elif choix.lower() == "3":
            choix_valide = True
            print("Système: ^^")
            Robot.ennemistues.append('SCP-600')
            deplacement()

        elif choix.lower() == "4":
            choix_valide = True
            print("Système: ^^")
            Robot.ennemistues.append('SCP-600')
            deplacement()

def SCP600d2():
    print("SCP-600: Ouah ! Génial ! D'ailleurs il fait beau n'est-ce pas ?")
    print("1. Ouaf Ouaf\n"
          "2. Oui\n"
          "3. Bof\n"
          "4. Non\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Système: ^^")
            SCP600d3()

        elif choix.lower() == "2":
            choix_valide = True
            print("Système: ^^")
            SCP600d3()

        elif choix.lower() == "3":
            choix_valide = True
            print("Système: ^^")
            SCP600d3()

        elif choix.lower() == "4":
            choix_valide = True
            print("Système: ^^")
            SCP600d3()


def SCP600d1():
    print("SCP-600: Ca faisait longtemps, ça va depuis ?")
    print("1. Ouaf Ouaf\n"
          "2. Je cherche mon constructeur ouaf\n"
          "3. J'ai perdu la mémouaf en me réveillant tout à l'heure\n"
          "4. Oui\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Système: ...")
            SCP600d2()

        elif choix.lower() == "2":
            choix_valide = True
            print("Système: ...")
            SCP600d2()

        elif choix.lower() == "3":
            choix_valide = True
            print("Système: ...")
            SCP600d2()

        elif choix.lower() == "4":
            choix_valide = True
            print("Système: ...")
            SCP600d2()


def SCP600():
    print("Système: Cela fait maintenant 10 minutes et 37 secondes que nous marchons depuis notre dernière rencontre")
    print("Système: J'espère que nous n'allons pas rencontrer un ennemi.. Tiens ! Je crois que nous connaissons cette personne")
    print(Robot.nom,": Bwoufjour !")
    print("SCP-600: Bonjour !")
    print("1. Ouaf Ouaf\n"
          "2. Gaet- non. George, c'est ça ouaf?\n"
          "3. Comment tu vas ouaf ?\n"
          "4. T'as pouaf changé\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Système: Ca à l'air de lui faire plaisir de nous revoir")
            SCP600d1()

        elif choix.lower() == "2":
            choix_valide = True
            print("Système: Ca à l'air de lui faire plaisir de nous revoir")
            SCP600d1()

        elif choix.lower() == "3":
            choix_valide = True
            print("Système: Ca à l'air de lui faire plaisir de nous revoir")
            SCP600d1()

        elif choix.lower() == "4":
            choix_valide = True
            print("Système: Ca à l'air de lui faire plaisir de nous revoir")
            SCP600d1()

def doged3():
    print("Doge: Ouaf Ouaf")
    print("1. Ouaf Ouaf \n"
          "2. Merci !\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Système: Vous avez l'air de bien pouvoir communiquer")
            Robot.ennemistues.append('Doge')
            deplacement()

        elif choix.lower() == "2":
            choix_valide = True
            print("Système: Vous avez l'air de bien pouvoir communiquer")
            Robot.ennemistues.append('Doge')
            deplacement()


def doged2():
    print("Doge: Ouaf Ouaf")
    print("1. Ouaf Ouaf \n"
          "2. Et ils sont partis par oùaf ?\n"
          "3. Je te crouaf pas.\n"
          "4. BARK BARK\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Système: Vous avez l'air de bien pouvoir communiquer")
            doged3()

        elif choix.lower() == "2":
            choix_valide = True
            print("Système: Vous avez l'air de bien pouvoir communiquer")
            doged3()

        elif choix.lower() == "3":
            choix_valide = True
            print("Doge: Grrrrr!!!")
            DogeStats()

        elif choix.lower() == "4":
            choix_valide = True
            print("Système: Ca à l'air de lui faire plaisir de nous revoir")
            DogeStats()

def doged1():
    print("Doge: Ouaf Ouaf")
    print("1. Ouaf Ouaf \n"
          "2. Touaf aurais pas vu mon constructeur ?\n"
          "3. Doge ? Mais pourquouaf un nom aussi farfelu ?\n"
          "4. BARK BARK\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Système: Vous avez l'air de bien pouvoir communiquer")
            doged2()

        elif choix.lower() == "2":
            choix_valide = True
            print("Système: Vous avez l'air de bien pouvoir communiquer")
            doged2()

        elif choix.lower() == "3":
            choix_valide = True
            print("Doge: Grrrrr!!!")
            DogeStats()

        elif choix.lower() == "4":
            choix_valide = True
            print("Système: Ca à l'air de lui faire plaisir de nous revoir")
            DogeStats()


def doge():
    print("Système: Je détecte une présence en face de nous\n"
          "D'après mes analyses, c'est un chien comme vous mais sans robotique")
    print("Doge: Ouaf Ouaf")
    print("1. Ouaf Ouaf \n"
          "2. Comment tu t'ouafpelle ?\n"
          "3. Touaf aurais pas vu mon constructeur ?\n"
          "4. BARK BARK\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Système: Vous avez l'air de bien pouvoir communiquer")
            doged1()

        elif choix.lower() == "2":
            choix_valide = True
            print("Système: Vous avez l'air de bien pouvoir communiquer")
            doged1()

        elif choix.lower() == "3":
            choix_valide = True
            print("Doge: Grrrrr!!!")
            DogeStats()

        elif choix.lower() == "4":
            choix_valide = True
            print("Doge: Grrrrr!!!")
            DogeStats()

def boblechiend3():
    print("Ah ça ? Un de tes collègues en parlait un peu plus au sud, j'imagine qu'il sait où il est")
    print("1. Ouaf Ouaf\n"
          "2. À plus, Bob !\n"
          )
    
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Bob le chien : À plus !")
            Robot.ennemistues.append('Bob le chien')
            deplacement()

        elif choix.lower() == "2":
            choix_valide = True
            print("Système: ...")
            Robot.ennemistues.append('Bob le chien')
            deplacement()

def boblechiend2():
    print("Bob le chien : Au moins quelqu'un de poli et qui se présente ! T'es nouveau dans le coin ?")
    print("1. Ouaf Ouaf\n"
          "2. Je viens d'arriver et je cherche mon constructeur depouaf tout à l'heure\n"
          "3. Je viens de me réveiller et j'ai une sérieuse envie de démolir touaf le monde\n"
          "4. Peu importe.\n"
          )
    
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Bob le chien : Hé ! T'arrêtes de te payer ma tête !")
            BobStats()

        elif choix.lower() == "2":
            choix_valide = True
            print("Système: ...")
            boblechiend3()

        elif choix.lower() == "3":
            choix_valide = True
            print("Bob le chien : Hé ! T'arrêtes de te payer ma tête !")
            BobStats()

        elif choix.lower() == "4":
            choix_valide = True
            print("Bob le chien : Tant pis pour toi.")
            BobStats()


def boblechiend1():
    print("Bob le chien : Non, sans déconner, je sais parler. Je m'appelle Bob.")
    print("1. Ouaf Ouaf\n"
          "2. Je m'ouafpelle",Robot.nom,"\n"
          "3. Je cherche mon constructeur ouaf\n"
          "4. Ah. Et alors ?\n"
          )
    
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Bob le chien : Hé ! T'arrêtes de te payer ma tête !")
            BobStats()

        elif choix.lower() == "2":
            choix_valide = True
            print("Système: ...")
            boblechiend2()

        elif choix.lower() == "3":
            choix_valide = True
            print("Bob le chien : Je m'en fiche !")
            BobStats()

        elif choix.lower() == "4":
            choix_valide = True
            print("Bob le chien : Hé ! T'arrêtes de te payer ma tête !")
            BobStats()


def boblechien():
    print("Système: Un chien passe devant vous.")
    print("Bob le chien : BARK BARK")
    print("1. Ouaf Ouaf\n"
          "2. Skouizi ?\n"
          "3. BARK BARK BARK\n"
          "4. Je vais te démolir\n"
          )
    
    choix_valide = False
    while not choix_valide:
        choix = input(">")
        
        if choix.lower() == "1":
            choix_valide = True
            print("Système: Ce chien s'est levé sur ses deux pattes !")
            boblechiend1()

        elif choix.lower() == "2":
            choix_valide = True
            print("Système: Ca à l'air de l'avoir énervé...")
            BobStats()

        elif choix.lower() == "3":
            choix_valide = True
            print("Système: Ca à l'air de l'avoir énervé...")
            BobStats()

        elif choix.lower() == "4":
            choix_valide = True
            print("Système: Ca à l'air de l'avoir énervé...")
            BobStats()


def boss1d2():
    print("Cyberfriend 2020: Question numéro trois: Quel est le jeu-vidéo le plus vendu de tous les temps, toutes plateformes confondues ?")
    print("1. Grand Theft Auto V\n"
          "2. Minecraft\n"
          "3. Super Mario Bros\n"
          "4. Cyberpunk 2077\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Cyberfriend 2020: FAUX !")
            Robot.ennemistues.append('boss1')
            Boss1Stats()

        elif choix.lower() == "2":
            choix_valide = True
            print("Cyberfriend 2020: Cyberfriend 2020: Bonne réponse ☐")
            Robot.ennemistues.append('boss1')
            deplacement()

        elif choix.lower() == "3":
            choix_valide = True
            print("Cyberfriend 2020: FAUX une fois !")
            Robot.ennemistues.append('boss1')
            Boss1Stats()

        elif choix.lower() == "4":
            choix_valide = True
            print("")
            Robot.ennemistues.append('boss1')
            Boss1Stats()

def boss1d1():
    print("Cyberfriend 2020: Question Nummer zwei: Qui était le dieu de la guerre dans la mythologie grecque ?")
    print("1. Apollon\n"
          "2. Hermès\n"
          "3. Hadès\n"
          "4. Arès\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Cyberfriend 2020: FAUX !")
            Robot.ennemistues.append('boss1')
            Boss1Stats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "2":
            choix_valide = True
            print("Cyberfriend 2020: FAUX !")
            Robot.ennemistues.append('boss1')
            Boss1Stats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "3":
            choix_valide = True
            print("Cyberfriend 2020: FAUX !")
            Robot.ennemistues.append('boss1')
            Boss1Stats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "4":
            choix_valide = True
            print("Cyberfriend 2020: Bonne réponse.")
            Robot.ennemistues.append('boss1')
            boss1d2()

def boss1():
    print("Système: Mes analyses indiquent un pic d'énergie ici..")
    print("Cyberfriend 2020: HAHAHA, tu recherches quelqu'un peut être ?\n"
          "Pour pouvouaf rencontrer notre constructeur on va vouaf si t'es en l'état... Avec un Quiz de Culture Générale !!\n"
          "T'es censé avouaf les réponses dans ton code alors ça devrait être facile, non ?"), time.sleep(0.5)
    print("Cyberfriend 2020: On va faire simple, 3 questions de débutant, pour vouaf si tu tiens la route.\n"
          "Mes 3 autres collègues s'occuperont de vouaf ton code en profondeur à travers d'autres quiz plus dures.\n"
          "Si tu réponds bien à tous les quiz, tu pourras vouaf le constructeur !")
    print("Système: J'espère que notre mémoire profonde n'a pas été endommagé")
    print(Robot.nom,": Je suis prêt, envoie tes questions !")
    print("Cyberfriend 2020: Question numero uno: Quel pays a remporté la coupe du monde de football en 2018 ?")
    print("1. L'Allemagne\n"
          "2. Le seum\n"
          "3. La France\n"
          "4. Le Brésil\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")
        if choix.lower() == "1":
            choix_valide = True
            print("Cyberfriend 2020: FAUX !")
            Robot.ennemistues.append('boss1')
            Boss1Stats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "2":
            choix_valide = True
            print("Cyberfriend 2020: FAUX une fois !")
            Robot.ennemistues.append('boss1')
            Boss1Stats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "3":
            choix_valide = True
            print("Cyberfriend 2020: Bonne réponse.")
            boss1d1()

        elif choix.lower() == "4":
            choix_valide = True
            print("Cyberfriend 2020: FAUX !")
            Robot.ennemistues.append('boss1')
            Boss1Stats()  # en vrai c'est combat mais tmtc travis

def boss2d2():
    print("Cyberfriend-19: Quelle est la hauteur du Mont Blanc ?")
    print("1. Environ 5108 m\n"
          "2. Environ 3808 m\n"
          "3. Environ 4808 m\n"
          "4. Environ 4208 m\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")
        if choix.lower() == "1":
            choix_valide = True
            print("Cyberfriend-19: FAUX ! *tousse tousse*")
            Robot.ennemistues.append('boss2')
            Boss2Stats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "2":
            choix_valide = True
            print("Cyberfriend-19: FAUX ! *tousse tousse*")
            Robot.ennemistues.append('boss2')
            Boss2Stats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "3":
            choix_valide = True
            print("Cyberfriend-19: Bonne réponse..")
            deplacement()

        elif choix.lower() == "4":
            choix_valide = True
            print("Cyberfriend-19: FAUX !*tousse tousse*")
            Robot.ennemistues.append('boss2')
            Boss2Stats()  # en vrai c'est combat mais tmtc travis

def boss2d1():
    print("Cyberfriend-19: De quelle pièce de Molière Alceste et Célimène sont-ils les protagonistes ?")
    print("1. Le Misanthrope\n"
          "2. Dom Juan\n"
          "3. Le Malade imaginaire\n"
          "4. Les Fourberies de Scapin\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")
        if choix.lower() == "1":
            choix_valide = True
            print("Cyberfriend-19: Bonne réponse..")
            boss2d2()

        elif choix.lower() == "2":
            choix_valide = True
            print("Cyberfriend-19: FAUX ! *tousse tousse*")
            Robot.ennemistues.append('boss2')
            Boss2Stats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "3":
            choix_valide = True
            print("Cyberfriend-19: FAUX ! *tousse tousse*")
            Robot.ennemistues.append('boss2')
            Boss2Stats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "4":
            choix_valide = True
            print("Cyberfriend-19: FAUX !*tousse tousse*")
            Robot.ennemistues.append('boss2')
            Boss2Stats()  # en vrai c'est combat mais tmtc travis

def boss2():
    print("Système: Mes analyses indiquent un pic d'énergie ici, avec quelques.. perturbations")
    print("Cyberfriend-19: *Tousse* *tousse*... Pardonne-mouaf, le constructeur m'a fait faire un stress-test avec un virus et depuis, je suis quelque peu malade... *Tousse* *tousse*\n"
          "Si tu réponds bien à ces questions de niveau intermédiaire, il ne resterouaf que 2 de mes collègues à affronter. Alors, c'est parti ! *Tousse* *tousse*")
    print(Robot.nom,": Ca ira pour moi ! Mais tu veux pas prendre du Lysopaïne avant ?"), time.sleep(1)
    print("Cyberfriend-19: Quelle théorie doit-on à Isaac Newton ?")
    print("1. La théorie de l'évolution des espèces\n"
          "2. La théorie de la gravitation universelle\n"
          "3. La théorie atomique\n"
          "4. La théorie des cordes\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")
        if choix.lower() == "1":
            choix_valide = True
            print("Cyberfriend-19: FAUX !*tousse tousse*")
            Robot.ennemistues.append('boss2')
            Boss2Stats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "2":
            choix_valide = True
            print("Cyberfriend-19: Bonne réponse..")
            boss2d1()

        elif choix.lower() == "3":
            choix_valide = True
            print("Cyberfriend-19: FAUX ! *tousse tousse*")
            Robot.ennemistues.append('boss2')
            Boss2Stats()  # en vrai c'est combat mais tmtc travis

        elif choix.lower() == "4":
            choix_valide = True
            print("Cyberfriend-19: FAUX !*tousse tousse*")
            Robot.ennemistues.append('boss2')
            Boss2Stats()  # en vrai c'est combat mais tmtc travis

def boss3d2():
    print("Question 3 : céléxioné la bone utilizasion du particip passé dan la fraz 'La villa qu'ils ont (réserver) avait une piscine'")
    print("1. réservé\n"
          "2. réservés\n"
          "3. réservée\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")
        if choix.lower() == "1":
            choix_valide = True
            print("Cyberfriend-19: ta ra t o le nul")
            Robot.ennemistues.append('boss3')
            Boss3Stats()

        elif choix.lower() == "2":
            choix_valide = True
            print("Cyberfriend-19: ta ra t o le nul")
            Robot.ennemistues.append('boss3')
            Boss3Stats()

        elif choix.lower() == "3":
            choix_valide = True
            print("Cyberfriend-19: bone répons ta ganié le kwiz")
            Robot.ennemistues.append('boss3')
            deplacement()


def boss3d1():
    print("Question 2 : ke sinifi 'à l'instar de'?")
    print("1. comme\n"
          "2. contrairement à\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")
        if choix.lower() == "1":
            choix_valide = True
            print("Cyberfriend-19: bone répons")
            boss3d2()

        elif choix.lower() == "2":
            choix_valide = True
            print("Cyberfriend-19: ta ra t o le nul")
            Robot.ennemistues.append('boss3')
            Boss3Stats()

def boss3():
    print("Système: Mes analyses indiquent un pic d'énergie ici.. un sacré pic d'énergie, je n'ai jamais vu ça !")
    print("Cyberfriend-19 : oé alor mon kod é pa pré encor mé je vé fer de mon mieu waf\n"
          "g lé kestyon é lé répons du kwiz waf. cé parti du kou waf!\n")

    print("Question 1 : céléxioné la bone dé 4 répons propozé dan la fraz 'ce sont plus souvent les proffessionnels / profesionnels / proffessionels / professionels / professionnels qui en bénéficient'.")
    print("1. proffessionnels\n"
          "2. proffessionels\n"
          "3. professionnels\n"
          "4. professionels\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")
        if choix.lower() == "1":
            choix_valide = True
            print("Cyberfriend-19: ta ra t o le nul")
            Robot.ennemistues.append('boss3')
            Boss3Stats()

        elif choix.lower() == "2":
            choix_valide = True
            print("Cyberfriend-19: ta ra t o le nul")
            Robot.ennemistues.append('boss3')
            Boss3Stats()

        elif choix.lower() == "3":
            choix_valide = True
            print("Cyberfriend-19 : bone répons")
            boss3d1()

        elif choix.lower() == "4":
            choix_valide = True
            print("Cyberfriend-19: ta ra t o le nul")
            Robot.ennemistues.append('boss3')
            Boss3Stats()
def bossfinald3():
    #SI ON EST DANS UNE RUN NORMALE
    if Pacifique == False:
        print("Cyberfriend 2077 : Bravo, bravo, tu ouafs triomphé aux quiz..."), time.sleep(2)
        print("Cependant"), time.sleep(1)
        print("Je vais te détruire"), time.sleep(1)
        print("Je vais te détruire car le constructeur me l'a demandé, il m'a demandé de détruire les Cyberfriends tueurs."), time.sleep(1)
        print("Ou alors il m'a juste demandé de le retrouver puis lui faire résoudre un stupide quiz ?"), time.sleep(3)
        print("..."), time.sleep(1)
        print("... Il m'a reprogrammé après que j'ai détruit les Cyberfriends sur ma route et m'a programmé pour détruire le prochain qui fait comme moi-"), time.sleep(2)
        print("..."), time.sleep(4)
        print("Je vais le tuer. Tu es trop dangereux alors je vais te détruire d'abord puis le tuer ensuite."), time.sleep(2)
        time.sleep(4)
        combat() #<-- OBLIGATOIRE

    #SI ON EST DANS UNE RUN PACIFIST
    else:
        print("Cyberfriend 2077 : T'as été sympa avec tous le monde...\n"
              "Dans ce cas-là le constructeur m'a demandé de me désactiver... Il va venir te chercher. T'en fais pas.")
        #Ending pacifist
        Ending_pacifique()

def bossfinald2():
    print("Combien une entreprise a-t-elle de cibles lors d'une mise en place de stratégie de ciblage ?")
    print("1. 1\n"
          "2. 2\n"
          "3. 3\n"
          "4. 4\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Cyberfriend 2077 : Viens te battre.")
            BossFinalStats()

        elif choix.lower() == "2":
            choix_valide = True
            print("Cyberfriend 2077 : Viens te battre.")
            BossFinalStats()

        elif choix.lower() == "3":
            choix_valide = True
            print("Cyberfriend 2077 : Bonne réponse...")
            bossfinald3()

        elif choix.lower() == "4":
            choix_valide = True
            print("Cyberfriend 2077 : Viens te battre.")
            BossFinalStats()

def bossfinald1():
    print("Qu'est-ce qui se place au coeur d'une stratégie marketing ?")
    print("1. Le produit\n"
          "2. Le logo\n"
          "3. Le service\n"
          "4. Le projet\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Cyberfriend 2077 : Bonne réponse...")
            bossfinald2()

        elif choix.lower() == "2":
            choix_valide = True
            print("Cyberfriend 2077 : Viens te battre.")
            BossFinalStats()

        elif choix.lower() == "2":
            choix_valide = True
            print("Cyberfriend 2077 : Viens te battre.")
            BossFinalStats()

        elif choix.lower() == "2":
            choix_valide = True
            print("Cyberfriend 2077 : Viens te battre.")
            BossFinalStats()


def bossfinal():
    print("Système: ERREUR")
    print("Cyberfriend 2077 : Faisons çouaf vite.\n"
          "Cyberfriend 2077 : 3 questions ouàf propos de la communication des entreprises.\n")

    print("Question 1 : Quel est le plus haut positionnement que peut avoir une entreprise ?")
    print("1. Haut de Gamme\n"
          "2. Icone\n"
          "3. Luxe\n"
          "4. Excelsior\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "1":
            choix_valide = True
            print("Cyberfriend 2077 : Viens te battre.")
            BossFinalStats()

        elif choix.lower() == "2":
            choix_valide = True
            print("Cyberfriend 2077 : Bonne réponse...")
            bossfinald1()

        elif choix.lower() == "3":
            choix_valide = True
            print("Cyberfriend 2077 : Viens te battre.")
            BossFinalStats()

        elif choix.lower() == "4":
            choix_valide = True
            print("Cyberfriend 2077: Viens te battre.")
            BossFinalStats()
#_______________________________________________________________________________________________________________________

def Debut_de_partie():
    Pacifique = True
    reset()
    Robot.nom = input("Entrez votre pseudo : ")
    if Robot.nom == "":
        print("S'agirait de grandir... \n Allez on recommence : ")
        Robot.nom = input("Entrez votre pseudo : ")
    if Robot.nom == "":
        print("Vous êtes PUNIS."), time.sleep(0.5)
        print("Fermeture dans 3..."), time.sleep(1)
        print("Fermeture dans 2..."), time.sleep(1)
        print("Fermeture dans 1..."), time.sleep(1)
        time.sleep(1)
        quit()
    else : 
        print("Hé bien",Robot.nom,", c'est parti !")
        time.sleep(3)
        print(":.....Oh ! Que se passe-t-il ? Où suis-je ?")
        print("Système: Bonjour", Robot.nom, ", votre système vient d'être reboot, vous vous trouvez en plein milieu du Bois de Bourg le Borgne")
        
        centre()


def menu_ecran_titre():
    print('\n'
          '          Bienvenue dans Cyberfriend 2077\n'
          '              1 - Nouvelle partie        \n'
          '              2 - Aide                   \n'
          '              3 - Crédits                \n'
          '              4 - Quitter                \n'
          )
    choix = int(input("> "))
    if choix==1:
        Debut_de_partie()

    elif choix==2:
        aide()

    elif choix==3:
        credits()

    elif choix==4:
        quitter()

#_______________________________________________________________________________________________________________________
#À REVOIR SANS PYGAME !!
def deplacementpnj():
    print("Système: Où voulez vous allez ?\n"), time.sleep(0.5)
    print("Vers le Nord \n"
          "Vers l'Est \n"
          "Vers le Sud \n"
          "Vers l'Ouest \n"
          "Vers le Nord-Ouest\n"
          "Vers le Sud-Est\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "nord":
            choix_valide = True
            nordpnj()

        elif choix.lower() == "est":
            choix_valide = True
            estpnj()

        elif choix.lower() == "sud":
            choix_valide = True
            sudpnj()

        elif choix.lower() == "ouest":
            choix_valide = True
            ouestpnj()

        elif choix.lower() == "nord-ouest":
            choix_valide = True
            nordouestpnj()

        elif choix.lower() == "sud-est":
            choix_valide = True
            sudestpnj()

        elif choix.lower() == "nord-est":
            choix_valide = True
            nordestpnj()

        elif choix.lower() == "sud-ouest":
            choix_valide = True
            sudouestpnj()

        else:
            print("Tu dois écrire une direction si tu veux avancer dans l'aventure (ex: nord)")


def nordpnj():
    print("Vous vous dirigez vers le Nord")
    michellepnj()


def estpnj():
    print("Vous vous dirigez vers le Est")
    dogepnj()

def sudpnj():
    print("Vous vous dirigez vers le Sud")
    boblechienpnj()

def ouestpnj():
    print("Vous vous dirigez vers le Ouest")
    celestabellebethabellepnj()

def nordouestpnj():
    print("Vous vous dirigez vers le Nord-Ouest")
    kiyupnj()

def sudestpnj():
    print("Vous vous dirigez vers le Sud-Est")
    SCP600pnj()

def nordestpnj():
    print("Une grand falaise se creuse par ici, impossible d'y aller.")
    panneau()

def sudouestpnj():
    print("Il n'y a que des arbres et de la verdure dense remplie de ronces.")
    panneau()


def deplacement():
    print("Système: Où voulez vous allez ?\n"), time.sleep(0.5)
    print("Vers le Nord \n"
          "Vers l'Est \n"
          "Vers le Sud \n"
          "Vers l'Ouest \n"
          "Vers le Nord-Ouest\n"
          "Vers le Sud-Est\n"
          "Vers la clairière\n"
          )
    choix_valide = False
    while not choix_valide:
        choix = input(">")

        if choix.lower() == "nord":
            choix_valide = True
            nord()

        elif choix.lower() == "est":
            choix_valide = True
            est()

        elif choix.lower() == "sud":
            choix_valide = True
            sud()

        elif choix.lower() == "ouest":
            choix_valide = True
            ouest()

        elif choix.lower() == "nord-ouest":
            choix_valide = True
            nordouest()

        elif choix.lower() == "sud-est":
            choix_valide = True
            sudest()

        elif choix.lower() == "nord-est":
             choix_valide = True
             nordest()

        elif choix.lower() == "sud-ouest":
             choix_valide = True
             sudouest()

        elif choix.lower() == "clairiere":
             choix_valide = True
             clairiere()

        else:
            print("Tu dois écrire une direction si tu veux avancer dans l'aventure (ex: nord)")

def nord():
    print("Vous vous dirigez vers le Nord")
    if 'Michelle' in Robot.ennemistues :
        michellepnj()
    else :
        michelle()

def est():
    print("Vous vous dirigez vers le Est")
    if 'Doge' in Robot.ennemistues :
        dogepnj()
    else :
        doge()

def sud():
    if 'Bob le chien' in Robot.ennemistues :
        boblechienpnj()
    else :
        boblechien()

def ouest():
    print("Vous vous dirigez vers le Ouest")
    if 'Celestabellebethabelle' in Robot.ennemistues :
        celestabellebethabellepnj()
    else :
        celestabellebethabelle()

def nordouest():
    print("Vous vous dirigez vers le Nord-Ouest")
    if 'Kiyu' in Robot.ennemistues :
        kiyupnj()
    else :
        kiyu()

def sudest():
    print("Vous vous dirigez vers le Sud-Est")
    if 'SCP-600' in Robot.ennemistues :
        SCP600pnj()
    else :
        SCP600()

def nordest():
    print("Une grand falaise se creuse par ici, impossible d'y aller.")
    panneau()

def sudouest():
    print("Il n'y a que des arbres et de la verdure dense remplie de ronces.")
    panneau()
#_______________________________________________________________________________________________________________________


def inventaire_soin():
    print("\n")
    if Inventaire.processeur >= 1:
        print(Inventaire.soin.index('processeur') + 1, " : Processeur = +10 PV ( x", Inventaire.processeur, ")")

    if Inventaire.carte_graphique >= 1:
        print(Inventaire.soin.index('carte_graphique') + 1, " : Carte graphique = +20 PV ( x",
              Inventaire.carte_graphique, ")")

    if Inventaire.barrette_de_ram >= 1:
        print(Inventaire.soin.index('barrette_de_ram') + 1, " : Barrette de ram = +15 d'Attaque ( x",
              Inventaire.barrette_de_ram, ")")

    if Inventaire.huile_de_moteur >= 1:
        print(Inventaire.soin.index('huile_de_moteur') + 1, " : Huile de moteur = +5 d'Attaque +10 d'Armure ( x",
              Inventaire.huile_de_moteur, ")")

    if Inventaire.processeur == 0 and Inventaire.carte_graphique == 0 and Inventaire.barrette_de_ram == 0 and Inventaire.huile_de_moteur == 0:
        print("exit")
    print(Inventaire.soin.index('exit') + 1, " : exit")
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

    if Inventaire.barrette_de_ram >= 1:
        if choix == Inventaire.soin.index('barrette_de_ram') + 1:
            Inventaire.barrette_de_ram = Inventaire.barrette_de_ram - 1
            Robot.attaque += 15
            Robot.boostattaque += 15
            print("Tu as gagné 15 d'Attaque !")
            if Inventaire.barrette_de_ram == 0:
                Inventaire.soin.remove('barrette_de_ram')
        return

    if Inventaire.huile_de_moteur >= 1:
        if choix == Inventaire.soin.index('huile_de_moteur') + 1:
            Inventaire.huile_de_moteur = Inventaire.huile_de_moteur - 1
            Robot.attaque += 5
            Robot.boostattaque += 5
            Robot.armure += 10
            Robot.boostarmure += 10
            print("Tu as gagné 5 d'Attaque et 10 d'Armure ")
            if Inventaire.huile_de_moteur == 0:
                Inventaire.soin.remove('huile_de_moteur')
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