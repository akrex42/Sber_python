s = input("Enter here\n")

print(s[2:3])

n = len(s)
print(s[n - 2:n - 1])

print(s[0:5])

print(s[:n - 2])

for i in range(0, n, 2):
    print(s[i], end='')
print()

for i in range(1, n, 2):
    print(s[i], end='')
print()

for i in range(n - 1, -1, -1):
    print(s[i], end='')
print()

for i in range(n - 1, -1, -2):
    print(s[i], end='')
print()

print(n)
