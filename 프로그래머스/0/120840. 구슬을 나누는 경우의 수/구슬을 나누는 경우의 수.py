def solution(balls, share):
    fact = 1
    for n in range(1, balls + 1):
        fact *= n
    for m in range(1, share + 1):
        fact //= m
    for num in range(1, balls - share + 1):
        fact //= num
    return fact