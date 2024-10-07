def solution(array):
    return (sorted(array)[-1], array.index(sorted(array)[-1]))