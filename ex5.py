liste_of_website=[]
maxwebsite = 5
while maxwebsite > 0:
    web=input("Write the best website you want to add to your list:")
    liste_of_website.append(f"https//:{web}")
    maxwebsite -= 1
    print(f"You have successfully added the website, and you have {maxwebsite} left.")
    print(liste_of_website)
else :
    print(f"You can't add more, you have {maxwebsite} places left.")
    x=0
    if len(liste_of_website) > 0 :
        while x < (len(liste_of_website)): #On peut aussi utiliser une boucle while (tant que) en initialisant le compteur, en définissant la condition, puis en l'incrémentant à chaque itération. Cependant, une boucle for (pour) est plus pratique dans ce cas.
            print(f"#{x}/ {liste_of_website[x]}")
            x+=1
    clear=input("If you want to clear the list, write 'clear':")
    if clear == "clear":
        liste_of_website.clear()
        maxwebsite=5
        print(f"The list is cleared. {liste_of_website}")
        print(f"You have {maxwebsite} places!")
    else :
        print("You wrote the incorrect word, can you repeat?")
        clear=input("If you want to clear the list, write 'clear':")
        if clear == "clear":
            liste_of_website.clear()
            maxwebsite=5
            print(f"The list is cleared. {liste_of_website}")
            print(f"You have {maxwebsite} places!")
     #On peut aussi utiliser une boucle while (tant que) en initialisant le compteur, en définissant la condition, puis en l'incrémentant à chaque itération. Cependant, une boucle for (pour) est plus pratique dans ce cas.
        #     if len(liste_of_website) > 0 :
        # for x in range(len(liste_of_website)): #On peut aussi utiliser une boucle while (tant que) en initialisant le compteur, en définissant la condition, puis en l'incrémentant à chaque itération. Cependant, une boucle for (pour) est plus pratique dans ce cas.
        #     print(f"#{x}/ {liste_of_website[x]}")