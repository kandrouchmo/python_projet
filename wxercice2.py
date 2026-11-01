admin = ["mohammed", "nouhaila", "soufiane", "malak"]
name = input("Write your name: ")
if name in admin:
    print(f"Welcome back {name}")
    option = input("Choose your option: 'delete' or 'update': ")
    if option == "update":
        newname = input("Write your new name please for updating the list: ")
        print(f"Thank you for your understanding, {newname}. The list has been updated.")
        admin[admin.index(name)] = newname
        print(admin)
    elif option == "delete":
        admin.remove(name)
        print(admin)
else:
    print("Sorry, the name is wrong.")
    
website = input(f"Write your website {newname}: ")
psudoname = website[website.index(".") + 1:website.index(".com")]

print(f"Your website is: {website} and your pseudoname is: {psudoname}")
