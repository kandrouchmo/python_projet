# from datetime import datetime
# class etrehumain:
#     def __init__(self,yeux,peau):
#         self.yeux=yeux
#         self.peau=peau
#     def respiration(self):
#         return "done"
# class personne(etrehumain):
#     def __init__(self, yeux, peau,nom,cin,naissance):
#         super().__init__(yeux, peau)
#         self.nom=nom
#         self.cin=cin
#         self.naissance=naissance
#     def age(self):
#         return datetime.now().year-datetime.strptime(self.naissance,"%d/%m/%Y").year
# class Etudiant (personne):
#     def __init__(self, yeux, peau, nom, cin, naissance,note1,note2):
#         super().__init__(yeux, peau, nom, cin, naissance)
#         self.note1=note1
#         self.note2=note2
#     def moyenne(self):
#         return (self.note1 +self.note2)/2
# etudiant=Etudiant (
#     nom="Mohmmed",
#     cin="AE173316",
#     yeux="marron",
#     peau="blanc",
#     naissance="10/01/1997",
#     note1=18,
#     note2=16,
# )
# print(f"le nom de letudiant: {etudiant.nom}")
# print(f"la CIN de letudiant: {etudiant.cin}")
# print(f"la couleur des yeux de letudiant: {etudiant.yeux}")
# print(f"la couleur de la peau de letudiant: {etudiant.peau}")
# print(f"l'age de letudiant: {etudiant.age()}")
# print(f"la moyenne de letudiant: {etudiant.moyenne()}")
# print(f"la fonction de letudiant: {etudiant.respiration()}")
# variable1= ["one","two",1,  True]

# print(variable1.pop(3))
variable2= {"one","tree",1.52,True}
print(type(variable2))
# print(variable2[0:3])
variable2.clear()
print(variable2)