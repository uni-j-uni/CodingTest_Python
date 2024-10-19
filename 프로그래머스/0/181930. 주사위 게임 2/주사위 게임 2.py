def solution(a, b, c):
    answer = a + b + c
    if a == b == c:
        answer *= pow(a, 3) + pow(b, 3) + pow(c, 3)
    if a == b or b == c or c == a:
        answer *= pow(a, 2) + pow(b, 2) + pow(c, 2)
    return answer