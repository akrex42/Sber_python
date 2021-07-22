def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + "." + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + "." + i[0][0:letter] + '@company.io')
    return emails

list_of_names = []
list1 = []
flag = 0
file = open("task_file.txt", 'r+w')
# file1 = open("result.txt", 'r+w')
# lines = file1.readlines()
# file1.write(str(file.readlines()[:1]))
# file.close()
# file = open("task_file.txt", 'r+w')
for line in file:
    list1 = line.split(',')
    flag = 0
    # here I should create a cycle to check all the blanks
    for item in list1[1:len(list1)]:
        if list1[1][1:1] == '':
            line = ''
            break
        elif list1[2][1:1] == '':
            line = ''
            break
        elif len(list1[len(list1) - 2]) != 8:
            line = ''
            break
        elif flag == 0:
            list1.append(list1[1][1:len(list1[1])])
            list1.append(list1[2][1:len(list1[2])])
            list_of_names.append(list1)
            list1 = []
            flag = 1
emails = []
i = 0
print(list_of_names)
emails = email_gen(list_of_names)
print(emails)

file.close()
file = open("task_file.txt", 'r+w')
for line in file:
    list1 = line.split(',')
    print(list1)
    # list[0] = emails[i]
    # i+=1
# file.close()
# file = open("task_file.txt", 'r+')
# for line in file:
#     print(line)
# file1.write(line)
