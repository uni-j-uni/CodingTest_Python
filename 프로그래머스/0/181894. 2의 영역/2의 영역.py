def solution(arr):
    return arr[arr.index(2):len(arr) - list(reversed(arr)).index(2)] if 2 in arr else [-1]