def solution(n):
    i = 0
    fac = 1
    while(True):
        i += 1
        if i * fac > n:
            return i - 1
        fac *= i