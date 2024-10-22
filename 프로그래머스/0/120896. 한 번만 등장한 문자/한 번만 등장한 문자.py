def solution(s):
    answer = ''
    i = 0
    while(True):
        if s.count(s[i]) > 1:
            s = s.replace(s[i], '')
        else:
            answer += s[i]
            if i + 1 >= len(s):
                break
            else:
                i += 1
    return ''.join(sorted(answer))