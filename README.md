# Projet-Robot
Projet Robot, ev3 ECAM - Rennes

Bonjour l'ami ! Dans ce document, tu retrouveras tous les codes que notre équipe a pu coder dans le cadre du projet de simulation numérique avec le robot EV3, pour l'ECAM - Rennes.
Fais-en ce que tu veux ! Nous avons essayé de rendre le code le plus lisible possible, et il y a même, si tu le souhaites, des organigrammes qui expliquent comment le code fonctionne, sans ligne de code ; c'est plus lisible ;). Tous les codes fonctionnent correctement.
Il faut juste savoir que notre projet de simulation numérique utilise l'algorithme de Fleury pour trouver un chemin optimal, à partir d'un sommet de départ que tu choisis. Donc, il faudra peut-être adapter l'algorithme demandé pour ton projet, si jamais il est différent, évidemment. Également, il faut faire attention aux ports où sont branchés ton moteur, tes capteurs, etc... Si tu construis ton robot différemment, il ne fonctionnera pas avec notre code.

Si tu es juste de passage et n'étudies pas à l'ECAM, et que tu aimes beaucoup la robotique avec le boîtier EV3, bah tu peux profiter de ce code également ! Et pareillement, veille bien à la correspondance des ports entre ton robot et ceux dans notre code.

Pour utiliser les codes, il faut appeler la fonction tele, qui utilise la télécommande et le capteur infrarouge. Ensuite, il faut choisir le bon canal sur la télécommande et appuyer sur la touche correspondante au code que tu veux utiliser.
Ou alors tu appelles directement la fonction dans le main, c'est plus rapide. Pour ça, n'oublie pas d'appeler la classe robot comme suit : ClasseRobot.Robot. et le nom de ta fonction.
Certains codes utilisent la télécommande pour sélectionner le sommet de départ. (Le niveau 5 et le niveau 2 bonus)

Voilà voilà ! S'il y a des questions, n'hésite pas à me contacter via l'adresse mail sur mon profil, si ça ne se voit pas c'est : fercq.strz@gmail.com.
Bon courage à toi !


Hello friend! In this document, you will find all the code that our team has been able to develop as part of the digital simulation project with the EV3 robot, for ECAM - Rennes.
Feel free to use it however you like! We've tried to make the code as readable as possible, and there are even flowcharts, if you wish, that explain how the code works without any lines of code; it's easier to read that way ;). All the code works correctly.
Just know that our digital simulation project uses the Fleury algorithm to find an optimal path from a chosen starting vertex. So, you may need to adapt the algorithm required for your project if it's different, of course. Also, be careful with the ports where your motor, sensors, etc., are connected... If you build your robot differently, it won't work with our code.

To use the codes, you need to call the tele function, which utilizes the remote control and the infrared sensor. Then, you need to choose the correct channel on the remote control and press the corresponding button for the code you want to use.
Alternatively, you can directly call the function in the main, which is faster. For that, don't forget to call the robot class as follows: ClasseRobot.Robot. and the name of your function.
Some codes use the remote control to select the starting vertex (Niveau 5 and niveau 2 bonus).

If you're just passing by and not studying at ECAM, and you really enjoy robotics with the EV3 brick, well, you can still make use of this code! Similarly, make sure to match the ports between your robot and those in our code.

There you have it! If you have any questions, don't hesitate to contact me via the email address on my profile, if it's not visible, it's: fercq.strz@gmail.com.
Good luck to you!
