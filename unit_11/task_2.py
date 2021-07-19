dict1 = eval(input("Enter the dictionary:\n"))
item = input("Enter the value:\n")
for key, value in dict1.items():
    if item == str(value):
        print(key)

#  should an item be surrounded by quotes while reading with input?
