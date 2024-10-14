def solution(numLog):
    answer = { 1 : 'w', -1 : 's', 10 : 'd', -10 : 'a' }
    return ''.join(answer[numLog[i + 1] - numLog[i]] for i in range(len(numLog) - 1))