# # # a=int(input("entrer la valeur du tableau de multiplication :"))
# # # if a % 2 ==0:

# # #     print (f"la somme de {a} est paire")
# # # else :
# # #     print(f"la somme de {a} est impaire")
# def double (x):
#     return x*2

# nombres = [3, 7, 10, 5]
# resultat=map(double,nombres)
# print(list(resultat))
# # def checknum(num):

# #     if num > 10:
# #         return(num)#ic je demande si num est supperieur de 10 ila me rent la valeur de num qui est une variable local 
# # mylist=[1,10,22,33,2,1,0]
# # resultat=filter(checknum,mylist)#ici la valeur que la fonction me fais retourner je le filtre avec la fonction filter quand elle true 
# # print(list(resultat))
# def multiplication (x):
#     return x*20
# mylist=[1,2,3,4,5,6,7,8]
# multi=map(lambda x :x*20 print(f"- {x}") ,mylist)
# print(list(multi))
mylist=["oussama","khalid","hana","souhail"]
mylistbis=enumerate(mylist)
for x,y in mylistbis:
    print(f"{x}-{y}")
    if x ==1:
        break 