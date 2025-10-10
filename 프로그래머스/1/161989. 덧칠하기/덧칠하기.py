def solution(n, m, section):
    answer = 0
    section.sort()
    i = 0
    while i < len(section):
        start = section[i]
        end = start + m
        while i < len(section) and section[i] < end:
            i += 1
        answer += 1
    return answer