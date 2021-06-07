from random import *
from grille import *
from bateau import *

#PARTIE 1 : MODELISATION ET FONCTIONS SIMPLES

def peut_placer(grille, bateau, position, direction):
    """Grille*Bateau*(int*int)*(int*int)->bool"""
    #on suppose que direction={0,1}
    #si direction=0 alors on place le bateau verticalement
    (x,y)=position  
   
   
    if direction not in [0,1]:
       
        return False
        	
    for i in range( 0,bateau.get_longueur() ):
       
        boolean,val=grille.get_case(x,y)
        if not boolean or (val!=0) :
            return False
        if(direction==0):
            x+=1
        else:   
            y+=1

    return True

def place(grille, bateau, position, direction):
	"""Grille*Bateau*(int*int)*(int*int)->
	si l’opération est possible, rend la grille modifiée 
	où le bateau a été placé comme indiqué
	"""
	
	(x,y)=position
	
	if peut_placer(grille,bateau,position,direction):
	    
	    for i in range(0,bateau.get_longueur()):
	     
	        grille.set_case(x,y,bateau.get_valeur())
	        if(direction==0):
	            x=x+1
	        else:
	            y=y+1    

	        
	        
	    


def place_alea(grille,bateau):
	"""Grille*Bateau->
	place aléatoirement le bateau dans la grille en tirant uniformément 
	une position et une direction aléatoires 
	jusqu’à ce quele positionnement choisi soit admissible et effectué
	"""
	a = randrange(-1,2,1)
	b = randrange(-1,2,1)
	position=(a,b)
	
	direction=randint(0,1)

	while not peut_placer(grille,bateau,position,direction) :
	    
	    direction=randint(0,1)
	    x = randrange(0,10,1)
	    y = randrange(0,10,1)
	    position=(x,y)
	
	
	place(grille, bateau, position, direction)
	
	
def genere_grille_alea():

	grille=Grille()
	
	porte_avion=Bateau(5,1)
	croiseur=Bateau(4,2)
	contre_torpilleurs=Bateau(3,3)
	sous_marin=Bateau(3,4)
	torpilleur=Bateau(2,5)
	
	for b in [porte_avion,croiseur,contre_torpilleurs,sous_marin,torpilleur] :
	    
	    place_alea(grille,b)
		
	return grille	
	
	
	
		
	
#PARTIE 2 : COMBINATOIRE DU JEU

def nombre_combinaisons_un_bateau(grille,bateau):
    """ Grille*Bateau->int"""
    return 2*grille.taille*(grille.taille-bateau.get_longueur()+1) #formule expliquée dans le rapport
   
   
def nombre_positions_possibles(grille,bateau):
    """Grille*Bateau->list[(int*int)*(int*int)]"""
    L=[]
    for i in range(0,10):
        for j in range(0,10):
            for d in [0,1]:
                if(peut_placer(grille,bateau,(i,j),d)):
                    L.append(((i,j),d))
    return L                    
                    
            
    
    
    
       
def nombre_combinaisons_liste(grille,liste_bateaux):

    if not liste_bateaux:
        return 1 #le nombre de façons de placer aucun bateau sur une grille : une seule façon (grille vide)
        
    else:
        liste_positions_possibles=[]
        liste_positions_possibles = nombre_positions_possibles(grille,liste_bateaux[0]) #on récupère la liste de toutes les positions possibles pour le bateau courant.
        cpt=0
        for (position,direction) in liste_positions_possibles:
            place(grille,liste_bateaux[0],position,direction) #on fixe le bateau courant à une position donnée
            cpt=cpt+nombre_combinaisons_liste(grille,liste_bateaux[1:])
            #appel récursif sur le reste de la liste afin de chercher pour le reste des bateaux les positions possibles, en tenant compte qu'on a déjà placé le bateau précedant.
            tmp=0
            longueur=liste_bateaux[0].get_longueur() #arrivé à la fin de la liste,tous les autres bateaux sont fixés, on va pouvoir changer la position du dernier bateau, cette fois-ci il n'y a plus d'appel recursif, on incremente cpt a chaque fois qu'on change de position '
            (x,y)=position
            while(tmp<longueur):
                grille.matrix[x][y]=0 # il faut remettre à 0 pour compter le nombre de façons 
                if(direction==0):
                    x+=1
                else:
                    y+=1
                tmp=tmp+1
                
                
        return cpt
        
        
        
        
def genere_grille(grille):

	grille_generee=genere_grille_alea()
	
	cpt=1
	while(grille_generee != grille):
		grille_generee=genere_grille_alea()
		cpt=cpt+1
		
	return cpt        
			
			

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	


