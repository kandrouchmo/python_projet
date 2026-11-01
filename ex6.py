psodoname=input("white youre name psodoname")
mainname="mohammed@gmail.com"
passeword=input("white the password please:")
def test_double(x):
    if len(x)==1:
        return x
    if x[0]==x[1]:
        return test_double(x[1:])
    return x[0]+test_double(x[1:])
test=4
while mainname!=passeword :
    print(f"the password it not correct {'last'if test ==0 else test} !")
    test-=1
    passeword=input("white the password please:")
    if test==0:
        print(f"sorry you cant trais again! {test}")
        break
else :
    # print(f"hello {mainname[mainname.index('@')+1:mainname.index('.com')]}")
    print(f"hello {passeword[passeword.index("@")+1:passeword.index(".com")]}")
print(test_double(psodoname))
print(test_double(mainname))
print(test_double(passeword))
