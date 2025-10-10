def solution(a, b):
    day = {0:"SUN", 1:"MON", 2:"TUE", 3:"WED", 4:"THU", 5:"FRI", 6:"SAT"}
    return day[([0, 4, 0, 1, 4, 6, 2, 4, 0, 3, 5, 1, 3][a] + b) % 7]