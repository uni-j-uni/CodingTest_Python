def solution(my_string, num1, num2):
    my_string = list(my_string)
    ch1 = my_string[num1]
    ch2 = my_string[num2]
    my_string[num1] = ch2
    my_string[num2] = ch1
    return ''.join(my_string)