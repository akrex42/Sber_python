n = int(input("Enter here:\n"))
for i in range(1, n + 1):
    for a in range(1, n - i + 1):
        print(end=' ')
    for j in range(1, i + 1):
        print(j, end='')
    print()
for i in range(n + 1, 1, -1):
    for a in range(1, n + 1):
        print(end=' ')
    for k in range(1, i + 1):
        if i - k != 0:
            print(i - k, end='')
    print()