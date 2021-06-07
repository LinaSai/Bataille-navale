from bateau import *
from grille import *
from fonctions1_2 import *

class Bataille:


	def __init__(self):
		self.grille=genere_grille_alea()




	def joue_alea(self):

		liste_tire=[] # nous stockons la liste des positions tirées, afin de ne pas les tirer ultérieurement

		cpt=0
		tmp=0

		while (cpt<17): #le nombre total de cases( de tous les bateaux) est égal à 17

			tmp=tmp+1

			(a,b)=(randint(0,9),randint(0,9))

			while (a,b) in liste_tire: #on tire aléatoirement tant que la case a déjà été tirée

				(a,b)=(randint(0,9),randint(0,9))

			if (self.grille.matrix[a][b]!=0): #si la case tirée n'est pas vite

				cpt=cpt+1 # on crie "touché" et on se rapproche encore plus de la victoire ;)


			liste_tire.append((a,b)) #on ajoute la position tirée dans la liste


		return tmp # on retourne le nombre de tirages nécessaires pour terminer le jeu


#------------------------------------------------------------------------------------------------------------
#---------------------------VERSION PROABILISTE SIMPLIFIEE-------------------------------------------------
#-----------------------------------------------------------------------------------------------------------





	def nb_facons_placer_bateau_case(self,position,bateau,grille_modifie):
	    cpt=0
	    (a,b)=position
	    if grille_modifie.matrix[a][b]==0:
	    #on fait des calculs si et seulement si la case est vide ( ne contient pas déjà un bateau)
		    lon=bateau.get_longueur()
		    val=bateau.get_valeur()
		    for i in range(0,lon): #pour savoir si on peut placer le bateau, il faut parcourir un nombre de fois <==> sa longueur
		        cpt_interne=0
		        for j in range(0,lon):#et on fait cela en débutant de toutes les cases connexes de (a,b) -de la gauche vers la droite-, toujours avec une distance egale a la longueur du bateau et incluant la case donnée en parametre
		            if(a-i+j>9 or a-i+j<0):
		                break
		            if (grille_modifie.matrix[a-i+j][b]!=0 and grille_modifie.matrix[a-i+j][b]!=val): #on ne fait rien si en cours de route, une case est occupée par un bateau hors que celui passé en parametre
		                break
		            else:
		                cpt_interne+=1
		        if cpt_interne==lon:#si on a parcouru une distance égale a la longueur, et aucune des cases était occupée
		        #ici le test pour savoir la valeur de la case va nous servir ensuite, car meme si une case est occupée par un bateau , si c'est le meme que celui en parametre ( de meme valeur) on voudra quand meme le compter, ( en vérité les chances que le bateau se trouve dans une zone connexe a cette case va augmenter)
		            cpt+=1

		     #meme chose que précedemment, sauf que ici on cherche à placer le bateau verticalement
		    for i in range(0,lon):
		        cpt_interne=0
		        for j in range(0,lon):
		            if(b-i+j>9 or b-i+j<0):
		                break
		            else:
		                if(grille_modifie.matrix[a][b-i+j]!=0 and grille_modifie.matrix[a][b-i+j]!=val):
		                    break
		                else:
		                    cpt_interne+=1
		        if cpt_interne==lon:
		            cpt+=1

	    return cpt




	def grille_de_probabilite(self,bateau,grille_modifie):
		""" Bataille*Bateau*Grille->Grille
		    Cette fonction retourne la grille qui contient pour un bateau donné et pour chaque case, la probabilité que le bateau ne s'y trouve pas"""

		cpt=0
		grilleCompteur=Grille()

		for i in range (0,10):
			for j in range (0,10):
				a=self.nb_facons_placer_bateau_case((i,j),bateau,grille_modifie)
				grilleCompteur.matrix[i][j]=a # ici, on crée une grille qui contient pour chaque case le nombre de façons d'y placer le bateau
				cpt+=a #accumulateur representant la cardinalité de l'univers qui contient le nombre de placements possibles pour ce bateau dans la grille


		for i in range (0,10):
			for j in range (0,10):
				a=(cpt-grilleCompteur.matrix[i][j])/cpt #en divisant par cpt, on aura bien une probabilité par case, ici on soustrait la probabilité de chaque case de 1 afin d'obtenir la probabilité que le bateau ne s'y trouve pas
				grilleCompteur.matrix[i][j]=a

		return grilleCompteur




	def grille_finale(self,liste,grille_modifie):
	    """ Bataille*list[Bateau]*Grille->Grille"""
	    gfinal=Grille()
	    gfinal.set_matrix(np.ones((10,10)))#car on va multiplier

	    for k in liste:

	        g=self.grille_de_probabilite(k,grille_modifie) #on calcule la grille de probabilité pour chaque bateau se trouvant dans la liste passée en parametre
	        gfinal.matrix*=g.matrix #ici grille finale sera la grille ou la valeur de chaque case représente la probabilité que le bateau 1 ne s'y trouve pas ET que le bateau 2 ne s'y trouve pas ET...etc

	    grille1=np.ones((10,10))
	    gfinal.matrix=np.subtract(grille1,gfinal.matrix) # en soustrayant 1 a chaque case de la grille finale précédente, nous allons avoir la probabilité qu'elle contienne soit le bateau 1 OU le bateau 2 OU..etc


	    return gfinal






	def joue_probabiliste_simplifiee(self):

		b1=Bateau(5,1)
		cpt1=5 # on initialise les cpt à la longueur des bateaux
		b2=Bateau(4,2)
		cpt2=4
		b3=Bateau(3,3)
		cpt3=3
		b4=Bateau(3,4)
		cpt4=3
		b5=Bateau(2,5)
		cpt5=2
		liste=[b1,b2,b3,b4,b5]#liste qui contientra les bateaux qu'on a toujours pas coulés

		reussi=0
		grille_modifie=Grille() #grille de jeu qu'on va modifier à chaque coup
		cpt=0

		while(reussi<17): #tant qu'on n'a pas coulé tous les bateaux :
			grille_probabiliste=self.grille_finale(liste,grille_modifie) #on calcule ici la grille ou chaque case represente la probabilité de contenir au moins un bateau (les bateaux se trouvant dans la liste, qu'on mettra à jour plutard)

			max=0
			for i in range (0,10):
				for j in range (0,10):
					if (grille_probabiliste.matrix[i][j]>max):
						max=grille_probabiliste.matrix[i][j] # ici nous allons chercher le maximum ( la probabilité la plus grande), ie : la case ou il y a plus de chances de trouver un bateau
						pos_touchee=(i,j)

			(a,b)=pos_touchee

			if (self.grille.matrix[a][b]==0): # si la case qu'on a tirée est vide ( c'est possible d'avoir ce cas )
				grille_modifie.matrix[a][b]=-1 # on modifie sa valeur dans la grille afin de ne pas la tirer encore une fois ( meme fonctionnement que liste_deja_tire)
				cpt+=1 #cpt represente le résultat à retourner : le nombre de fois ou on a tiré une position

			else:
				liste=[]
				grille_modifie.matrix[a][b]=self.grille.matrix[a][b]
				reussi+=1
				cpt+=1
				if(self.grille.matrix[a][b]==1): #si c'est le bateau 1 qu'on a touché
					cpt1=cpt1-1 #on décremente sa longueur

				if(cpt1!=0): #si la longueur n'est pas nulle : on n'a pas encore coulé toutes les cases du bateau
					liste.append(b1) # on ajoute ce bateau à la liste

                #on repete la meme chose pour tous les bateaux
                #ici, on ne fait pas de if,else car il est important d'ajouter les autres bateaux pas encore coulés, meme si ce n'est pas eux qu'on a touché lors du tirage de la case (a,b)
				if(self.grille.matrix[a][b]==2):
					cpt2=cpt2-1

				if(cpt2!=0):
					liste.append(b2)


				if(self.grille.matrix[a][b]==3):
					cpt3=cpt3-1

				if(cpt3!=0):
					liste.append(b3)

				if(self.grille.matrix[a][b]==4):
					cpt4=cpt4-1

				if(cpt4!=0):
					liste.append(b4)

				if(self.grille.matrix[a][b]==5):
					cpt5=cpt5-1

				if(cpt5!=0):
					liste.append(b5)

		return cpt


