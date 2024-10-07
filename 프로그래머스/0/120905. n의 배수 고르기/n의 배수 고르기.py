def solution(n, numlist):
    list = []
    for num in numlist:
        if num % n == 0:
            list.append(num)
    return list