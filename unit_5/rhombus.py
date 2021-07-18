
n = int(input("Enter here:\n"))
for i in range(1, n + 1):
    for a in range(1, n - i + 1):
        print(end=' ')
    for j in range(1, i + 1):
        print(j, end='')
    for k in range(1, i + 1):
        if i - k != 0:
            print(i - k, end='')
    print()
for i in range(1, n):
    for a in range(1, i + 1):
        print(end=' ')
    for l in range(1, n - i + 1):
        print(l, end='')
    for m in range(1, n - i + 1):
        if n - i - m != 0:
            print(n - i - m, end='')
    print()

# n = 100
# for i in range(n, 1, -1):
#     print(i, end=' ')
