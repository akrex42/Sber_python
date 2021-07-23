def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + "." + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + "." + i[0][0:letter] + '@company.io')
    return emails


list_of_names_gen = []
emails_raw = []
list1 = []
list2 = []
flag_blank = 0
file = open("task_file.txt", 'r+')
for line in file:
    list1 = line.split(',')
    if len(list1[3][1:]) != 7 or not list1[3][1:].isdigit():
        continue
    for it in list1[1:]:
        if it == ' ':
            flag_blank = 1
            break
    if not flag_blank:
        list2.append(list1[1][1:])
        list2.append(list1[2][1:])
        list_of_names_gen.append(list2)
        list2 = []
    elif flag_blank:
        flag_blank = 0
emails_raw = email_gen(list_of_names_gen)
file.seek(0)
j = 0
index = 0
flag_blank = 0
list_of_lines = file.readlines()
for line in list_of_lines:
    list1 = line.split(',')
    if len(list1[3][1:]) != 7 or not list1[3][1:].isdigit():
        list_of_lines[j] = line
        j += 1
        continue
    for it in list1[1:]:
        if it == ' ':
            flag_blank = 1
            break
    if not flag_blank:
        if list1[0] == '':
            list_of_lines[j] = str(emails_raw[index]) + line
            index += 1
    elif flag_blank:
        flag_blank = 0
        list_of_lines[j] = line
    j += 1
file.close()
file = open("task_file.txt", 'w+')
file.writelines(list_of_lines)
file.seek(0)
for line in file:
    print(line)
