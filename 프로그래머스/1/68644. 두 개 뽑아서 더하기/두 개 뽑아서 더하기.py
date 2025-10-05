from itertools import combinations

def solution(numbers):
    return sorted(list(set(sum(num) for num in combinations(numbers, 2))))