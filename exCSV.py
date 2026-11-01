import csv


# CREATION ET REMPLISSAGE DU FICHIER CSV :

myCsvFile = open("info.csv", "wt")
ecrivainCSV = csv.writer(myCsvFile, delimiter=";")
ecrivainCSV.writerow(["Nom", "Prenom", "Age", "Note"])
ecrivainCSV.writerow(["Badraoui", "Raouia", "22", "18"])
ecrivainCSV.writerow(["Malaki", "Salma", "19", "13"])
ecrivainCSV.writerow(["Yassine", "Reda", "19", "6"])
ecrivainCSV.writerow(["Mardoude", "Yassine", "20", "9"])
myCsvFile.close()


# IMPORTATION DU FICHIER ET STOKAGE DANS UNE VARIABLE : 

fichier = open("info.csv", "rt")
lecteurCSV = csv.reader(fichier, delimiter=";")
listeDeDonnees = list(lecteurCSV)

# AFFICHAGE DES INFOS DE CHAQUE STAGIAIRE :

for element in listeDeDonnees:
    if len(element) != 0 :
        print(element)

print("=" * 60)

print("Les informationes de chaque stagiaire :")

for element in listeDeDonnees[1:] :
    if len(element) != 0 :
        fname = element[0]
        lname = element[1]
        age = element[2]
        note = element[3]
        print(f" - {fname} {lname}, {age} ans, sa note est : {note}")

fichier.close()

print("=" * 60)

# CREATION ET AFFICHAGE D'UNE LISTE DES STAGIAIRES REUSSI :

listeReussi = []
for element in listeDeDonnees[1:]:
    if len(element) != 0 :
        if int(element[-1]) >= 10 :
            fname = element[0]
            lname = element[1]
            listeReussi.append(fname + " " + lname)

print("Les stagiaire qui ont reussi sont :")
print(listeReussi)

print("=" * 60)

# CREATION ET AFFICHANGE D'UNE LISTE DES STAGIAIRE SUP A LA MOYENNE :

somNotes = 0
noteMoyenne = 0

for element in listeDeDonnees[1:] :
    if len(element) != 0 :
        fname = element[0]
        lname = element[1]
        age = element[2]
        note = element[3]
        somNotes += int(note)

noteMoyenne += somNotes / 4
print(f"La note moyenne est : {noteMoyenne}")
majorant = []
for element in listeDeDonnees[1:]:
    if len(element) != 0 :
        fname = element[0]
        lname = element[1]
        note = element[3]
        if int(note) >= noteMoyenne :
            majorant.append(fname + " " + lname + " : " + note)

print ("Les stagiaires qui ont eu une note sup a la moyenne sont : ")
print (majorant)
