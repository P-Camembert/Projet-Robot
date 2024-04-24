#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



ev3=EV3Brick()
left_motor=Motor(Port.A)
right_motor=Motor(Port.D)
light=ColorSensor(Port.S4)
gyro=GyroSensor(Port.S3)
sonic=UltrasonicSensor(Port.S1)
infra=InfraredSensor(Port.S2)

#Création du robot et de variables
        # Gaffeur orange, couleur détectée RED
        # Gaffeur noir, couleur détectée BLACK
        # Matela, couleur détectée BROWN
robot=DriveBase(left_motor,right_motor,wheel_diameter=30,axle_track=175)
correction= 30
speed=80

# Définition de la Classe robot

class Robot:
    def __init__(self,left_motor,right_motor,wheel_diameter,axle_track):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.wheel_diameter = wheel_diameter
        self.axle_track = axle_track

    """
    Définition de fonctions pour faire des actions basiques
    """
    # Renvoie un int random avec LCG (Pas sûr de pouvoir utiliser la bibliothèque random)
    def random(n):
        # Paramètres du LCG (Linear Congruential Generator)
        a = 1664525
        c = 1013904223
        m = 2**32
        # Initialisation de la seed (vous pouvez choisir n'importe quelle valeur initiale)
        seed = 1

        # Calcul de la nouvelle seed
        seed = (a*seed+c) % m

        # Calcul et renvoie du nombre pseudo-aléatoire entre 1 et n
        return (seed % n) + 1


    # Lecture de fichier et création d'objet utilisable pour les algorithmes suivants
    def lire_Chemin(fichier_chemin):
        with open(fichier_chemin, 'r') as f:
            chemin = f.readline().strip().split() 
        return chemin # Renvoie une liste depuis ['n','n','n','n','n','n','n'] en n n n n n et ['nnnnnn'] en nnnnnn

    def lire_Matrice_Orientation(fichier_matrice_orientation):
        with open(fichier_matrice_orientation, 'r') as f:
            lignes = f.readlines()
        return [ligne.strip().split() for ligne in lignes] 

    def construire_Matrice_Orientation(graphe):
        orientations = {'N': "N", 'S': "S", 'E': "E", 'O': "O", "X": 'X'}
        matrice_orientation = []
        for ligne in graphe:
            ligne_orientation = [orientations[sommet] for sommet in ligne]
            matrice_orientation.append(ligne_orientation)
        return matrice_orientation
    
    def matrice_Orientation(fichier_matrice_orientation):
        return Robot.construire_Matrice_Orientation(Robot.lire_Matrice_Orientation(fichier_matrice_orientation))
    # Renvoie avec Orientation.txt
    # matrice_orientation =
    # [['X', 'O', 'E', 'X', 'X', 'X'],
    # ['N', 'X', 'E', 'O', 'S', 'X'],
    # ['N', 'O', 'X', 'X', 'S', 'E'],
    # ['X', 'N', 'X', 'X', 'E', 'X'],
    # ['X', 'N', 'E', 'O', 'X', 'S'],
    # ['X', 'X', 'N', 'X', 'S', 'X']]
    
    
    # ENSEMBLE DES FONCTIONS DE LA MATRICE ADJACENTE :
    def lire_Fichier_Graphe(nom_fichier):
        arretes = []
        with open(nom_fichier, 'r') as fichier:
            nombre_sommets = int(fichier.readline().strip())  # Lite le nombre de sommets depuis la première ligne
            for ligne in fichier:
                sommet_depart, sommet_arrivee = map(int, ligne.split())  
                arretes.append((sommet_depart, sommet_arrivee))
        return arretes, nombre_sommets

    def construire_Matrice_Adjacence(arretes, nombre_sommets):
        matrice_adjacence = [[0] * nombre_sommets for _ in range(nombre_sommets)]  # Initialisation de la matrice

        for sommet_depart, sommet_arrivee in arretes:  # Attribution de la valeur 1 pour les arretes existantes dans la matrice
            if sommet_depart <= nombre_sommets and sommet_arrivee <= nombre_sommets:
                matrice_adjacence[sommet_depart-1][sommet_arrivee-1] = 1
                matrice_adjacence[sommet_arrivee-1][sommet_depart-1] = 1
        return matrice_adjacence

    def matrice_Adjacence_Vers_Graphe(matrice_adjacence):
        graphe = {}
        for sommet, voisins in enumerate(matrice_adjacence):
            sommet += 1  # Ajuste l'indice pour commencer à 1
            graphe[sommet] = [voisin + 1 for voisin, valeur in enumerate(voisins) if valeur == 1]
        return graphe
    

        # ENSEMBLE DES FONCTIONS DE FLEURY :
    def fleury(fichier_graph, start_vertex=None): # Doit prendre en entrée le nom du fichier avec le circuit ex: graphe_ciruit
        arretes, nombre_sommets = Robot.lire_Fichier_Graphe(fichier_graph)
        matrice_adjacence = Robot.construire_Matrice_Adjacence(arretes, nombre_sommets)
        graphe = Robot.matrice_Adjacence_Vers_Graphe(matrice_adjacence)

        # Vérifie si le graphe est eulérien en vérifiant que chaque sommet a un degré pair
        for vertex in graphe:
            if len(graphe[vertex]) % 2 != 0:
                raise ValueError("Le graphe n'est pas eulérien")

        def is_bridge(u, v):
            # Retire temporairement l'arête entre u et v
            graphe[u].remove(v)
            graphe[v].remove(u)

            # Vérifie si v est toujours accessible depuis u
            visited = {vertex: False for vertex in graphe}
            dfs(u, visited)

            # Ajoute l'arête retirée pour restaurer le graphe
            graphe[u].append(v)
            graphe[v].append(u)

            # Si v est inaccessible depuis u, alors (u, v) est un pont
            return not visited[v]

        def dfs(u, visited):
            visited[u] = True
            for v in graphe[u]:
                if not visited[v]:
                    dfs(v, visited)

        # Initialise la chaîne C
        chain = [start_vertex]

        # Choisi le sommet de départ
        if start_vertex is None:
            # Si aucun sommet n'est spécifié, choisi arbitrairement un sommet
            start_vertex = next(iter(graphe))

        # Parcours le graphe
        current_vertex = start_vertex
        while any(graphe.values()):
            # Trouve un successeur qui n'est pas un pont
            next_vertex = None
            for neighbor in graphe[current_vertex]:
                if not is_bridge(current_vertex, neighbor):
                    next_vertex = neighbor
                    break
            
            # Si aucun successeur non-pont n'est trouvé, choisi arbitrairement un successeur
            if next_vertex is None:
                next_vertex = graphe[current_vertex][0]

            # Ajoute le successeur à la fin de la chaîne C
            chain.append(next_vertex)

            # Supprime l'arête (x, y) du graphe
            graphe[current_vertex].remove(next_vertex)
            graphe[next_vertex].remove(current_vertex)

            # Choisi le prochain sommet
            current_vertex = next_vertex
        
        return chain


    # Commandes de base du robot
    def avance_Distance_n(n):
        robot.straight(n)
    
    def avance_Rouge():
        i=0
        while light.color()!=Color.RED:
            if i<2:
                robot.straight(60)
                i+=1
            else:
                Robot.arret()
                robot.turn(10)
                if light.color()!=Color.RED:
                    robot.turn(-20)
            
    def test_Si_Rouge():
        while light.color()!=Color.RED:
            Robot.arret()
            robot.turn(10)
            if light.color()!=Color.RED:
                robot.turn(-20)

    def tourne_Gyro_Gauche(angle):
        angle = -abs(angle)
        robot.turn(angle)

    def tourne_Gyro_Droite(angle):
        angle = abs(angle)
        robot.turn(angle)

    def tourne_Droite():
        robot.turn(25)
        while light.color() != Color.RED:
            robot.turn(15)
            
    def tourne_Gauche():
        robot.turn(-35)
        while light.color() != Color.RED:
            robot.turn(-15)
            
    def tourner_90(n):
        robot.turn(n*90)
    
    def tourner_N(n):
        robot.turn(n)     
        
    def arret():
        robot.straight(10)
        robot.stop()
        left_motor.brake()
        right_motor.brake()
        left_motor.hold()
        right_motor.hold()
        wait(1000)
        
    def beepBoop():
        ev3.speaker.beep()
        
    def affiche_Ecran(element, texte_explicatif=None):
        if texte_explicatif is not None:
            ev3.screen.print("{} : {}".format(texte_explicatif, element))
        else:
            ev3.screen.print("{}".format(element))
        
    ##################################################
    # Niveau 2 : suivre une route d'un carrefour i à j
    ##################################################
    
    def suivre_Ligne():
        while light.color() != Color.BLACK: # Détecte si le gaffeur est noir
            if light.color() == Color.RED: 
                robot.drive(speed,correction) # Si la couleur détectée est rouge, alors le robot avance et tourne vers la droite
            else:
                robot.drive(speed,-correction) # Sinon il avance et tourne vers la gauche

    def niv_2_Carrefours(fichier_trajet, fichier_matrice_orientation):
        carrefours = Robot.lire_Chemin(fichier_trajet)
        matrice_orientation = Robot.construire_Matrice_Orientation(Robot.lire_Matrice_Orientation(fichier_matrice_orientation))
        angle = 0
        gyro.reset_angle(0)
        orientation = matrice_orientation[int(carrefours[0])-1][int(carrefours[1])-1]
        
        # Modifie la direction en valeur d'angle à l'aide du graphique de la matrice orientation        
        if orientation == 'N':
            angle = 0
        elif orientation == 'S':
            angle = 180
        elif orientation == 'E':
            angle = 90 
        elif orientation == 'O':
            angle = 270
        else :
            return 0
        print(angle)
        # Détermine la direction à prendre pour parcourir l'arête (i,j)
        if gyro.angle() <= angle :
            Robot.tourne_Gyro_Droite(angle-gyro.angle())
            Robot.suivre_Ligne()
        else: 
            Robot.tourne_Gyro_Gauche(gyro.angle()-angle)
            Robot.suivre_Ligne()

    ########################################################################
    # Niveau 3 : 1 code fait à la main, 1 code qui lit les commandes : C,D,G
    ########################################################################
    
    def niv_3_Implementation_Manuelle():
        Robot.suivre_Ligne()  
        Robot.arret() # Arrive 3
        Robot.avance_Distance_n(100)
        Robot.tourne_Gauche()
        Robot.suivre_Ligne()
        Robot.arret() # Arrive 6
        Robot.avance_Distance_n(70)
        Robot.suivre_Ligne()
        Robot.arret()# Arrive 5
        Robot.tourne_Droite()
        Robot.suivre_Ligne()
        Robot.arret() # Arrive 3
        Robot.tourne_Gauche()
        Robot.suivre_Ligne()
        Robot.arret() # Arrive 2
        Robot.beepBoop()

    def niv_3_DCG(txt):
        # Lis le fichier en entrée
        with open(txt, 'r') as f:
            ligne = f.readlines()
            print(ligne)
        
        # Détermine le parcours à partir du fichier
        for e in ligne[0]:
            if e == "G" : # Déplacement à gauche
                Robot.avance_Distance_n(50)
                Robot.tourne_Gauche()
            elif e == "C" : # Déplacement tout droit
                Robot.avance_Rouge()
            elif e == "D" : # Déplacement à droite
                Robot.avance_Distance_n(50)
                Robot.tourne_Droite()
            Robot.suivre_Ligne()
            Robot.arret()
        Robot.beepBoop()

    ####################################################
    # Niveau 4 : 2 Codes : avec gyroscope et une matrice
    ####################################################
    
    # Utilise le gyroscope
    def niv_4_Gyro(fichier_chemin, fichier_matrice_orientation):
        chemin = Robot.lire_Chemin(fichier_chemin)        
        matrice_orientation = Robot.matrice_Orientation(fichier_matrice_orientation)
        liste_angles = []
        gyro.reset_angle(0)
        
        # Créer une liste des angles où le robot doit s'orienter à partir de la matrice orientation
        for i in range(len(chemin) - 1):
            carrefour_actuel = int(chemin[i])
            prochain_carrefour = int(chemin[i + 1])
            orientation = matrice_orientation[carrefour_actuel - 1][prochain_carrefour - 1]
            if orientation == 'N':
                liste_angles.append(0)
            elif orientation == 'S':
                liste_angles.append(180)
            elif orientation == 'E':
                liste_angles.append(90) 
            elif orientation == 'O':
                liste_angles.append(270)
            else :
                break   
        print(liste_angles)
        # Passe la première étape de la liste d'action (Départ)
        if gyro.angle() <= liste_angles[0] :
            Robot.tourne_Gyro_Droite(liste_angles[0]-gyro.angle())
        else : 
            Robot.tourne_Gyro_Gauche(gyro.angle()-liste_angles[0])
            
        # Lit les angles dans la liste et compare avec l'angle mesuré : Si l'angle est inférieur -> tourne à gauche sinon à droite
        for i in range(1,len(liste_angles)):
            Robot.suivre_Ligne()
            Robot.arret()
            Robot.avance_Distance_n(120)
            Robot.affiche_Ecran(gyro.angle())
            if gyro.angle() <= liste_angles[i] :
                Robot.tourne_Gyro_Droite(liste_angles[i]-gyro.angle())
                Robot.affiche_Ecran(gyro.angle())
            else : Robot.tourne_Gyro_Gauche(gyro.angle()-liste_angles[i])
            Robot.affiche_Ecran(gyro.angle())
            Robot.test_Si_Rouge()
        Robot.suivre_Ligne()
        Robot.arret()
        Robot.avance_Distance_n(120)
        Robot.tourner_N(0-gyro.angle())
        Robot.beepBoop()
        
    def niv_4_Gyro_Sans_Lire_Chemin(fichier_chemin, fichier_matrice_orientation):
        chemin = fichier_chemin        
        matrice_orientation = Robot.matrice_Orientation(fichier_matrice_orientation)
        liste_angles = []
        gyro.reset_angle(0)
        
        # Créer une liste des angles où le robot doit s'orienter à partir de la matrice orientation
        for i in range(len(chemin) - 1):
            carrefour_actuel = int(chemin[i])
            prochain_carrefour = int(chemin[i + 1])
            orientation = matrice_orientation[carrefour_actuel - 1][prochain_carrefour - 1]
            if orientation == 'N':
                liste_angles.append(0)
            elif orientation == 'S':
                liste_angles.append(180)
            elif orientation == 'E':
                liste_angles.append(90) 
            elif orientation == 'O':
                liste_angles.append(270)
            else :
                break   

        # Passe la première étape de la liste d'action (Départ)
        if gyro.angle() <= liste_angles[0] :
            Robot.tourne_Gyro_Droite(liste_angles[0]-gyro.angle())
        else : 
            Robot.tourne_Gyro_Gauche(gyro.angle()-liste_angles[0])
            
        # Lit les angles dans la liste et compare avec l'angle mesuré : Si l'angle est inférieur -> tourne à gauche sinon à droite
        for i in range(1,len(liste_angles)):
            Robot.suivre_Ligne()
            Robot.arret()
            Robot.avance_Distance_n(120) 
            if gyro.angle() <= liste_angles[i] :
                Robot.tourne_Gyro_Droite(liste_angles[i]-gyro.angle()) 
            else : Robot.tourne_Gyro_Gauche(gyro.angle()-liste_angles[i])
            Robot.test_Si_Rouge()
        Robot.suivre_Ligne()
        Robot.arret()
        Robot.avance_Distance_n(120)
        Robot.tourner_N(0-gyro.angle())
        Robot.beepBoop()

    # Fonction qui créer une matrice pour déterminer quelle action faire selon le carrefour d'où le robot vient, celui où il est,
    # et où il va
    def matrice(orientation):
        matrice=[[[None for i in range (len(orientation)) ] for i in range (len(orientation))] for i in range(len(orientation))]
        for i in range(len(orientation)):
            N=None
            S=None
            E=None
            O=None
            for j in range(len(orientation[0])):
                if orientation[i][j]=='N':
                    N=j
                elif orientation[i][j]=='S':
                    S=j
                elif orientation[i][j]=='E':
                    E=j
                elif orientation[i][j]=='O':
                    O=j
            if N!=None and S!=None:     #NS=C   EO=C
                matrice[i][N][S]='C'
                matrice[i][S][N]='C'
            if E!=None and O!=None:
                matrice[i][E][O]='C'
                matrice[i][O][E]='C'
            if N!=None and O!=None:     #NO=D   NE=G
                matrice[i][N][O]='D'
                matrice[i][O][N]='G'
            if N!=None and E!=None:
                matrice[i][N][E]='G'
                matrice[i][E][N]='D'
            if O!=None and S!=None:     #SO=G   ES=G
                matrice[i][O][S]='D'
                matrice[i][S][O]='G'                           
            if E!=None and S!=None:
                matrice[i][E][S]='G'
                matrice[i][S][E]='D'
        return matrice #sort une matrice du genre M2
    
    """ Implémentation à la main de la matrice créée avec la fonction matrice, pour le circuit actuel
M2=[
 [[ None , None , None , None , None , None ], 
  [ None , None , 'C'  , None , None , None ], 
  [ None , 'C'  , None , None , None , None ], 
  [ None , None , None , None , None , None ], 
  [ None , None , None , None , None , None ], 
  [ None , None , None , None , None , None ]], 
 
 [[ None , None , 'G'  , 'D'  , 'C'  , None ], 
  [ None , None , None , None , None , None ], 
  [ 'D'  , None , None , 'C'  , 'G'  , None ], 
  [ 'G'  , None , 'C'  , None , 'D'  , None ], 
  [ 'C'  , None , 'D'  , 'G'  , None , None ], 
  [ None , None , None , None , None , None ]],
 
 [[ None , 'D'  , None , None , 'C'  , 'G'  ], 
  [ 'G'  , None , None , None , 'D'  , 'C'  ], 
  [ None , None , None , None , None , None ], 
  [ None , None , None , None , None , None ], 
  [ 'C'  , 'G'  , None , None , None , 'D'  ], 
  [ 'D'  , 'C'  , None , None , 'G'  , None ]],
 
 [[ None , None , None , None , None , None ], 
  [ None , None , None , None , 'G'  , None ], 
  [ None , None , None , None , None , None ], 
  [ None , None , None , None , None , None ], 
  [ None , 'D'  , None , None , None , None ], 
  [ None , None , None , None , None , None ]],
 
 [[ None , None , None , None , None , None ], 
  [ None , None , 'G'  , 'D'  , None , 'C'  ], 
  [ None , 'D'  , None , 'C'  , None , 'G'  ], 
  [ None , 'G'  , 'C'  , None , None , 'D'  ],
  [ None , None , None , None , None , None ],
  [ None , 'C'  , 'D'  , 'G'  , None , None ]],
 
 [[ None , None , None , None , None , None ], 
  [ None , None , None , None , None , None ],
  [ None , None , None , None , 'C'  , None ],
  [ None , None , None , None , None , None ],
  [ None , None , 'C'  , None , None , None ], 
  [ None , None , None , None , None , None ]]]
"""

    # Fonction qui selon le graphe créé avec la fonction matrice, et le chemin, va faire suivre le chemin au robot sans gyroscope
    def niv_4_Matrice(fichier_chemin ,fichier_matrice_orientation): 
        graphe=Robot.lire_Chemin(fichier_chemin)
        M=Robot.matrice(Robot.matrice_Orientation(fichier_matrice_orientation))
        
        Robot.suivre_Ligne()
        Robot.arret()
        for i in range(1,len(graphe)-1):
            e=M[int(graphe[i])-1][int(graphe[i-1])-1][int(graphe[i+1])-1]
            if e == "G" : # Déplacement à gauche
                Robot.avance_Distance_n(60)
                Robot.tourne_Gauche()
            elif e == "C" : # Déplacement tout droit
                Robot.avance_Rouge()
            elif e == "D" : # Déplacement à droite
                Robot.avance_Distance_n(50)
                Robot.tourne_Droite()
            Robot.suivre_Ligne()
            Robot.arret()
        Robot.beepBoop()
        
    def niv_4_Matrice_Sans_Lire_Chemin(fichier_chemin ,fichier_matrice_orientation): 
        graphe=fichier_chemin
        M=Robot.matrice(Robot.matrice_Orientation(fichier_matrice_orientation))
        
        Robot.suivre_Ligne()
        Robot.arret()
        for i in range(1,len(graphe)-1):
            e=M[int(graphe[i])-1][int(graphe[i-1])-1][int(graphe[i+1])-1]
            if e == "G" : # Déplacement à gauche
                Robot.avance_Distance_n(60)
                Robot.tourne_Gauche()
            elif e == "C" : # Déplacement tout droit
                Robot.avance_Rouge()
            elif e == "D" : # Déplacement à droite
                Robot.avance_Distance_n(50)
                Robot.tourne_Droite()
            Robot.suivre_Ligne()
            Robot.arret()
        Robot.beepBoop()
    
    ##########################################################
    # Niveau 5 : 2 Codes, à partir des algorithmes du niveau 4
    ##########################################################
        
    def niv_5_Gyro(fichier_matrice_orientation, graphe_Circuit):   
        sommet = Robot.bonus_touchSelection()
        fichier_chemin = Robot.fleury(graphe_Circuit, sommet)
        Robot.niv_4_Gyro_Sans_Lire_Chemin(fichier_chemin, fichier_matrice_orientation)
            
    def niv_5_Matrice(fichier_matrice_orientation, graphe_Circuit):
        sommet = Robot.bonus_touchSelection()
        fichier_chemin = Robot.fleury(graphe_Circuit, sommet)
        Robot.affiche_Ecran(fichier_chemin[1])
        wait(5000)
        Robot.niv_4_Matrice_Sans_Lire_Chemin(fichier_chemin, fichier_matrice_orientation)
        
    ##############
    # Niveau Bonus
    ##############

    def suivre_Ligne_Obstacle():
        distance=150
        while light.color() != Color.BLACK: # Détecte si le gaffeur est noir
            if light.color() == Color.RED: # Si la couleur est rouge, alors le robot avance et tourne vers la droite si pas d'obstacle
                if sonic.distance() >= distance:
                    robot.drive(speed,correction)
                else :
                    Robot.arret()
                    Robot.beepBoop()
                    while sonic.distance() <= distance:
                        wait(1000)
            else: # Sinon il avance et tourne vers la gauche si pas d'obstacle
                if sonic.distance() >= distance:
                    robot.drive(speed,-correction)
                else :
                    Robot.arret()
                    Robot.beepBoop()
                    while sonic.distance() <= distance:
                        wait(1000)

    def niv_4_Gyro_Obstacle(fichier_chemin, fichier_matrice_orientation):
        chemin = Robot.lire_Chemin(fichier_chemin)
        matrice_orientation = Robot.construire_Matrice_Orientation(Robot.lire_Matrice_Orientation(fichier_matrice_orientation))
        liste_angles = []
        gyro.reset_angle(0)
        
        # Créer une liste des angles où le robot doit s'orienter à partir de la matrice orientation
        for i in range(len(chemin) - 1):
            carrefour_actuel = int(chemin[i])
            prochain_carrefour = int(chemin[i + 1])
            orientation = matrice_orientation[carrefour_actuel - 1][prochain_carrefour - 1]
            if orientation == 'N':
                liste_angles.append(0)
            elif orientation == 'S':
                liste_angles.append(180)
            elif orientation == 'E':
                liste_angles.append(90) 
            elif orientation == 'O':
                liste_angles.append(270)
            else :
                break
        Robot.beepBoop()
            
        # Passe la première étape de la liste d'action (Départ)
        if gyro.angle() <= liste_angles[0] :
            Robot.tourne_Gyro_Droite(liste_angles[0]-gyro.angle())
        else : 
            Robot.tourne_Gyro_Gauche(gyro.angle()-liste_angles[0])
        Robot.beepBoop()   
        # Lit les angles dans la liste et compare avec l'angle mesuré : Si l'angle est inférieur -> tourne à gauche sinon à droite
        for i in range(1,len(liste_angles)):
            Robot.suivre_Ligne_Obstacle()
            Robot.arret()
            Robot.avance_Distance_n(120) 
            if gyro.angle() <= liste_angles[i] :
                Robot.tourne_Gyro_Droite(liste_angles[i]-gyro.angle()) 
            else :
                Robot.tourne_Gyro_Gauche(gyro.angle()-liste_angles[i])
            Robot.test_Si_Rouge()
        Robot.suivre_Ligne_Obstacle()
        Robot.arret()
        Robot.avance_Distance_n(120)
        Robot.tourner_N(0-gyro.angle())
        Robot.beepBoop()
        

        # Bonus du niveau 2 sur la sélection du sommet à l'aide des touches de la brique ev3
    def bonus_touchSelection():
        """
        with open(graphe_Circuit, 'r') as fichier:
            nombre_sommets = int(fichier.readline().strip())  # Lire le nombre de sommets depuis la première ligne
        """
        sommet = 1 # Initialisation du sommet de départ
        maximum_sommet = 6 # Doit être initialiser avec le dernier sommet du graphe

        run = True # variable qui permet d'entrer dans la boucle de sélection du sommet
        Robot.affiche_Ecran(sommet)
        while run: # Boucle de sélection du sommet
            #liste = ev3.buttons.pressed()
            if infra.buttons(2)== [Button.LEFT_UP] : # incrémente le sommet  #Button.UP  in liste 
                ev3.screen.clear()
                wait(400)
                sommet = sommet + 1
                sommet = max(1, min(sommet, maximum_sommet)) 
                Robot.affiche_Ecran(sommet)
            elif infra.buttons(2)== [Button.LEFT_DOWN]: # Décrémente le sommet #Button.DOWN in liste 
                ev3.screen.clear()
                wait(100)     
                sommet = sommet - 1
                sommet = max(1, min(sommet, maximum_sommet))
                Robot.affiche_Ecran(sommet)
            elif infra.buttons(2)== [Button.RIGHT_UP]: # Valide le sommet #Button.CENTER in liste 
                run = False
        return sommet

    def niv_2_Carrefours_bonus(fichier_matrice_orientation):
        sommet1 = Robot.bonus_touchSelection()
        wait(1000)
        sommet2 = Robot.bonus_touchSelection()
        matrice_orientation = Robot.construire_Matrice_Orientation(Robot.lire_Matrice_Orientation(fichier_matrice_orientation))
        angle = 0
        gyro.reset_angle(0)
        orientation = matrice_orientation[sommet1-1][sommet2-1]
        
        # Modifie la direction en valeur d'angle à l'aide du graphique de la matrice orientation        
        if orientation == 'N':
            angle = 0
        elif orientation == 'S':
            angle = 180
        elif orientation == 'E':
            angle = 90 
        elif orientation == 'O':
            angle = 270
        else :
            return 0
        
        # Détermine la direction à prendre pour parcourir l'arête (i,j)
        if gyro.angle() <= 180:
            Robot.tourner_N(angle-gyro.angle())
            Robot.suivre_Ligne()
        elif gyro.angle() > 180: 
            Robot.tourner_N(angle-360)
            Robot.suivre_Ligne()


    def tele():
        ev3.screen.load_image(ImageFile.ANGRY)
        
        trajet = "trajet.txt"
        orientaion = "Orientation.txt"
        chemin = "chemin.txt"
        graphe_Circuit = "facteur6.txt" 
        
        while True:
            if infra.buttons(1)!=[]:
                if infra.buttons(1)[0]== Button.LEFT_UP:
                    Robot.suivre_Ligne()
                    Robot.arret()
                    
                elif infra.buttons(1)[0]== Button.LEFT_DOWN:                    
                    Robot.niv_2_Carrefours(chemin, orientaion)
                    Robot.arret()
                    
                elif infra.buttons(1)[0]== Button.RIGHT_UP:                    
                    Robot.niv_3_Implementation_Manuelle()
                    Robot.arret()
                    
                elif infra.buttons(1)[0]== Button.RIGHT_DOWN:                    
                    Robot.niv_3_DCG(trajet)
                    Robot.arret()
                    
            if infra.buttons(2)!=[]:
                if infra.buttons(2)[0]== Button.LEFT_UP:
                    Robot.niv_4_Gyro(chemin, orientaion)
                    Robot.arret()
                    
                elif infra.buttons(2)[0]== Button.LEFT_DOWN:
                    Robot.niv_4_Matrice(chemin, orientaion)
                    Robot.arret()
                    
                elif infra.buttons(2)[0]== Button.RIGHT_UP:
                    Robot.niv_5_Gyro(orientaion, graphe_Circuit)
                    Robot.arret()
                    
                elif infra.buttons(2)[0]== Button.RIGHT_DOWN:
                    Robot.niv_5_Matrice(orientaion, graphe_Circuit)
                    Robot.arret()
                    
            if infra.buttons(3)!=[]:
                if infra.buttons(3)[0]== Button.LEFT_UP:
                    Robot.niv_2_Carrefours_bonus(orientaion)
                    Robot.arret()
                    
                elif infra.buttons(3)[0]== Button.LEFT_DOWN:
                    Robot.niv_4_Gyro_Obstacle(chemin, orientaion)
                    Robot.arret()
                    
                elif infra.buttons(3)[0]== Button.RIGHT_UP:
                    return Robot.beepboop()