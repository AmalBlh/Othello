class Joueur:

    def __init__(self, nom: str, couleur: str, score: int):
        self.nom = nom
        self.couleur = couleur
        self.score = score

    def choisir_case(self):
        """
        Permet au joueur de choisir une case.
        """
        
        case = input("Choisissez une case (exemple 43) : ")

        coordinates = self.convert_coordinates(case)

        if coordinates is not None:
            x, y = coordinates
            print("Ligne :", x)
            print("Colonne :", y)
            return x, y
        else:
            raise ValueError("Coordonnées incorrectes")

    def convert_coordinates(self, position):
        """
        Convertit une position comme 43 en coordonnées Python.
        """

        # position = position.strip().upper()

        if len(position) != 2:
            return None

        column = position[0]
        row = position[1]

        if column not in "12345678":
            return None

        if row not in "12345678":
            return None

        x = int(row) - 1
        y = int(column) - 1
        # y = ord(column) - ord("A")

        return x, y
