def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        for num in sorted(arr[queries[i][0]:queries[i][1] + 1]):
            if num > queries[i][2]:
                answer.append(num)
                break
        if len(answer) != i + 1:
            answer.append(-1)
    return answer