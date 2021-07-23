from random import *

num = int(input())

if num < 12:
    print("Password too short")
else:
    password = []
    password = str(randint(0, 9)) + ' ' + choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")\
        + ' ' + choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()) + ' ' + choice("!@#$%^&*()-+") + ' '
    for i in range(4, num):
        password = password\
            + choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-+0123456789abcdefghijklmnopqrstuvwxyz") + ' '
    list1 = password.split()
    shuffle(list1)
    final_password = ''.join(list1)
    print(final_password)

