
from joueur import Joueur
from plateau import Plateau
from case import Couleur

class Jeu:

    def __init__(self):
        self.plateau = Plateau()
        self.joueur1 = Joueur("Noir", Couleur.NOIR, 0)
        self.joueur2 = Joueur("Blanc", Couleur.BLANC, 0)
        self.joueur_courant = self.joueur1

    def switch_joueur(self):
        if self.joueur_courant == self.joueur1:
            self.joueur_courant = self.joueur2
        else:
            self.joueur_courant = self.joueur1

    def jeu_terminer(self):
        if self.plateau.plateau_plein():
            return True

        if (not self.plateau.peu_jouer(self.joueur1.couleur)
                and not self.plateau.peu_jouer(self.joueur2.couleur)):
            return True

        return False

    def jouer(self):

        while not self.jeu_terminer():
            self.plateau.affichage()
            
            if not self.plateau.peu_jouer(self.joueur_courant.couleur):
                print(f"{self.joueur_courant.nom} ne peut pas jouer. Il passe son tour.")
                self.switch_joueur()
                continue

            print(f"C'est le tour de {self.joueur_courant.nom}.")
            coup_valide = False

            while not coup_valide:
                x, y = self.joueur_courant.choisir_case()

                if self.plateau.coup_jouable(
                    x, y, self.joueur_courant.couleur
                ):
                    self.plateau.jouer_coup(
                        x, y, self.joueur_courant.couleur
                    )
                    coup_valide = True

                else:
                    print("Coup non jouable, choisissez une autre case.")

            if self.jeu_terminer():
                break

            self.switch_joueur()

        print("Jeu terminé !")

        score_noir, score_blanc = self.plateau.calculer_score()

        self.joueur1.score = score_noir
        self.joueur2.score = score_blanc

        self.afficher_resultat()

    def jouer_coup_interface(self, x, y):

        couleur = self.joueur_courant.couleur

        if not self.plateau.coup_jouable(x, y, couleur):
            return False, "Coup non jouable !"

        self.plateau.jouer_coup(x, y, couleur)

        if self.jeu_terminer():
            return True, "Partie terminée !"

        self.switch_joueur()

        if not self.plateau.peu_jouer(self.joueur_courant.couleur):
            joueur_passe = self.joueur_courant.nom
            self.switch_joueur()

            return True, f"{joueur_passe} ne peut pas jouer. Il passe son tour."

        return True, ""

    def afficher_resultat(self):

        print(f"Score de {self.joueur1.nom} : {self.joueur1.score}")
        print(f"Score de {self.joueur2.nom} : {self.joueur2.score}")

        if self.joueur1.score > self.joueur2.score:
            print(f"{self.joueur1.nom} a gagné !")
        elif self.joueur2.score > self.joueur1.score:
            print(f"{self.joueur2.nom} a gagné !")
        else:
            print("Match nul !")
