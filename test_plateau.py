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



if __name__ == "__main__":
    unittest.main()


#Commande de test : python -m unittest -v test_plateau.py