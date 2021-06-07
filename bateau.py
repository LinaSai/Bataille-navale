class Bateau : 
    """Classe définissant un bateau caractérisée par une longueur"""
	
    def __init__ (self,longueur,valeur):
        
        """ int*int -> Bateau
        constructeur de Bateau
        """
        self.__valeur=valeur 
        self.__longueur=longueur
        
    def get_longueur(self):
        """ ->int
        retourne la longueur du bateau
        """
        return self.__longueur
        
    def get_valeur(self):
        """ ->int
        retourne la valeur du bateau
        """
        return self.__valeur    
		
				
    		
        	
