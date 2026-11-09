from plateau import Plateau
from case import Couleur
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
                if (i, j) not in [(3, 3), (3, 4), (4, 3), (4, 4)]:
                    ma_case = plateau.get_case(i, j)
                    self.assertEqual(ma_case.get_stat(), Couleur.VIDE)

    def test_init_pions_centraux(self):
        plateau = Plateau()

        self.assertEqual(plateau.get_case(3, 3).get_stat(), Couleur.BLANC)
        self.assertEqual(plateau.get_case(3, 4).get_stat(), Couleur.NOIR)
        self.assertEqual(plateau.get_case(4, 3).get_stat(), Couleur.NOIR)
        self.assertEqual(plateau.get_case(4, 4).get_stat(), Couleur.BLANC)

    def test_init_get_case_error(self):
        plateau = Plateau()

        with self.assertRaises(ValueError):
            plateau.get_case(-1, 1)

        with self.assertRaises(ValueError):
            plateau.get_case(13, 0)

        with self.assertRaises(TypeError):
            plateau.get_case("1", 0)

    def test_init_get_case(self):
        plateau = Plateau()

        for i in range(8):
            for j in range(8):
                ma_case = plateau.get_case(i, j)

                if ma_case.get_stat() == Couleur.VIDE:
                    ma_case.set_pawn(Couleur.NOIR)

                    self.assertEqual(
                        plateau.get_case(i, j).get_stat(),
                        Couleur.NOIR
                    )

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

    def test_coup_jouable_initial_noir(self):
        plateau = Plateau()

        coups_valides = [(2, 3), (3, 2), (4, 5), (5, 4)]

        for x, y in coups_valides:
            self.assertTrue(plateau.coup_jouable(x, y, Couleur.NOIR))


    def test_coup_jouable_initial_blanc(self):
        plateau = Plateau()

        coups_valides = [(2, 4), (3, 5), (4, 2), (5, 3)]

        for x, y in coups_valides:
            self.assertTrue(plateau.coup_jouable(x, y, Couleur.BLANC))


    def test_coup_non_jouable(self):
        plateau = Plateau()

        self.assertFalse(plateau.coup_jouable(0, 0, Couleur.NOIR))
        self.assertFalse(plateau.coup_jouable(3, 3, Couleur.NOIR))


    def test_coup_jouable_erreurs(self):
        plateau = Plateau()

        with self.assertRaises(TypeError):
            plateau.coup_jouable(2, 3, "NOIR")

        with self.assertRaises(ValueError):
            plateau.coup_jouable(2, 3, Couleur.VIDE)

        with self.assertRaises(ValueError):
            plateau.coup_jouable(8, 3, Couleur.NOIR)

        with self.assertRaises(TypeError):
            plateau.coup_jouable("2", 3, Couleur.NOIR)

    def test_capture_direction_initial(self):
        plateau = Plateau()

        self.assertTrue(
            plateau.capture_direction(2, 3, 1, 0, Couleur.NOIR)
        )

        self.assertTrue(
            plateau.capture_direction(2, 4, 1, 0, Couleur.BLANC)
        )


    def test_capture_direction_sans_capture(self):
        plateau = Plateau()

        self.assertFalse(
            plateau.capture_direction(0, 0, 1, 0, Couleur.NOIR)
        )

        self.assertFalse(
            plateau.capture_direction(2, 3, -1, 0, Couleur.NOIR)
        )


if __name__ == "__main__":
    unittest.main()