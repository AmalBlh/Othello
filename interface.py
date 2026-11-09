
import tkinter as tk
from tkinter import messagebox

from jeu import Jeu
from case import Couleur


class OthelloGUI:

    def __init__(self):
        self.jeu = Jeu()

        self.root = tk.Tk()
        self.root.title("Jeu Othello")
        self.root.geometry("650x650")
        self.root.configure(bg="#eeeeee")

        # Titre
        titre = tk.Label(
            self.root,
            text="OTHELLO",
            font=("Arial", 24, "bold"),
            bg="#eeeeee"
        )
        titre.pack(pady=15)

        # Informations des joueurs
        self.info = tk.Label(
            self.root,
            text="",
            font=("Arial", 14),
            bg="#eeeeee"
        )
        self.info.pack(pady=10)

        # Plateau graphique
        self.frame_plateau = tk.Frame(
            self.root,
            bg="#006400",
            padx=5,
            pady=5
        )
        self.frame_plateau.pack()

        self.boutons = []

        for i in range(8):
            ligne = []

            for j in range(8):
                bouton = tk.Button(
                    self.frame_plateau,
                    width=5,
                    height=2,
                    font=("Arial", 20),
                    bg="#228B22",
                    command=lambda x=i, y=j: self.cliquer_case(x, y)
                )

                bouton.grid(row=i, column=j, padx=2, pady=2)
                ligne.append(bouton)

            self.boutons.append(ligne)

        # Message de jeu
        self.message = tk.Label(
            self.root,
            text="",
            font=("Arial", 12),
            bg="#eeeeee"
        )
        self.message.pack(pady=15)

        self.actualiser_plateau()

        self.root.mainloop()

    def actualiser_plateau(self):

        for i in range(8):
            for j in range(8):

                case = self.jeu.plateau.get_case(i, j)
                couleur = case.get_stat()

                if couleur == Couleur.NOIR:
                    texte = "●"
                    couleur_texte = "black"

                elif couleur == Couleur.BLANC:
                    texte = "●"
                    couleur_texte = "white"

                else:
                    texte = ""
                    couleur_texte = "black"

                self.boutons[i][j].config(
                    text=texte,
                    fg=couleur_texte
                )

        score_noir, score_blanc = self.jeu.plateau.calculer_score()

        self.info.config(
            text=(
                f"Noir : {score_noir}     "
                f"Blanc : {score_blanc}     "
                f"Tour : {self.jeu.joueur_courant.nom}"
            )
        )

    def cliquer_case(self, x, y):

        valide, message = self.jeu.jouer_coup_interface(x, y)

        self.message.config(text=message)

        if not valide:
            return

        self.actualiser_plateau()

        if self.jeu.jeu_terminer():
            self.terminer_partie()

    def terminer_partie(self):

        score_noir, score_blanc = self.jeu.plateau.calculer_score()

        self.jeu.joueur1.score = score_noir
        self.jeu.joueur2.score = score_blanc

        if score_noir > score_blanc:
            gagnant = "Noir a gagné !"
        elif score_blanc > score_noir:
            gagnant = "Blanc a gagné !"
        else:
            gagnant = "Match nul !"

        messagebox.showinfo(
            "Fin de partie",
            f"Score Noir : {score_noir}\n"
            f"Score Blanc : {score_blanc}\n\n"
            f"{gagnant}"
        )

        for ligne in self.boutons:
            for bouton in ligne:
                bouton.config(state="disabled")


if __name__ == "__main__":
    OthelloGUI()
