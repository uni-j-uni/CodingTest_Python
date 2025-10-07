def solution(k, score):
    answer = []
    list = []
    for i in range(len(score)):
        if (len(list) < k):
            list.append(score[i])
        else:
            if (list[-1] < score[i]):
                list.pop()
                list.append(score[i])
        list.sort(reverse=True)
        answer.append(list[-1])
    return answer