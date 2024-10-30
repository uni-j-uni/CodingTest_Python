def solution(arr, k):
    answer = []
    for num in arr:
        if num not in answer:
            answer.append(num)
        if len(answer) == k:
            break
    if len(answer) < k:
        for i in range(k - len(answer)):
            answer.append(-1)
    return answer