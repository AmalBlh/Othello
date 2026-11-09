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

        self.get_case(3,3).set_pawn(Couleur.BLANC)
        self.get_case(3,4).set_pawn(Couleur.NOIR)
        self.get_case(4,3).set_pawn(Couleur.NOIR)
        self.get_case(4,4).set_pawn(Couleur.BLANC)


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

    def coup_jouable(self, x, y, couleur):
        if not isinstance(couleur, Couleur):
            raise TypeError("La couleur du joueur est invalide")
        if couleur == Couleur.VIDE:
            raise ValueError("La couleur demandée ne peut pas être VIDE")
        if not (isinstance(x, int) and isinstance(y, int)):
            raise TypeError("Les coordonnées ne sont pas des entiers")
        if not (0 <= x <= 7 and 0 <= y <= 7):
            raise ValueError("Les coordonnées sont hors plateau")

        current = self.get_case(x, y)

        est_vide = current.get_stat() == Couleur.VIDE

        if not est_vide:
            return False

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue

                if self.capture_direction(x, y, dx, dy, couleur):
                    return True

        return False

    def capture_direction(self, x, y, dx, dy, couleur):
        nx = x + dx
        ny = y + dy

        if couleur == Couleur.NOIR:
            adversaire = Couleur.BLANC
        else:
            adversaire = Couleur.NOIR

        pion_adverse_trouve = False

        while 0 <= nx < 8 and 0 <= ny < 8:
            statut = self.get_case(nx, ny).get_stat()

            if statut == adversaire:
                pion_adverse_trouve = True
                nx += dx
                ny += dy

            elif statut == couleur and pion_adverse_trouve:
                return True

            else:
                return False

        return False

    def cases_flip(self, x, y, couleur):
        cases_flippables = []

        if couleur == Couleur.NOIR:
            adversaire = Couleur.BLANC
        else:
            adversaire = Couleur.NOIR
        
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                if self.capture_direction(x, y, dx, dy, couleur):
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < 8 and 0 <= ny < 8:
                        statut = self.get_case(nx, ny).get_stat()
                        while 0 <= nx < 8 and 0 <= ny < 8 and statut == adversaire:
                            cases_flippables.append(self.get_case(nx, ny))
                            nx += dx
                            ny += dy
                            if 0 <= nx < 8 and 0 <= ny < 8:
                                statut = self.get_case(nx, ny).get_stat()
        return cases_flippables

    def jouer_coup(self, x, y, couleur):
        if self.coup_jouable(x, y, couleur):
            flip = self.cases_flip(x, y, couleur)
            self.get_case(x, y).set_pawn(couleur)

            for jeton in flip:
                jeton.flip()
        else:
            raise ValueError("Le coup n'est pas jouable.")