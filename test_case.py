import unittest

from case import Case, Couleur

class TestCase(unittest.TestCase):

    def test_flip_blanc(self):
        case = Case(0, 1, Couleur.BLANC)
        case.flip()
        self.assertEqual(case.get_stat(), Couleur.NOIR)

    def test_flip_noir(self):
        case = Case(1, 2, Couleur.NOIR)
        case.flip()
        self.assertEqual(case.get_stat(), Couleur.BLANC)

    def test_flip_vide(self):
        case = Case(1, 2, Couleur.VIDE)
        with self.assertRaises(ValueError):
            case.flip()
    
    def test_flip_2fois(self):
        case = Case(1, 2, Couleur.NOIR)
        case.flip()
        case.flip()
        self.assertEqual(case.get_stat(), Couleur.NOIR)

    def test_set_pawn_blanc(self):
        case = Case(0, 0, Couleur.VIDE)
        case.set_pawn(Couleur.BLANC)

        self.assertEqual(case.get_stat(), Couleur.BLANC)
    
    def test_set_pawn_noir(self):
        case = Case(0, 0, Couleur.VIDE)
        case.set_pawn(Couleur.NOIR)

        self.assertEqual(case.get_stat(), Couleur.NOIR)

if __name__ == "__main__":
    unittest.main()


#Commande de test : python -m unittest -v test_case.py