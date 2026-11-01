import csv


# ----- Creation et remplissage fichier CSV : -----
myfile =  open("fichierCSV.csv", "w")
myfile.write("Hello CSV, How are you?, Nice to see you")
myfile.close()

# ----- Lecture du contenu du fichier avec la methode reader() : -----
myfile = open("fichierCSV.csv", "rt")
lecteurCSV = csv.reader(myfile, delimiter=",")
for ligne in lecteurCSV :
    print(ligne)
myfile.close()

#############################################################

# ----- Creation et remplissage fichier CSV : -----
csvFile = open("file.csv", "wt")
ecrivainCSV = csv.writer(csvFile, delimiter=";")
ecrivainCSV.writerow(["Nom", "Prenom", "Telephone"])
ecrivainCSV.writerow(["Elfquieh", "Youssef", "0606969696"])
ecrivainCSV.writerow(["Kandrouch", "Mohamed", "0607696969"])
csvFile.close()

# ----- Methode 1 : read sous format list -----
csvFile = open("file.csv", "rt")
lecteurCSV = csv.reader(csvFile, delimiter=";")
for ligne in lecteurCSV :
    print(ligne)
csvFile.close()

# ----- Methode 2 : read sous format Dict -----
csvFile = open("file.csv", "rt")
lecteurCSV = csv.DictReader(csvFile, delimiter=";")
for ligne in lecteurCSV :
    print(ligne)
csvFile.close()

############################################################