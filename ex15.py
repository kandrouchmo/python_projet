# import os 
# print(os.getcwd)
# print(os.path.abspath(__file__))
# total=int(input("Entrez le nombre de lignes que vous voulez remplir : \n"))
# myfile=open(r"c:\Users\DELL\Downloads\OneDrive\Bureau\TP Python\ficherdexdecrice.txt","w")
# for i in range(total):
#     ligne=str(input(f"--> ligne {i+1} : \n"))
#     myfile.write(ligne+"\n")
# myfile.close()


# if os.path.exists(r"c:\Users\DELL\Downloads\OneDrive\Bureau\TP Python\ficherdexdecrice.txt"):
#     os.remove(r"c:\Users\DELL\Downloads\OneDrive\Bureau\TP Python\ficherdexdecrice.txt")
#     print("Fichier supprimé avec succès.")
# else:
#     print("Le fichier n'existe pas.")

#<------------------------------------------------------next stup ex 3------------------------------------------------------------------------------------------->
# maliste=[1,2,2,2,3,4,55,6,7]
# def elements_uniques(x):
#     y= []
#     for i in x:
#         if x.count(i) == 1:
#             y.append(i)
#     return y
# print(elements_uniques(maliste))
#<------------------------------------------------------next stup ex 2 ------------------------------------------------------------------------------------------->
# prix_du_bien=(400000)
# budgetinteret=float(3.6)
# duree=int(25)

# def calcule_du_bien(x,y,z):
#     total_credit=(x*(y*z))/100
#     return total_credit

# print(calcule_du_bien(prix_du_bien,budgetinteret,duree))
#<------------------------------------------------------next stup ex 1 ------------------------------------------------------------------------------------------->
# Début

#     somme ← 0
#     Pour i de 0 à N-1 faire
#         somme ← somme + T[i]
#     FinPour
#     moyenne ← somme / N
#     N1 ← 0
#     N2 ← 0
#     Pour i de 0 à N-1 faire
#         Si T[i] > moyenne alors
#             N1+=1
#             T1 ← T[i]
#         Sinon
#             N2 += 1 
#             T2 ← T[i]
#         FinSi
#     FinPour
#<------------------------------------------------------next stup ex 1 ------------------------------------------------------------------------------------------->

# maliste=[1,2,2,2,3,4,55,6,7]
# def elements_uniques(x):
#     y= []
#     for i in x:
#         if x.count(i) == 1:
#             y.append(i)
#     return y
# print(elements_uniques(maliste))
##<------------------------------------------------------un test rapide ------------------------------------------------------------------------------------------->

import os 
print(os.getcwd)
print(os.path.abspath(__file__))
ttligne=int(input("combien de ligne vouler vous ecrire :"))
myfile=open(r"c:\Users\DELL\Downloads\OneDrive\Bureau\TP Python\ficherdexdecrice.txt","w")
for i in range (ttligne):
    ligne=str(input(f"ligne {i+1} :"))
    myfile.write(ligne+"\n")
myfile.close()

if os.path.exists(r"c:\Users\DELL\Downloads\OneDrive\Bureau\TP Python\ficherdexdecrice.txt"):
    os.remove(r"c:\Users\DELL\Downloads\OneDrive\Bureau\TP Python\ficherdexdecrice.txt")
    print("le fichier est bien suprimer !")
else:
    print("fichier intruvable !!")
##<------------------------------------------------------un test rapide ------------------------------------------------------------------------------------------->
