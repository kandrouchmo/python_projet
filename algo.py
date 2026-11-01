# Programme pour trouver la valeur maximale dans un tableau

# Initialisation du tableau
N = []

# Saisie des 8 entiers
for i in range(1, 9):
    nombre = int(input(f"Entrez l'\u00e9l\u00e9ment num\u00e9ro {i} : "))
    N.append(nombre)

# Initialisation de la valeur maximale
max_val = N[0]

# Recherche de la valeur maximale
for i in range(1, len(N)):
    if N[i] > max_val:
        max_val = N[i]

# Affichage de la valeur maximale
print(f"La valeur maximale du tableau est : {max_val}")
