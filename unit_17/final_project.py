from passwords import *
from emails import *
import re

file = open("file_sample.txt", 'r+')
file1 = open("file_errors.txt", 'a+')
list_of_lines = file.readlines()
i = 1
flag_blank = 0
if re.search(r'PASSWORDS', list_of_lines[0]) is None:
    list_of_lines[0] = list_of_lines[0].replace('\n', ', ') + 'PASSWORDS' + '\n'
file.seek(0)
for line in list_of_lines[1:]:
    list1 = line.split(',')
    if len(list1[3][1:]) != 7 or re.search(r'\D', list1[3][1:]) is not None:
        file1.write(list_of_lines[i])
        list_of_lines.pop(i)
        continue
    if re.match(r'[a-z]', list1[1][1:]) is not None or re.match(r'[a-z]', list1[2][1:]) is not None \
            or re.match(r'[a-z]', list1[4][1:]) is not None:
        file1.write(list_of_lines[i])
        list_of_lines.pop(i)
        continue
    if re.search(r'[^a-z\.A-Z\n]', list1[1][1:]) is not None or re.search(r'[^a-z\.A-Z\n]', list1[2][1:]) is not None \
            or re.search(r'[^a-z\.A-Z\n]', list1[4][1:]) is not None:
        file1.write(list_of_lines[i])
        list_of_lines.pop(i)
        continue
    for it in list1[1:]:
        if it == ' ':
            file1.write(list_of_lines[i])
            list_of_lines.pop(i)
            flag_blank = 1
            break
    if not flag_blank and len(list_of_lines[i].split(',')) == 5:
        list_of_lines[i] = list_of_lines[i][:len(list_of_lines[i]) - 1] + ', ' + password_gen(20) + '\n'
        i += 1
    elif flag_blank:
        flag_blank = 0
file.close()
file = open("file_sample.txt", 'w+')
file.writelines(list_of_lines)
file.close()
fill_emails()
file = open("file_sample.txt", 'r+')
for line in file:
    print(line)

