# Projet_Incendie_L1

IN200: projet de simulation de la propagation d’un incendie

Ce projet a pour objectif de vous apprendre à construire un programme réalisant ce qui est indiqué dans le sujet. Le sujet vous donne des indications sur la manière de construire votre programme et il doit être lu attentivement. 

Le projet doit être écrit en Python. Les compétences techniques attendues sont celles du cours IN100 du premier semestre. Quelques compléments pourront être apportés en cours sur des points précis de programmation en Python. Vous devez utiliser les outils de programmation étudiés en IN100, à savoir le gestionnaire de version git couplé au dépôt GitHub, le linter flake8 qui doit être installé avec votre environnement VSCode, et le debugger fourni avec VSCode.

Le projet a pour objet la simulation de la propagation d’un incendie. Il comporte une partie graphique qui permettra de visualiser ce que l’on cherche à simuler, ainsi qu’un ensemble de fonctionnalités qui enrichiront le programme.

* Contraintes de programmation : 

- le programme doit être écrit dans un unique fichier qui s’appelle incendie.py;
- le programme ne doit pas définir de classes d’objets;
- vous devez utiliser la librairie graphique tkinter;


* Le programme sera découpé de la manière suivante:

- import des librairies
- définition des constantes (écrites en majuscule)
- définition des variables globales
- définition des fonctions (chaque fonction devra contenir une docstring)
- programme principal contenant la définition des widgets et des événements qui leur sont liés et l’appel  à la boule de gestion des événements


* Sujet : 

On considère un terrain rectangulaire constitué de LARGEUR x HAUTEUR parcelles, où LARGEUR et HAUTEUR sont des constantes définies au début du programme et laissées à votre appréciation. Chaque parcelle est représentée par un carré dont la couleur est donnée par le type du terrain, couleurs données par le tableau suivant:

Type 	            Couleur 	Durée de l’état
Eau 	            Bleu 	    + ∞
Forêt 	            Vert 	    Dépend des voisins
Feu 	            Rouge 	    Constante DUREE_FEU
Prairie 	        Jaune 	    Dépend des voisins
Cendres tièdes 	    Gris 	    Constante DUREE_CENDRE
Cendres éteintes 	Noir 	    + ∞


* Les règles d’évolution sont les suivantes : 

- une parcelle d’eau reste une parcelle d’eau durant toute la simulation;
- une parcelle qui devient en feu reste en feu durant la durée DUREE_FEU avant de devenir des cendres tièdes pendant la durée DUREE_CENDRE et enfin devenir des cendres éteintes durant le reste de la simulation; les valeurs de ces deux constantes sont à définir et laissées à votre appréciation;
- une parcelle de prairie prend feu dès qu’une des 4 cases voisines (gauche, droite, haut, bas) est en feu;
- une parcelle de forêt prend feu avec la probabilité 0.1 × nf où nf est le nombre de ses voisins en feu;

On considère que les bords du terrain ne peuvent pas brûler et qu’ils n’interviennent pas dans la propagation du feu. Le programme doit malgré tout être adapté pour les parcelles du bord.


* Votre programme devra contenir les fonctionnalités suivantes:

     - fonctionnalités liées au choix du terrain:
        -> un bouton qui génère un terrain au hasard avec des parcelles d’eau, de forêt et de prairie;
        -> un clic sur une parcelle de forêt ou de prairie la transforme en parcelle en feu;
        -> un bouton pour sauvegarder l’état du terrain dans un fichier;
        -> un bouton pour charger un terrain depuis un fichier;

    - fonctionnalités liées à la simulation:
        -> un bouton permet d’effectuer une étape de simulation; cela doit aussi être possible en appuyant sur une touche du clavier (à définir);
        -> un bouton qui permet de démarrer une simulation; le nombre d’étapes doit alors s’afficher, ainsi que le nombre de parcelles en feu, et la simulation s’arrête quand il n’y a plus de parcelle en feu;
        -> un bouton pour arrêter la simulation;


