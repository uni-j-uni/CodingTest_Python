def solution(arr):
    answer = []
    for i in arr:
        for j in range(i):
            answer.append(str(i))
    return list(map(int, answer))