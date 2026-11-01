product_name= "shoompoin"
price= int(90)
country=input("entrer votre country")
student=input("si vous etes etudiant faite yes ou no ")
print(f"parceque vous etes {student}est votre pays est {country}")
if country=="morocco":
    print(f"bonjours{product_name} parceque vous etes de {country}")
    if student== "yes":
     print(f"le produit dans votre pays est dun prix qui ne depasse pas {price-50}$")
    else : 
        print(f"le produit dans votre pays est dun prix qui ne depasse pas {price-30}$")
elif country=="egypte":
    print(f"le produit dans votre pays est dun prix qui ne depasse pas {price-20}$")
else :
 print(f"le prix du produit est {price}$")
