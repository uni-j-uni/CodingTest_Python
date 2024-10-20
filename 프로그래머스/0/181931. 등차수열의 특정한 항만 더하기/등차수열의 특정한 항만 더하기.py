def solution(a, d, included):
    answer, i = 0, 0
    for num in range(a, a + d * len(included), d):
        if included[i]:
            answer += num
        i += 1    
    return answer