s = input()
s1 = ''
s = s.split(' ')

for word in s:
    if word:
        s1 += ''.join(word[0].upper() + word[1:]) + ' '
    else:
        s1 += ''.join(' ')

print(s1)