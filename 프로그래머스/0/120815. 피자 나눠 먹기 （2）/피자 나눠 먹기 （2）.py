def solution(n):
    for i in range (1, 51):
        if i * 6 % n == 0:
            return i
    return 0