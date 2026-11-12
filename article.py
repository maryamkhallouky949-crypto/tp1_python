
class Article:

    def __init__(self, reference: str, designation: str,
                 prix_ht: float, stock: int):

        self.reference = reference
        self.designation = designation
        self.prix_ht = prix_ht
        self.stock = stock

    def valeur_stock(self) -> float:
        return self.prix_ht * self.stock

    def ajouter_stock(self, quantite: int):
        if quantite < 0:
            raise ValueError("La quantité ne peut pas être négative.")

        self.stock += quantite

    def __str__(self):
        return f"[{self.reference}] {self.designation} - Stock : {self.stock} - Prix HT : {self.prix_ht:.2f} DH"

a1 = Article("REF-001", "Clavier Mécanique", 89.99, 10)

print("Valeur du stock :", a1.valeur_stock())

a1.ajouter_stock(5)

print(a1)
try:
    a1.ajouter_stock(-3)
except ValueError as e:
    print("Erreur :", e)
