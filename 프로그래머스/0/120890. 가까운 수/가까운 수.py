def solution(array, n):
    array.sort()
    return array[[abs(n - num) for num in array].index(min([abs(n - num) for num in array]))]