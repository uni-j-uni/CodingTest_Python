def solution(num_list):
    mul = 1
    for i in num_list:
        mul *= i
    return int(mul < sum(num_list) ** 2)