#------------------------------------------------------------------------------------------------------------
#---------------------------VERSION HEURISTIQUE-------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

	def trouve_liste_voisin(self,position,liste_deja_tiree):

		liste_voisine=[] #on initialise la liste des voisins de la case passée en parametre
		(a,b)=position

		if(a-1>=0):#on commence par vérifier si nous ne sommes pas aux bords de la grille

			if ((a-1,b) not in liste_deja_tiree): #si la case n'a pas déjà été tirée (test important dans la fonction récursive car on va appeler la fonction sur les voisines,ensuite sur les voisines des voisines). Solution alternative : changer la valeur de la case dans la matrice une fois ajoutée

				if(self.grille.matrix[a-1][b]!=0):#si la case voisine contient un bateau :
					liste_voisine.append((a-1,b))#on l'ajoute a la liste des voisines

				liste_deja_tiree.append((a-1,b))#dans tous les cas, on les rajoute à la liste des positions déja tirées, pour gagner en efficacité

                #on repete ça pour les 4 cases adjacentes à la case passée en parametre
		if(a+1<10):
			if ((a+1,b) not in liste_deja_tiree):
				if(self.grille.matrix[a+1][b]!=0):
					liste_voisine.append((a+1,b))

				liste_deja_tiree.append((a+1,b))


		if(b-1>=0):
			if ((a,b-1) not in liste_deja_tiree):
				if(self.grille.matrix[a][b-1]!=0):
					liste_voisine.append((a,b-1))

				liste_deja_tiree.append((a,b-1))


		if(b+1<10):
			if ((a,b+1) not in liste_deja_tiree):
				if(self.grille.matrix[a][b+1]!=0):
					liste_voisine.append((a,b+1))

				liste_deja_tiree.append((a,b+1))

		return (liste_voisine,liste_deja_tiree)



	def heuristique_rec(self,liste_voisines,liste_deja_tiree,resultat):

		if liste_voisines==[] : #cas de base, ou on arrive a une case qui n'a plus de voisines qui contient un bateau, ( toutes les autres ont déjà été ajoutées)

			return (resultat,liste_deja_tiree)

		else:

			L_nouvelles_voisines=[] #on déclare une liste de cases qu'on va rajouter à chaque appel recursif sur les cases voisines pour avoir à leur tour les cases adjacentes non vides

			(L_nouvelles_voisines,liste_deja_tiree)=self.trouve_liste_voisin(liste_voisines[0],liste_deja_tiree) #on ajoute les voisines de la premiere case

			resultat.extend(L_nouvelles_voisines) #on stocke les cases ajoutées au tour courant

			liste_voisines.extend(L_nouvelles_voisines) #on les ajoute aux cases déja tirées pour ne pas les tirer encore une fois

			(resultat,liste_deja_tiree)=self.heuristique_rec(liste_voisines[1:],liste_deja_tiree,resultat) #appel récursif sur le reste des cases adjacentes de couche 1


		return (resultat,liste_deja_tiree) #on retourne les nouvelles caches adjacentes ( de couche 2) qui sont non vides, ainsi que la liste des cases tirées


	def joue_heuristique(self):

		liste_deja_tire=[]
		cpt=0
		tmp=0

		while (cpt<17):

			(a,b)=(randint(0,9),randint(0,9))

			while (a,b) in liste_deja_tire:
				(a,b)=(randint(0,9),randint(0,9))


			liste_deja_tire.append((a,b))#on ajoute la case à la liste des positions déja tirées


			if(self.grille.matrix[a][b]!=0):# si la case tirée contient un bateau :

				(listevoisin,liste_deja_tire)=self.trouve_liste_voisin((a,b),liste_deja_tire) #on va chercher la liste des cases adjacentes qui contiennent un bateau, l'important de passer liste_deja_tire en parametre est de s'assurer qu'on ajoute pas plusieurs fois les memes cases, vu qu'on teste l'appartenance à cette liste dans la fonction trouve_liste_voisin

				cpt=cpt+len(listevoisin)+1 # on ajoute à cpt le nombre de voisins contenant un bateau et +1 car on compte aussi la position qu'on a tirée

				resultat=[]
				(resultat,liste_deja_tire)=self.heuristique_rec(listevoisin,liste_deja_tire,resultat)
				cpt=cpt+len(resultat) #on ajoute à cpt le nombre de cases adjacentes à la liste des voisines qui contiennent un bateau


		return len(liste_deja_tire) #on retourne la liste de toutes les cases tirées


