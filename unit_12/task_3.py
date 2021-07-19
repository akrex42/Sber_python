set_1 = eval(input())
set_2 = eval(input())
if set_1 == set_2:
    print(False)
else:
    print(set_1.issubset(set_2))
