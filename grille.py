import numpy as np
import matplotlib.pyplot as plt

class Grille : 
    """Classe définissant une grille carrée d'entiers caractérisée par : une taille ( qui sera initialisée à 10 dans ce jeu )"""
        
    def __init__ (self):
        """ -> Grille
        constructeur de Grille
        """
        
        self.taille=10
        self.matrix=np.zeros((self.taille,self.taille))
                                
                                
    def __eq__(self, other) :
        """ -> bool rend le booléen vrai si la Grille est égale à other, faux sinon. Elle permet que == fonctionne pour les grilles"""
        
        if type(self)!=type(other) or self.taille!=other.taille :
            return False

                                
        for i in range(0,self.taille) :
            for j in range(0,self.taille) :
                
                if self.matrix[i][j]!=other.matrix[i][j]:
                    return False
        return True     
       
    def set_matrix(self,matrix):
        self.matrix=matrix

        
          
        
                
    def get_case(self,x,y) :
        """ int*int -> int*bool
        rend la valeur de la case grille[x][y]
        """     
        t=self.taille   
        if (x > t-1) or (y > t-1) or (x<0) or (y<0):
            return False,-1 
        return True,self.matrix[x][y]
     
        
    def set_case(self,x,y,val) :
        """ int*int*int-> 
        met à jour la valeur de la case grille[x][y]
        """     
        self.matrix[x][y]=val  
  
              
    def __repr__(self):
        """permet d'afficher la matrice dans le terminal"""
        print(self.matrix)
   
        
    
    def affiche(self):
        """permet d'afficher la matrice dans une fenetre graphique"""
        plt.imshow(self.matrix)
        plt.show()
        
        
                
