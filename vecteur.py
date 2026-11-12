
class Vecteur2D:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, autre):
        return Vecteur2D(
            self.x + autre.x,
            self.y + autre.y
        )

    def __sub__(self, autre):
        return Vecteur2D(
            self.x - autre.x,
            self.y - autre.y
        )

    def __mul__(self, scalaire: float):
        return Vecteur2D(
            self.x * scalaire,
            self.y * scalaire
        )

    def __eq__(self, autre: object) -> bool:

        if not isinstance(autre, Vecteur2D):
            return False

        return self.x == autre.x and self.y == autre.y

    def __repr__(self):
        return f"Vecteur2D({self.x}, {self.y})"


v1 = Vecteur2D(1, 2)
v2 = Vecteur2D(3, 4)


v3 = v1 + v2
print("Addition :", v3)

v4 = v2 - v1
print("Soustraction :", v4)

v5 = v1 * 2
print("Multiplication :", v5)

print("Égalité :", v1 == Vecteur2D(1, 2))
