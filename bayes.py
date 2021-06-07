from bateau import *
from grille import *
from random import *


class Bayes:

	def __init__(self,taille,pi_centre,pi_bord):
	    #cette fonction initialiste notre classe, avec les deux grilles (grille de probabilités et celle qui contient le bateau), elle prend en parametre la distribution de pii. Ici nous avons fait l'hypothese que le bateau a moins de chances de se trouver aux bords par rapport au centre ( region peu profonde
		self.taille=taille
		self.matricebateau=np.zeros((taille,taille))
		(a,b)=(randint(0,taille-1),randint(0,taille-1))
		self.matricebateau[a][b]=1#on place le bateau dans une case aléatoire dans la grille
		self.matriceproba=np.zeros((taille,taille))

		for i in range(0,taille):
			for j in range(0,taille):
				if(i<(taille//4) or i>=(taille-taille//4))or(j<(taille//4) or j>=(taille-taille//4)):#ici nous avons définit la largeur de la bordure
					self.matriceproba[i][j]=pi_bord
				else:
					self.matriceproba[i][j]=pi_centre


	def trouve(self,position,ps):
	    """cette fonction permet en fonction d'une case(a,b) et selon une hypothese ps, de rentre vrai ssi le bateau s'y trouve et qu'on a réussi à le detecter"""
	    alea=randint(0,1)
	    (a,b)=position
	    if((alea<ps)and(self.matricebateau[a][b]==1)):
	        return True
	    else :
	        return False



	def  rechercher_objet_perdu(self,ps,nbmax):
	    """fonction qui recherche l'objet perdu, ici nous avons supposé que si la recherche ne donne rien au bout de nbmax itérations, nous abandonnons la recherche"""
	    (a,b)=(self.taille//2,self.taille//2)#ici nous avons commmencé la recherche par la case du milieu, car intuitivement on se dit que c'est là que le bateau a le plus de chances d'etre
	    cpt=1

	    while ((not self.trouve((a,b),ps)) and (cpt<nbmax)):#tant qu'on a pas trouvé le bateau ou qu'on a pas itéré nbmax fois :
	        var=self.matriceproba[a][b]
	        self.matriceproba[a][b]=(var*(1-ps))/(1-ps*var)#on diminue la probabilité de la case qu'on a vérifié et ou on a pas trouvé le bateau

	        for i in range(0,self.taille):
	            for j in range(0,self.taille):
	                if (i!=a or j!=b):
	                    self.matriceproba[i][j]=self.matriceproba[i][j]/(1-ps*var)#on augmente la probabilité des autres cases
	        max=0
	        for i in range(0,self.taille):
	            for j in range(0,self.taille):
	                if (self.matriceproba[i][j]>max):

	                    max=self.matriceproba[i][j] #on recherche la case avec la plus grande probabilité
	                    (a,b)=(i,j) #on tire cette case à l'itération suivante
	        cpt+=1

	    if(cpt<nbmax):
	        print("bateau trouvé à la position :",a,",",b," au bout de ",cpt,"coups")
	    else:
	        print("on a pas trouver le bateau et on a arrivé au nombre maximum des coups")






