class FeuDeSignalisation:
    def __init__(self):
        self.couleur = 1  # Initialise couleur à 1

    def change(self):
        self.couleur += 1
        if self.couleur == 4:
            self.couleur = 1

# Exemple d'utilisation de la classe
feu = FeuDeSignalisation()
print(feu.couleur)  # Affiche la couleur initiale
feu.change()
print(feu.couleur)  # Affiche la couleur après changement
