my_list = eval(input("Enter the list:\n"))
my_str = ''
my_dict = {}
my_dict = {item: 0 for item in my_list}
for i in range(len(my_list)):
    for key, value in my_dict.items():
        if key == my_list[i]:
            my_dict.update({key: value + 1})
for key, value in my_dict.items():
    my_str += str(my_dict.get(key)) + ' '
print(my_str[0:len(my_str) - 1], end='')
