import math

def solution(n):
    return pow(math.sqrt(n) + 1, 2) if pow(int(math.sqrt(n)), 2) == n else -1