
class Convertisseur:

   
    taux_eur_dh = 10.9

    @staticmethod
    def vers_dh(euros: float) -> float:
        return euros * Convertisseur.taux_eur_dh

    @classmethod
    def changer_taux(cls, nouveau_taux: float):

        if nouveau_taux <= 0:
            raise ValueError("Le taux doit être positif.")

        cls.taux_eur_dh = nouveau_taux

    @classmethod
    def depuis_dh(cls, dirhams: float) -> float:
        return dirhams / cls.taux_eur_dh

print("200 euros en DH :", Convertisseur.vers_dh(200))

Convertisseur.changer_taux(12.0)

print("130 DH en euros :", Convertisseur.depuis_dh(130))

conv = Convertisseur()

print("60 euros en DH :", conv.vers_dh(60))
