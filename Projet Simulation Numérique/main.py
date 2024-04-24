#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import ClasseRobot


trajet = "trajet.txt"
orientation = "Orientation.txt"
chemin = "chemin.txt"
graphe_Circuit = "facteur6.txt" 
caref="careffour.txt"

# Choisir niveau avec n (de 2 à 5), choisir le code a utiliser (1 ou autre)
def niv(n,i=1):
    ClasseRobot.ev3.screen.load_image(ImageFile.ANGRY)
    if n==2:
        if i==1:
            return ClasseRobot.Robot.suivre_Ligne()
        else:
            return ClasseRobot.Robot.niv_2_Carrefours(caref, orientation) 
    elif n==3:
        if i==1:
            return ClasseRobot.Robot.niv_3_Implementation_Manuelle()
        else:
            return ClasseRobot.Robot.niv_3_DCG(trajet)
    elif n==4:
        if i==1:
            return ClasseRobot.Robot.niv_4_Gyro(chemin, orientation) 
        else:
            return ClasseRobot.Robot.niv_4_Matrice(chemin, orientation)
    elif n==5:
        if i==1:
            return ClasseRobot.Robot.niv_5_Gyro(orientation, graphe_Circuit)
        else:
            return ClasseRobot.Robot.niv_5_Matrice(orientation, graphe_Circuit)

    elif n==6:
        if i==1:
            return ClasseRobot.Robot.niv_2_Carrefours_bonus(orientation)
        else:
            return ClasseRobot.Robot.niv_4_Gyro_Obstacle(chemin, orientation)

ClasseRobot.Robot.tele()
