myFile = open(r"C:\Users\DELL\Downloads\OneDrive\Bureau\TP Python\tsesst.txt", "r")
print(myFile) # File Data Object
print(myFile.name)
print(myFile.mode)
print(myFile.encoding)

print(myFile.read(10))
# # myfile.reders()
# myFile.write("hellsssso"*50)
# x=[1,2,3,4,5,[]]
# if any(x):
#     print("your list is true")
# else:
#     print("one or all element is not true")