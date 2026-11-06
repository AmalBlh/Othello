from case import Case, Couleur

class Plateau:
    def __init__(self):
        board = []
        for i in range(8):
            line = []

            for j in range(8):
                line.append(Case(i,j, Couleur.VIDE))

            board.append(line)

        self.__board = board

    def get_case(self, x, y):
        if not (isinstance(x, int) and isinstance(y, int)):
            raise TypeError("Les coordonnées doivent être des entiers")
        elif not (0 <= x <= 7 and 0 <= y <= 7):
            raise ValueError("Les coordonnées doivent être comprises entre 0 et 7")

        else:
            return self.__board[x][y]

    def get_ligne(self, x):
        if not isinstance(x, int):
            raise TypeError("La ligne doit être un entier")
        elif not (0 <= x <= 7):
            raise ValueError("La ligne doit être comprise entre 0 et 7")
        else:
            line = self.__board[x]
            return line

    def get_colonne(self, y):
        if not isinstance(y, int):
            raise TypeError("La colonne doit être un entier")
        elif not (0 <= y <= 7):
            raise ValueError("La colonne doit être comprise entre 0 et 7")
        else:
            col = []
            for i in range(8):
                case = self.__board[i][y]
                col.append(case)
            return col