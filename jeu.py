from joueur import Joueur
from plateau import Plateau
from case import Couleur

class Jeu:

    def __init__(self):
    
        self.plateau = Plateau()
        self.joueur1 = Joueur("Test", Couleur.NOIR, 0)
        self.joueur2 = Joueur("Amal", Couleur.BLANC, 0)
        self.joueur_courant = self.joueur1

    def switch_joueur (self) :
            if self.joueur_courant == self.joueur1 :
                self.joueur_courant = self.joueur2
            else : 
                self.joueur_courant = self.joueur1
    
    def jeu_terminer(self):
        if self.plateau.plateau_plein():
            return True
        if not self.plateau.peu_jouer(self.joueur1) and \
            not self.plateau.peu_jouer(self.joueur2):
            return True

        return False
         
    def jouer(self):
        
        while not self.jeu_terminer():
            if not self.plateau.peu_jouer(self.joueur_courant):
                print(f"{self.joueur_courant.nom} ne peut pas jouer. Il passe son tour.")
                self.switch_joueur()
                continue
            coup_valide = False

            while not coup_valide:
                x, y = self.joueur_courant.choisir_case()
                if self.plateau.coup_jouable(x, y, self.joueur_courant):
                    
                    self.plateau.poser_pion(x, y, self.joueur_courant)
                    coup_valide = True
           
                else:
                    print("Coup non jouable, choisissez une autre case.")
            
            if self.jeu_terminer():
                break
            
            self.switch_joueur()
            
        print("Jeu terminé !")
        
    def afficher_resultat(self):
        
        print(f"Score de {self.joueur1.nom} : {self.joueur1.score}")
        print(f"Score de {self.joueur2.nom} : {self.joueur2.score}")

        if self.joueur1.score > self.joueur2.score:
            print(f"{self.joueur1.nom} a gagné !")
        elif self.joueur2.score > self.joueur1.score:
            print(f"{self.joueur2.nom} a gagné !")
        else:
            print("Match nul !")
                        