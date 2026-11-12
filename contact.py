
class Contact:

    def __init__(self, nom: str, telephone: str, email: str):
        self.nom = nom
        self.telephone = telephone
        self.email = email

    @property
    def initiale(self):
        return self.nom[0].upper() if self.nom else ""

    def __repr__(self):
        return f"Contact(nom='{self.nom}', email='{self.email}')"


class Carnet:

    def __init__(self):
        self.contacts = []

    def ajouter(self, contact: Contact):
        self.contacts.append(contact)

    def chercher(self, nom_partiel: str) -> list:
        nom_partiel_lower = nom_partiel.lower()

        return [
            c for c in self.contacts
            if nom_partiel_lower in c.nom.lower()
        ]

    def __len__(self):
        return len(self.contacts)



carnet = Carnet()

c1 = Contact("Younness SARHAT", "0618945678", "youness@example.com")
c2 = Contact("MARYAM HAFIDI", "0698855432", "maryam@example.com")

carnet.ajouter(c1)
carnet.ajouter(c2)

print("Initiale :", c1.initiale)

resultats = carnet.chercher("YOUNNESS")

print("Résultats :", resultats)

print("Nombre de contacts :", len(carnet))
