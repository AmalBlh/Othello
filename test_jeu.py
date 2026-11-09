import unittest
from unittest.mock import patch
from jeu import Jeu
from joueur import Joueur
from plateau import Plateau
from case import Couleur


class TestJeu(unittest.TestCase):

    def setUp(self):
        self.jeu = Jeu()

    # =================================
    # Tests du constructeur
    # =================================

    def test_init_plateau(self):
        self.assertIsInstance(self.jeu.plateau, Plateau)

    def test_init_joueur1(self):
        self.assertIsInstance(self.jeu.joueur1, Joueur)
        self.assertEqual(self.jeu.joueur1.nom, "Test")
        self.assertEqual(self.jeu.joueur1.couleur, Couleur.NOIR)
        self.assertEqual(self.jeu.joueur1.score, 0)

    def test_init_joueur2(self):
        self.assertIsInstance(self.jeu.joueur2, Joueur)
        self.assertEqual(self.jeu.joueur2.nom, "Amal")
        self.assertEqual(self.jeu.joueur2.couleur, Couleur.BLANC)
        self.assertEqual(self.jeu.joueur2.score, 0)

    def test_init_joueur_courant(self):
        self.assertIs(self.jeu.joueur_courant, self.jeu.joueur1)

    # =================================
    # Tests de switch_joueur()
    # =================================

    def test_switch_joueur1_vers_joueur2(self):
        self.jeu.switch_joueur()

        self.assertIs(self.jeu.joueur_courant, self.jeu.joueur2)

    def test_switch_joueur2_vers_joueur1(self):
        self.jeu.switch_joueur()
        self.jeu.switch_joueur()

        self.assertIs(self.jeu.joueur_courant, self.jeu.joueur1)

    # =================================
    # Tests de jeu_terminer()
    # =================================

    def test_jeu_terminer_plateau_plein(self):
        with patch.object(
            self.jeu.plateau,
            "plateau_plein",
            return_value=True
        ):
            self.assertTrue(self.jeu.jeu_terminer())

    def test_jeu_terminer_aucun_joueur_ne_peut_jouer(self):
        with patch.object(
            self.jeu.plateau,
            "plateau_plein",
            return_value=False
        ), patch.object(
            self.jeu.plateau,
            "peu_jouer",
            return_value=False
        ):
            self.assertTrue(self.jeu.jeu_terminer())

    def test_jeu_non_termine_joueur1_peut_jouer(self):
        with patch.object(
            self.jeu.plateau,
            "plateau_plein",
            return_value=False
        ), patch.object(
            self.jeu.plateau,
            "peu_jouer",
            side_effect=[True, False]
        ):
            self.assertFalse(self.jeu.jeu_terminer())

    def test_jeu_non_termine_joueur2_peut_jouer(self):
        with patch.object(
            self.jeu.plateau,
            "plateau_plein",
            return_value=False
        ), patch.object(
            self.jeu.plateau,
            "peu_jouer",
            side_effect=[False, True]
        ):
            self.assertFalse(self.jeu.jeu_terminer())

    # =================================
    # Tests de afficher_resultat()
    # =================================

    def test_resultat_victoire_joueur1(self):
        self.jeu.joueur1.score = 10
        self.jeu.joueur2.score = 5

        with patch("builtins.print") as mock_print:
            self.jeu.afficher_resultat()

        mock_print.assert_any_call("Test a gagné !")

    def test_resultat_victoire_joueur2(self):
        self.jeu.joueur1.score = 5
        self.jeu.joueur2.score = 10

        with patch("builtins.print") as mock_print:
            self.jeu.afficher_resultat()

        mock_print.assert_any_call("Amal a gagné !")

    def test_resultat_match_nul(self):
        self.jeu.joueur1.score = 10
        self.jeu.joueur2.score = 10

        with patch("builtins.print") as mock_print:
            self.jeu.afficher_resultat()

        mock_print.assert_any_call("Match nul !")

    # =================================
    # Tests de jouer()
    # =================================

    def test_jouer_partie_terminee_immediatement(self):
        with patch.object(
            self.jeu,
            "jeu_terminer",
            return_value=True
        ), patch("builtins.print") as mock_print:

            self.jeu.jouer()

        mock_print.assert_any_call("Jeu terminé !")

    def test_jouer_passage_tour_si_aucun_coup_possible(self):
        with patch.object(
            self.jeu,
            "jeu_terminer",
            side_effect=[False, True]
        ), patch.object(
            self.jeu.plateau,
            "peu_jouer",
            return_value=False
        ), patch.object(
            self.jeu,
            "switch_joueur"
        ) as mock_switch:

            self.jeu.jouer()

        mock_switch.assert_called_once()

    def test_jouer_coup_valide(self):
        with patch.object(
            self.jeu,
            "jeu_terminer",
            side_effect=[False, False, True]
        ), patch.object(
            self.jeu.plateau,
            "peu_jouer",
            return_value=True
        ), patch.object(
            self.jeu.joueur_courant,
            "choisir_case",
            return_value=(2, 3)
        ), patch.object(
            self.jeu.plateau,
            "coup_jouable",
            return_value=True
        ), patch.object(
            self.jeu.plateau,
            "poser_pion"
        ) as mock_poser:

            self.jeu.jouer()

        mock_poser.assert_called_once_with(
            2, 3, self.jeu.joueur1
        )

    def test_jouer_coup_invalide_puis_valide(self):
        with patch.object(
            self.jeu,
            "jeu_terminer",
            side_effect=[False, False, True]
        ), patch.object(
            self.jeu.plateau,
            "peu_jouer",
            return_value=True
        ), patch.object(
            self.jeu.joueur_courant,
            "choisir_case",
            return_value=(2, 3)
        ), patch.object(
            self.jeu.plateau,
            "coup_jouable",
            side_effect=[False, True]
        ), patch.object(
            self.jeu.plateau,
            "poser_pion"
        ) as mock_poser:

            self.jeu.jouer()

        mock_poser.assert_called_once_with(
            2, 3, self.jeu.joueur1
        )


if __name__ == "__main__":
    unittest.main()