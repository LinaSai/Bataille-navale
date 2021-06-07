from grille import *
from bateau import *
from fonctions1_2 import *
from bataille import *
from bayes import *

b1=Bateau(5,1)
b2=Bateau(4,2)
b3=Bateau(3,3)
b4=Bateau(3,4)
b5=Bateau(2,5)

grille=Grille()
grille2=Grille()



grille.__repr__()

print()
print("borne supérieure du nombre des combinaisons un bateau ",nombre_combinaisons_un_bateau(grille,b2))
print("nombre de positions",len(nombre_positions_possibles(grille,b2)))



print("Partie 2")


#liste_bateaux=[b1]
 #print(nombre_combinaisons_liste(grille,liste_bateaux))

bataille=Bataille()



print("Version aléatoire",bataille.joue_alea())
print("Version heuristique",bataille.joue_heuristique())
print("Version probabiliste simplifiée",bataille.joue_probabiliste_simplifiee())

#bayes=Bayes(10,0.6,0.2)

#bayes.rechercher_objet_perdu(0.8,100)
