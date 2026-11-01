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
lecteurCSV = csv.DictReader(fichier, delimiter=";")
listeStagiaires = list(lecteurCSV)

# AFFICHAGE DES INFOS DE CHAQUE STAGIAIRE :

print("Affichage des infos de chaque stagiaire :")
for element in listeStagiaires :
    nom = element.get("Nom")
    prenom = element.get("Prenom")
    age = element["Age"]
    note = element["Note"]
    print(f" - {nom} {prenom} | age : {age} | note obtenu : {note}/20")

print("=" * 60)

# CREATION ET AFFICHAGE D'UNE LISTE DES STAGIAIRES REUSSI :

listeReussi = []
print("Liste des stagiaire qui ont reussi :")
for element in listeStagiaires :
    nom = element["Nom"]
    prenom = element["Prenom"]
    note = element["Note"]
    if int(note) >= 10 :
        listeReussi.append(nom + " " + prenom)

print(listeReussi)

print("=" * 60)

# CREATION ET AFFICHANGE D'UNE LISTE DES STAGIAIRE SUP A LA MOYENNE :

sommeNotes = 0
moyenne = 0
compteur = 0
supMoyenne = []

for element in listeStagiaires :
    note = element["Note"]
    compteur += 1
    sommeNotes += int(note)

moyenne += sommeNotes / compteur
print(f"La note moyenne de la classe est : {moyenne}/20")

print("Liste des stagiaires ayaynt un note superieur a la moyenne :")

for element in listeStagiaires :
    nom = element["Nom"]
    prenom = element["Prenom"]
    note = element["Note"]
    if int(note) >= moyenne :
        supMoyenne.append(nom + " " + prenom + " : " + note +"/20")

print(supMoyenne)