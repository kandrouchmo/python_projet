word=input("white the word please :")
nom=input("white the nom please :")
def test_double(x): #(x) paramerte
    if len(x)==1: # task
        return x
    if x[0]==x[1]:
        # print(f"valeu befor slasing {word}")
        return test_double(x[1:])
    # print(f"valeu befor slasing {word}")
    return x[0]+test_double(x[1:])
print (test_double(word))   #(argument)
print (test_double(nom))    #(argument)

