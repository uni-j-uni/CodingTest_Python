import re
def solution(my_string):
    return sum(int(num) for num in re.findall(r'\d+', my_string))