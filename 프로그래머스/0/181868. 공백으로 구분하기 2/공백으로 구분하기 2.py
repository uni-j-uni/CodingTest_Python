def solution(my_string):
    return list(' '.join(my_string.split()).strip().replace(" +", " ").split(" "))