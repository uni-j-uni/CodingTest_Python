import math

def solution(n):
    if n == 0:
        return 0
    result = 1
    for i in range(2, n + 1):
        if n % i == 0:
            result += i
    return result