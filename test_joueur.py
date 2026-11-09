import unittest
from unittest.mock import patch
from joueur import Joueur


class TestJoueur(unittest.TestCase):

    def setUp(self):
        self.joueur = Joueur("Alice", "NOIR", 0)

    # =================================
    # Tests du constructeur
    # =================================

    def test_init_nom(self):
        self.assertEqual(self.joueur.nom, "Alice")

    def test_init_couleur(self):
        self.assertEqual(self.joueur.couleur, "NOIR")

    def test_init_score(self):
        self.assertEqual(self.joueur.score, 0)

    # =================================
    # Tests de convert_coordinates()
    # =================================

    def test_convert_premiere_case(self):
        self.assertEqual(
            self.joueur.convert_coordinates("A1"),
            (0, 0)
        )

    def test_convert_derniere_case(self):
        self.assertEqual(
            self.joueur.convert_coordinates("H8"),
            (7, 7)
        )

    def test_convert_case_centrale(self):
        self.assertEqual(
            self.joueur.convert_coordinates("D4"),
            (3, 3)
        )

    def test_convert_minuscules(self):
        self.assertEqual(
            self.joueur.convert_coordinates("d4"),
            (3, 3)
        )

    def test_convert_espaces(self):
        self.assertEqual(
            self.joueur.convert_coordinates(" D4 "),
            (3, 3)
        )

    def test_convert_colonne_invalide(self):
        self.assertIsNone(
            self.joueur.convert_coordinates("Z4")
        )

    def test_convert_ligne_invalide(self):
        self.assertIsNone(
            self.joueur.convert_coordinates("D9")
        )

    def test_convert_format_trop_long(self):
        self.assertIsNone(
            self.joueur.convert_coordinates("ABC")
        )

    def test_convert_format_trop_court(self):
        self.assertIsNone(
            self.joueur.convert_coordinates("D")
        )

    def test_convert_chaine_vide(self):
        self.assertIsNone(
            self.joueur.convert_coordinates("")
        )

    def test_convert_format_incorrect(self):
        self.assertIsNone(
            self.joueur.convert_coordinates("42")
        )

    # =================================
    # Tests de choisir_case()
    # =================================

    def test_choisir_case_valide(self):
        with patch("builtins.input", return_value="D4"):
            resultat = self.joueur.choisir_case()

        self.assertEqual(resultat, (3, 3))

    def test_choisir_case_minuscule(self):
        with patch("builtins.input", return_value="d4"):
            resultat = self.joueur.choisir_case()

        self.assertEqual(resultat, (3, 3))

    def test_choisir_case_invalide(self):
        with patch("builtins.input", return_value="Z9"):
            resultat = self.joueur.choisir_case()

        self.assertIsNone(resultat)

    def test_choisir_case_format_incorrect(self):
        with patch("builtins.input", return_value="ABC"):
            resultat = self.joueur.choisir_case()

        self.assertIsNone(resultat)


if __name__ == "__main__":
    unittest.main()