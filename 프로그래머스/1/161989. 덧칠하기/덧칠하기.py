def solution(n, m, section):
    answer = 1
    start = section[0]
    
    for num in section:
        if num - start >= m:
            start = num
            answer += 1

    return answer