# Bataille-navale

Ce petit projet a comme objectif d’étudier le jeu de la bataille navale d’un point de vue
probabiliste. Il s’agira dans un premier temps d’étudier la combinatoire du jeu, puis de
proposer une modélisation du jeu afin d’optimiser les chances d’un joueur de gagner, et
enfin d’étudier une variante du jeu plus réaliste.

Le jeu de la bataille navale se joue sur une grille de 10 cases par 10 cases. L’adversaire place sur cette grille un certain nombre de bateaux qui sont caractérisés par leur
longueur :
• un porte-avions (5 cases) ;
• un croiseur (4 cases) ;
• un contre-torpilleurs (3 cases) ;
• un sous-marin (3 cases) ;
• un torpilleur (2 cases).
Il a le droit de les placer verticalement ou horizontalement. Le positionnement des bateaux reste secret. L’objectif du joueur est de couler tous les bateaux de l’adversaire en
un nombre minimum de coup. A chaque tour de jeu, il choisit une case où il tire : si il
n’y a aucun bateau sur la case, la réponse est vide ; si la case est occupée par une partie
d’un bateau, la réponse est touché ; si toutes les cases d’un bateau ont été touchées,
alors la réponse est coulé et les cases correspondantes sont révélées. Lorsque tous les
bateaux ont été coulés, le jeu s’arrête et le score du joueur est le nombre de coups qui
ont été joués. Plus le score est petit, plus le joueur est performant.
