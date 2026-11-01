class personne:
    def __init__(self,nom,cin,annes):
        self.nom=nom
        self.cin=cin
        self.annes=annes
    def age(self,annes_actuelle):
        return annes_actuelle-self.annes 
class etudiant(personne):
    def __init__(self,nom,cin,annes,note1,note2):
        super(). __init__(nom,cin,annes)
        self.note1=note1
        self.note2=note2
    def moyenne(self):
        return(self.note1+self.note2)/2
class employe(personne):
    def __init__(self,nom,cin,annes,nb_hr,pr_hr):
        super(). __init__(nom,cin,annes)
        self.nb_hr=nb_hr
        self.pr_hr=pr_hr
    def salaire(self):
        return self.nb_hr*self.pr_hr
    
#pour enter les variable declarer au debut pour personne (si tu veux changer qlq chose tu dois la changer par ici)
#de preferance de changer le nom de la class de selui de lobjet pour quil nya pas de confusion
Personne =personne ("mk","age",(1997)) 
print(f"lage est {Personne.nom}:{Personne.age(2025)}:{Personne.cin}") 
Etudiant =etudiant ("mohhamed","AE173316",(1997),(17),(18))
print(f"la note de letudiant {Etudiant.nom}:{Etudiant.moyenne()}")
Employe=employe("mohammed","AE173316",(1998),(12),(16))
print(f"les nombres dheure sont {Employe.nom}:{Employe.salaire()}")
