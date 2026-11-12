
from dataclasses import dataclass, field
from typing import List


@dataclass
class Produit:

    nom: str
    prix: float
    quantite: int = 0
    tags: List[str] = field(default_factory=list)

    def valeur_totale(self) -> float:
        return self.prix * self.quantite


p1 = Produit(
    "thé",
    6.5,
    10,
    ["boisson", "chaud"]
)

p2 = Produit(
    "thé",
    5.5,
    10,
    ["boisson", "chaud"]
)

p3 = Produit("café", 3.0)


print(p1)


print("Produits identiques :", p1 == p2)


print("Valeur totale :", p1.valeur_totale())

print("Tags du café:", p3.tags)
