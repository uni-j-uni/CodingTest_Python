def solution(k, m, score):
    answer = 0
    score.sort()
    
    while (len(score) >= m):
        for i in range(m):
            if (i == m - 1):
                answer += score[-1] * m
            score.pop()
    return answer