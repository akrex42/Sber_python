s = input()
s1 = '!@#$%^&*()-+'
low = "добавить 1 строчную букву,"
u = "добавить 1 заглавную букву,"
d = "добавить 1 цифру,"
i = 0
sp = "добавить 1 спецсимвол,"
er = 0
length = 'увеличить число символов -'
var = 0

while i < len(s):
    if s[i].isdigit():
        d = ''
    elif s[i].islower():
        low = ''
    elif s[i].isupper():
        u = ''
    else:
        j = 0
        while j < len(s1):
            if s[i] == s1[j]:
                er = 2
                break
            j += 1
        if er == 2:
            sp = ''
            er = 0
        else:
            er = 1
    i += 1
s2 = ''
if len(s) < 12:
    var = 12 - len(s)
    length = length + ' ' + str(var) + ','
else:
    length = ''
if er == 1:
    print('Ошибка. Запрещенный спецсимвол')
elif sp == '' and d == '' and u == '' and low == '' and len(s) >= 12:
    print('Сильный пароль.')
else:
    print('Слабый пароль. Рекомендации: ', end='')
    if var:
        s1 = length + u + low + d + sp
    else:
        s1 = u + low + d + sp
    myList = s1.split(',')
    myList1 = []
    for word in myList:
        if word != '':
            myList1.append(word)
    print(', '.join(myList1), end='')



