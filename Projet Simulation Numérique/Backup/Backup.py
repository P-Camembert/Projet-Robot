# Niveau 3, parcours, controlé
"""
class Robot:
    def __init__(self,left_motor,right_motor,wheel_diameter,axle_track):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.wheel_diameter = wheel_diameter
        self.axle_track = axle_track

    def tourne_droite():
        robot.turn(20)
        while light.color == Color.BROWN:
            robot.turn(10)

    def tournegyro(n):
        robot.turn(30*n/abs(n))
        while gyro.angle() >= n:
            robot.turn(-2)
   
    def tourner90(n):
        robot.turn(n*90)

    def tourne_gauche():
        robot.turn(-20)
        while light.color == Color.BROWN:
            robot.turn(-10)

    def avance_distance_n(n):
        robot.straight(n)
    
    def arret():
        robot.stop()
        left_motor.brake()
        right_motor.brake()
        left_motor.hold()
        right_motor.hold()
        wait(2000)
    
    def suivre_ligne():
        # Gaffeur orange, couleur détectée RED
        # Gaffeur noir, couleur détectée BLACK
        # Matela, couleur détectée BROWN
        while light.color() != Color.BLACK: # Détecte si le gaffeur est noir
            
            #Suis la ligne orange, si la ligne est orange il avance et avec une correction il se replace correctement sur la ligne
            #en allant vers l'extérieur, autrement il revient dans la ligne
            
            if light.color() == Color.RED:
                robot.drive(speed,correction)
            else:
                robot.drive(speed,-correction)         
                
def niv3_1():
    rt.gyro.reset_angle(0)
    rt.Robot.suivre_ligne()  
    rt.Robot.arret() #arrive 3
    rt.Robot.avance_distance_n(125)
    rt.Robot.tourne_gauche()
    #rt.Robot.tournegyro(0)
    #rt.Robot.tourner90(-1)
    rt.Robot.suivre_ligne()
    rt.Robot.arret() #arrive 6
    rt.Robot.avance_distance_n(70)
    rt.Robot.suivre_ligne()
    rt.Robot.arret()#arrive 5
    rt.Robot.tourne_droite()
    rt.Robot.suivre_ligne()
    rt.Robot.arret() #arrive 3
    #rt.Robot.tourne_gauche()
    #rt.Robot.suivre_ligne()
    #rt.Robot.arret() #arrive 2       

def niv4foireux(graphe):
    rt.Robot.suivre_ligne()  
    rt.Robot.arret()
    for i in range(1,len(graphe)):
        if i!=(len(graphe)-1):
            e=rt.M2[graphe[i]-1][graphe[i-1]-1][graphe[i+1]-1]
            if e == "G" : # Deplacement a gauche
                rt.Robot.avance_distance_n(50)
                rt.Robot.tourne_gauche()
            elif e == "C" : # Deplacement tout droit
                rt.Robot.avancered()
            elif e == "D" : # Deplacement a droite
                rt.Robot.avance_distance_n(50)
                rt.Robot.tourne_droite()
            rt.Robot.suivre_ligne()  
            rt.Robot.arret()
        robot.beep()
niv4foireux([1,3,6,5,3,2,4,5])
"""

