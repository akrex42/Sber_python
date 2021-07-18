str_list = input("Enter the list:\n")
list1 = str_list.split(', ')
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
list1.pop(j)
list1.insert(j, str(maxim))
list1.pop(k)
list1.insert(k, str(minim))

# could use remove instead

print(list1)
