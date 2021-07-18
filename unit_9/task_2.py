
str_list = input("Введите список:\n")
list1 = str_list.split(', ')
list2 = []
i = 0
while i < len(list1) - 1:
    if int(list1[i]) < int(list1[i + 1]):
        list2.append(list1[i + 1])
    i += 1
print(list2)
