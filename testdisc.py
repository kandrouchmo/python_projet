# testdisc = {
#     "Html": "90%",
#     "Css": "80%",
#     "PHP": "70%",
#     "JS": "80%",
#     "Python": "90%",
# }

# for x in testdisc:
#     print(f"the programme is : {x} and youre skills is : {testdisc.get(x)}")
################################################################################################################################################
# peoples = {
# "Osama": #  (x) prend la valeur du nom du disc 
#  {
# "Html": "70%", #skill prend la valeur du key de chaque non du disc (osama)
# "Css": "80%",# peoples[x][skill] retourne la valeur de key qui est (skill) de chaque nom du disc (x) du disc principal (peoples)
# "Js": "70%"
# },
# "Ahmed": #  (x) prend la valeur du nom du disc 
# {
# "Html": "90%", #skill prend la valeur du key de chaque non du disc (ahmed)
# "Css": "80%", # peoples[x][skill] retourne la valeur de key qui est (skill) de chaque nom du disc (x) du disc principal (peoples)
# "Js": "90%" 
# },
# "Sayed": #  (x) prend la valeur du nom du disc 
# {
# "Html": "70%", #skill prend la valeur du key de chaque non du disc (sayed)
# "Css": "60%",# peoples[x][skill] retourne la valeur de key qui est (skill) de chaque nom du disc (x) du disc principal (peoples)
# "Js": "90%"
# },
# }
# for x in peoples:
#     print(f"Skills and Progress For {x} Is: ")

#     for skill in peoples [x]:
#             print(f"{skill} => {peoples[x] [skill]}")
x= { 
"beta-1" :{
    "test1":"80%",
    "test2":"20%",
    "test3":"30%"},
"beta-2" :{
    "test1":"80%",
    "test2":"20%",
    "test3":"30%"},
"beta-3" :{
    "test1":"80%",
    "test2":"20%",
    "test3":"30%"},
}
# for name in x :
#     print(f"the {name}")
#     for skill in x[name]:
#         print(f"skill is : {skill}")
#         print(f"and the value of skill is : {x[name][skill]}")
for key1,value1 in x.items(): # key1 represente le nom du disc qui se trouve dans le variable (x) , et value1 represente la valeur de beta-1
    print(f"give me {key1}")
    for key2,value2 in value1.items():#key2 , value2 represente la meme chose que key1 value1 pour faire la boucle en a besoin de associer les variable key2,value2 au resultat de notre key1 qui represente un disc qui est en meme temps le resultat de x 
        print(f"{key2}---->{value2}") #.items() fais retourner la valeur du variable en question sous forme dobjet paire (x,y) et le poser dans une tuple
