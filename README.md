# Snake-Game
In this project, I developed a snake game utilizing Object-Oriented Programming in Python with a Test Driven Development approach and PyGlet library.

Given the next instructions, I developed the code:


##Instructions:

Création d'un jeu du snake

à chaque update (toutes les 1/10 secondes), le snake avance dans une des quatre directions haut, bas, gauche ou droite. Initialement, la tête du snake est placée au milieu de l'écran et il se déplace vers le haut.
lorsque l'on appuie sur une touche de direction, la direction du snake change. On ne peut cependant pas aller à l'opposé de la direction actuelle
lorsque l'on appuie sur la touche espace, le jeu se met en pause (le snake s'arrête de bouger et le score s'arrête d'augmenter). En appuyant sur la barre d'espace, le jeu redémarre.
Initialement, le jeu est en pause. Il faut appuyer sur la barre d'espace pour que le snake se déplace. La direction par défaut est vers le haut.

Le snake est composé de carrés de 20 pixels de long qui se suivent en se touchant par un côté. Initialement, le snake est constitué de 3 carrés.

Position initiale du snake (□ est la tête du snake) :

 □
 O
 O
A chaque déplacement le 1er carré se déplace de 20 pixels dans la direction de déplacement, les carrés suivant se plaçant là où était le carré précédent (attention, le snake ne peut pas reculer).

Exemple. Position initiale du snake composé de 6 carrés (0 est la tête du snake) :

  O□
  O
OOO
Déplacement vers le haut (de 20pixels) :

   □
  OO
  O
 OO
Le jeu s'arrête si :

le snake sort de l'écran
un carré composant le snake se superpose avec un autre après un déplacement.
Le score augmente de 1 toutes les secondes où le snake est vivant et que le jeu n'est pas en pause. Initialement, le score vaut 0 et est affiché en haut à droite de l'écran.

Toutes les 5 secondes vont apparaître à l'écran (à une position aléatoire mais pas sur le snake) des disques de rayon 40 pixels. Lorsque le snake passe dessus, son score augmente de 5 et sa taille augmente de 5 carrés (le snake va grossir de 1 carré à chacun des 5 déplacements suivants) :

Exemple de grossissement du snake.

Position initiale :

 OO□
On veut faire augmenter la taille du snake de 2 carrés. On suppose également que le snake se déplace vers le haut.

Après le 1er déplacement, le snake à grossi de 1 carré (X est le nouveau carré) :

   □
 XOO
Après le 2ème déplacement, le snake a encore grossi de carré (X est le nouveau carré) :

   □
   O
 XOO
Finalement, le snake se déplace normalement. Par exemple, s'il continue de se déplacer vers le haut :

   □
   O
   O
  OO
etc...

Bonus/Malus/vies
Ajoutez à votre projet :

des vies à votre snake
des bonus qui diminuent la taille
des bonus qui augmentent le score
des malus qui font mourir le snake lorsque qu'il passe dessus
Vous expliciterez dans votre rapport comment vous avez fait pour implémenter ces différentes chose.

Organisation du projet
Vous devez créer autant de classes que nécessaires pour votre projet. Il devra au moins avoir :

votre rapport doit contenir les noms des membres de votre groupe.
une classe Snake
les 2 classes Bonus et Malus doivent hériter d'un même ancêtre
Vous devrez bien séparer ce qui a trait à l'interface pyglet (qi n'est pas pas testé) et ce est de l'ordre de l’interaction entre les différents objets (qui est testé).
