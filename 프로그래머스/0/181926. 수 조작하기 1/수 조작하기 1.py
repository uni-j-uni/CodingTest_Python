def solution(n, control):
    for word in control:
        if word == 'w':
            n += 1
        elif word == 's':
            n -= 1
        elif word == 'd':
            n += 10
        else:
            n -= 10
    return n