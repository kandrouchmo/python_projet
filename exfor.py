numbers = input("Write the number: ") 
list_of_numbers = [int(numbers)]
for x in range(list_of_numbers):
    if x % 2 == 0 :
     print(f"the {x} is even .")
     print(f"the even number liste {list_of_numbers[x]}")
