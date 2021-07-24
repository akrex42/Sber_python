from passwords import *
from emails import *
import re

file = open("file_sample.txt", 'r+')
list_of_lines = file.readlines()
i = 0
if re.search(r'PASSWORDS', list_of_lines[0]).group(0) != 'PASSWORDS':
    list_of_lines[0] = list_of_lines[0].replace('\n', ', ') + 'PASSWORDS' + '\n'
file.close()
file = open("file_sample.txt", 'w+')
file.writelines(list_of_lines)
file.seek(0)
for line in file:
    print(line)
# password_gen(19)
# fill_emails()
