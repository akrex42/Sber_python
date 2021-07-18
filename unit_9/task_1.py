
str_list = input("Введите список:\n")
list1 = str_list.split(', ')
i = 1
while i < len(list1):
    list1.pop(i)
    i += 1
list2 = list1.copy()
print(list2)