"""
gyro.reset_angle(0)
if gyro.angle() == 270 :
    robot.speaker.beep()


# Partie test :

fichier_chemin = "chemin.txt"
matrice_orientation = [
    ['X', 'O', 'E', 'X', 'X', 'X'],
    ['N', 'X', 'E', 'O', 'S', 'X'],
    ['N', 'O', 'X', 'X', 'S', 'E'],
    ['X', 'N', 'X', 'X', 'E', 'X'],
    ['X', 'N', 'E', 'O', 'X', 'S'],
    ['X', 'X', 'N', 'X', 'S', 'X']
]

[['X', 'O', 'E', 'X', 'X', 'X'],
['N', 'X', 'E', 'O', 'S', 'X'],
['N', 'O', 'X', 'X', 'S', 'E'],
['X', 'N', 'X', 'X', 'E', 'X'],
['X', 'N', 'E', 'O', 'X', 'S'],
['X', 'X', 'N', 'X', 'S', 'X']]
def matrice(orientation):
    matrice=[[[] for i in range (len(orientation))] for i in range(len(orientation))]

prototypefoireux
def niv4foireuxv1(graphe):
    rt.Robot.suivre_ligne()  
    rt.Robot.arret()
    for i in range(1,len(graphe)):
        if i!=(len(graphe)-1):
            e=rt.M2[graphe[i]-1][graphe[i-1]-1][graphe[i+1]-1]
            if e == "G" : # Deplacement a gauche
                rt.Robot.avance_distance_n(50)
                rt.Robot.tourne_gauche()
            elif e == "C" : # Deplacement tout droit
                rt.Robot.avancered()
            elif e == "D" : # Deplacement a droite
                rt.Robot.avance_distance_n(50)
                rt.Robot.tourne_droite()
            rt.Robot.suivre_ligne()  
            rt.Robot.arret()
        robot.beep()
niv4foireuxv1([1,3,6,5,3,2,4,5])

---FONCTION TEST---

ev3.screen.print(light.color())
wait(2000)
ev3.screen.print(light.reflection())
wait(2000)

    def trajet(fichier_trajet) :
        with open(fichier_trajet, 'r') as f:
            ligne = f.readlines()
            print(ligne) # Affiche la liste de direction présent dans le fichier
        
        for sommet in ligne :
            for direction in sommet :
                if direction == "G" : # Déplacement à gauche
                    Robot.tourne_gauche()
                elif direction == "C" : # Déplacement au centre
                    Robot.suivre_ligne()
                    Robot.arret()
                elif direction == "D" : # Déplacement à droite
                    Robot.tourne_droite()
"""
"""
def niv3_2(txt):
    with open(txt, 'r') as f:
            ligne = f.readlines()
            print(ligne)
        
    rt.Robot.suivre_ligne()    
    rt.Robot.arret()
    for e in ligne[0]:
        if e == "G" : # Déplacement à gauche
            rt.Robot.avance_distance_n(50)
            rt.Robot.tourne_gauche()
        elif e == "C" : # Déplacement tout droit
            rt.Robot.avancered()
        elif e == "D" : # Déplacement à droite
            rt.Robot.avance_distance_n(50)
            rt.Robot.tourne_droite()
        rt.Robot.suivre_ligne()  
        rt.Robot.arret()
#niv3_2(fichier)







##############
##############

import PSN_estPont
def fleury(graphe, sommet_depart_choisi):
    C = []  # Chaîne contenant les sommets visités
            # Sommet de départ, choisi arbitrairement
    C.append(sommet_depart_choisi)
    while graphe[sommet_depart_choisi]:
        y = graphe[sommet_depart_choisi][0]  # Prendre le premier successeur de x
        while PSN_estPont.estPont(graphe, sommet_depart_choisi, y) and len(graphe[sommet_depart_choisi]) > 1:
            graphe[sommet_depart_choisi].remove(y)
            graphe[y].remove(sommet_depart_choisi)
            y = graphe[sommet_depart_choisi][0]  # Prendre le prochain successeur de x
        C.append(y)
        graphe[sommet_depart_choisi].remove(y)
        graphe[y].remove(sommet_depart_choisi)
        sommet_depart_choisi = y
    return C

# Exemple d'utilisation
graphe = {
    0: [1, 2, 3, 4],
    1: [0, 2, 3, 4],
    2: [0, 1, 3, 4],
    3: [0, 1, 2, 4],
    4: [0, 1, 2, 3]
}

graphe2= {
    1:[2,3],
    2:[3,4,5,6],
    3:[2,4,5,6],
    4:[2,5],
    5:[2,3,4,6],
    6:[3,5]
}


sommet_depart_choisi = int(input("Entrez le sommet de départ : "))
print("Chaîne de Fleury:", fleury(graphe2, sommet_depart_choisi))




def matrix_power(a, n):
    if n == 0:
        # Renvoie la matrice identité si la puissance est 0
        size = len(a)
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    elif n == 1:
        # Renvoie simplement la matrice originale si la puissance est 1
        return a
    else:
        # Calcul de la puissance de la matrice en utilisant des boucles
        result = a
        for _ in range(1, n):
            result = matrix_multiply(result, a)
        return result

def matrix_multiply(a, b):
    # Multiplication de deux matrices
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        raise ValueError("Le nombre de colonnes de la matrice a doit être égal au nombre de lignes de la matrice b.")

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]

    return result

########################################################
estpont
########################################################
def produit_matriciel(matrice1, matrice2):
    # Vérifie si les dimensions des matrices sont compatibles pour le produit matriciel
    if len(matrice1) != len(matrice2[0]):
        raise ValueError("Les dimensions des matrices ne sont pas compatibles pour le produit matriciel")

    # Initialise la matrice résultante avec des zéros
    resultat = [[0] * len(matrice2[0]) for _ in range(len(matrice1))]

    # Effectue le produit matriciel
    for i in range(len(matrice1)):
        for j in range(len(matrice2[0])):
            for k in range(len(matrice2)):
                resultat[i][j] += matrice1[i][k] * matrice2[k][j]

    return resultat

def puissance_matrice(matrice, puissance):
    # Initialise la matrice résultante avec l'identité
    resultat = [[1 if i == j else 0 for j in range(len(matrice))] for i in range(len(matrice))]

    # Élève la matrice à la puissance spécifiée
    for _ in range(puissance):
        resultat = produit_matriciel(resultat, matrice)

    return resultat


def estPont(graphe, i, j):
    # Supprimer l'arete (i, j) du graphe temporairement
    graphe_temporaire = {sommet: voisins.copy() for sommet, voisins in graphe.items()}
    graphe_temporaire[i].remove(j)
    graphe_temporaire[j].remove(i)
    
    # Calculer la matrice d'adjacence du graphe temporaire
    n = len(graphe_temporaire)
    A = [[0 for i in range(n)]for i in range(n)]
    for sommet, voisins in graphe_temporaire.items():
        for voisin in voisins:
            A[sommet][voisin] = 1
    
    # Calculer la somme des puissances de la matrice d'adjacence
    S = [[0 for i in range(n)]for i in range(n)]
    for k in range(n):
        S += puissance_matrice(A, k)
    
    # Verifier si l'element S[i][j] est nul
    est_un_pont = S[i][j] == 0
    
    return est_un_pont
    
    # Même fonction que celle du niveau 4 mais sans l'appel de la fonction lire_chemin
    def niv_4_GyroSansLireChemin(chemin_fleury, fichier_matrice_orientation):
            chemin = chemin_fleury
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
"""