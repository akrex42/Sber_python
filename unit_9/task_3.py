str_list = input("Введите список:\n")
list1 = str_list.split(', ')
list2 = []
i = 0
j = 0
k = 0
minim = int(list1[0])
maxim = int(list1[0])
while i < len(list1):
    if int(list1[i]) < minim:
        minim = int(list1[i])
        j = i
    if int(list1[i]) > maxim:
        maxim = int(list1[i])
        k = i
    i += 1
print(list2)
