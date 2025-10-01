import math

def solution(left, right):
    answer = 0
    for i in range (left, right + 1):
        if math.pow(int(math.sqrt(i)), 2) == i:
            answer -= i
        else:
            answer += i
    return answer