def solution(food):
    answer = ''.join(str(i) * (food[i] // 2) for i in range(len(food)))
    return answer + '0' + answer[::-1]