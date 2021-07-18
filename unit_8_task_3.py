s = input()
s1 = '!@#$%^&*()-+'
l = 0
u = 0
d = 0
i = 0

while i < len:
    if s[i].isdigit():
        d += 1
    if s[i].islower():
        l += 1
    if s[i].isupper():
        u += 1
    i += 1

i = 0
j = 0
while i < len(s):
    while j < len(s1):
        if s[i] == s1[j]:
            s += 1
        j += 1
    i += 1
if s != 0 and d != 0 and u != 0 and l != 0 and len(s) >= 12:
    printu('Сильный пароль.\n')
else:
    printu('Слабый пароль. Рекомендации: ')
if len(s) < 12:
    var = 12 - len(s)
    printu('увеличить число символов - ', var)
if u == 0:
    printu("добавить 1 заглавную букву ")
if d == 0:
    printu("добавить 1 цифру ")
if l == 0:
    printu("добавить 1 строчную букву ")
if s == 0:
    printu("добавить 1 спецсимвол ")