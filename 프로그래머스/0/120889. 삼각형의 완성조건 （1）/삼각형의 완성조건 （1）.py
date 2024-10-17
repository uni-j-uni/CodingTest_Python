def solution(sides):
    sides.sort()
    return 2 - int(sides[0] + sides[1] > sides[2])