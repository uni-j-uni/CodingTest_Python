from itertools import combinations
import math

def solution(nums):
    answer = 0
    
    for i in combinations(nums, 3):
        num = sum(i)
        if(isPrime(num)):
            answer += 1

    return answer

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True