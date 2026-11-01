import csv

file = open("../Documents/users.csv", "rt")
a = csv.reader(file, delimiter=";")

# l'ecture de document csv (chaque enregistrement se convert en liste)
for x in a:
    print(x)

print("------------------------------")

# Manipulation d'affichage selon la demande (id, nom, prenom, age, email)
file = open("../Documents/users.csv", "rt")
a = csv.reader(file, delimiter=";")

i = 0
for x in a:
    if(i > 0):
        print(x[0] +'   '+ x[1] +'   '+ x[2] +'   '+ x[3] +'   '+ x[4])
    i += 1

print("------------------------------")
# L'affichage des utlisateur qui on un email professionnel de l'ofppt

file = open("../Documents/users.csv", "rt")
a = csv.reader(file, delimiter=";")

i = 0
for x in a:
    if(i > 0 and x[4].find("ofppt") > -1):
        print(x[0] +'   '+ x[1] +'   '+ x[2] +'   '+ x[3] +'   '+ x[4])
    i += 1