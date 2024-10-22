def solution(emergency):
    array = sorted(emergency, reverse = True)
    return [array.index(num) + 1 for num in emergency]