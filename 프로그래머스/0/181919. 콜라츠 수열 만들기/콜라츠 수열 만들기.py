def solution(n):
    nums = []
    while (n != 1):
        nums.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    nums.append(1)
    return nums