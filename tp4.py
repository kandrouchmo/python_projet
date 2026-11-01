class  personne:
    def __init__(self,nom,cin,annes):
        self.nom=nom
        self.cin=cin
        self.annes=annes
    def age(self,annes_actuelle):
        return annes_actuelle-self.annes
class etudiant(personne):
    def __init__(self,nom,cin,annes,note1,note2):
        super().__init__(nom,cin,annes)
        self.note1=note1
        self.note2=note2
    def moyenne(self):
        return(self.note1-self.note2)/2
class employe(personne):
    def __init__(self,nom,cin,annes,pr_hr,nb_hr):
        super().__init__(nom,cin,annes)
        self.pr_hr=pr_hr
        self.nb_hr=nb_hr
    def salaire(self):
        return self.pr_hr*self.nb_hr

personne=personne ("simo","AE173316",1997) #pour enter les variable declarer au debut pour personne (si tu veux changer qlq chose tu dois la changer par ici)
print(f"ancien Age de {personne.nom}:{personne.cin}:{personne.age(2025)}ans")
etudiant =etudiant ("mohamed","AE173316",(1997),(17),(18))
print(f"la note de letudiant {etudiant.nom}:{etudiant.moyenne()}")
employe=employe("mohammed","AE173316",(1998),(12),(16))
print(f"les nombres dheure sont{employe.nom}:{employe.salaire()}")