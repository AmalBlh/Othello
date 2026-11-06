from enum import Enum

class Couleur(Enum):
      VIDE = 0
      BLANC = 1
      NOIR = 2

      

class Case:
    def __init__(self, x, y, stat):
                self.__x = x
                self.__y = y
                self.set_stat(stat)

    def set_stat(self, stat):
        if isinstance(stat, Couleur) :
            self.__stat = stat
        else:
             raise TypeError("Le statut de la case n'est pas de type Couleur (Vide, Blanc ou Noir)")

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
    
    def get_stat(self):
        return self.__stat

    def set_pawn(self, couleur):
        if self.get_stat() != Couleur.VIDE:
            raise ValueError("A essayé de poser un pion sur une case non vide")
        elif not isinstance(couleur, Couleur):
            raise TypeError("Le statut demandé n'est pas de type Couleur (Vide, Blanc ou Noir)")
        elif couleur == Couleur.VIDE:
            raise ValueError("Ne peut pas poser un pion de type vide")
        self.set_stat(couleur)
    
    def flip(self):
        if self.get_stat() == Couleur.VIDE:
            raise ValueError("Ne peut pas fliper une case vide")
        
        elif self.get_stat() == Couleur.BLANC:
            self.set_stat(Couleur.NOIR)

        elif self.get_stat() == Couleur.NOIR:
            self.set_stat(Couleur.BLANC)

