def do_arithmetic_operation(string_args):
    ''' do_arithmetic_operation function takes a string, converts it to a list,
        then parse a list adn do  the proper operation
        :param string_args:
        :return: result of arithmetic operation
    '''
    my_list = list(string_args)
    my_str = ''
    flag_second_digit = 0
    sign = ''
    for item in my_list:
        if item.isdigit():
            my_str += str(item)
        else:
            break
    first_digit = int(my_str)
    for item in my_list:
        if item.isdigit():
            continue
        else:
            sign += str(item)
    my_str = ''
    for i in range(len(my_list)):
        if not my_list[i].isdigit():
            while i < len(my_list):
                if my_list[i].isdigit():
                    my_str += str(my_list[i])
                    flag_second_digit = 1
                i += 1
            break
    if flag_second_digit:
        second_digit = int(my_str)
        if sign == '+':
            return first_digit + second_digit
        elif sign == '-':
            return first_digit - second_digit
        elif sign == '/':
            return first_digit / second_digit
        elif sign == '*':
            return first_digit * second_digit
        elif sign == '**':
            return first_digit ** second_digit
    else:
        if sign == '%':
            return first_digit / 100
        elif sign == '**':
            return first_digit ** 2


print(do_arithmetic_operation(input()))
