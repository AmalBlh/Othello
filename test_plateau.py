from plateau import Plateau
from case import Case, Couleur
import unittest

class TestPlateau(unittest.TestCase):

    def test_init_nombre_colonne(self):
        plateau = Plateau()
        for i in range(8):
            self.assertEqual(len(plateau.get_ligne(i)), 8)

    def test_init_nombre_ligne(self):
        plateau = Plateau()
        for j in range(8):
            self.assertEqual(len(plateau.get_colonne(j)), 8)
    
    def test_init_cases_vides(self):
        plateau = Plateau()
        for i in range(8):
            for j in range(8):
                ma_case = plateau.get_case(i, j)
                self.assertEqual(ma_case.get_stat(), Couleur.VIDE)

    def test_init_get_case_error(self):
        plateau = Plateau()
        with self.assertRaises(ValueError):
            plateau.get_case(-1,1)

        with self.assertRaises(ValueError):
            plateau.get_case(13,0)

        with self.assertRaises(TypeError):
            plateau.get_case("1",0)

    def test_init_get_case(self):
        plateau = Plateau()
        for i in range(8):
            for j in range(8):
                ma_case = plateau.get_case(i,j)
                ma_case.set_pawn(Couleur.NOIR)
                self.assertEqual(plateau.get_case(i,j).get_stat(), Couleur.NOIR)

    def test_get_ligne_error(self):
        plateau = Plateau()

        with self.assertRaises(ValueError):
            plateau.get_ligne(-1)

        with self.assertRaises(ValueError):
            plateau.get_ligne(8)

        with self.assertRaises(TypeError):
            plateau.get_ligne("3")

        with self.assertRaises(TypeError):
            plateau.get_ligne(1.5)


    def test_get_ligne(self):
        plateau = Plateau()
        ligne = plateau.get_ligne(3)

        self.assertEqual(len(ligne), 8)
        self.assertEqual(ligne[0].get_x(), 3)
        self.assertEqual(ligne[0].get_y(), 0)
        self.assertEqual(ligne[7].get_x(), 3)
        self.assertEqual(ligne[7].get_y(), 7)

    def test_get_colonne_error(self):
        plateau = Plateau()

        with self.assertRaises(ValueError):
            plateau.get_colonne(-1)

        with self.assertRaises(ValueError):
            plateau.get_colonne(8)

        with self.assertRaises(TypeError):
            plateau.get_colonne("3")

        with self.assertRaises(TypeError):
            plateau.get_colonne(1.5)


    def test_get_colonne(self):
        plateau = Plateau()
        colonne = plateau.get_colonne(3)

        self.assertEqual(len(colonne), 8)
        self.assertEqual(colonne[0].get_x(), 0)
        self.assertEqual(colonne[0].get_y(), 3)
        self.assertEqual(colonne[7].get_x(), 7)
        self.assertEqual(colonne[7].get_y(), 3)

if __name__ == "__main__":
    unittest.main()


#Commande de test : python -m unittest -v test_plateau.py