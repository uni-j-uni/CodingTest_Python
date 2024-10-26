def solution(myStr):
    answer = ' '.join(myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split()).split()
    return answer if len(answer) > 0 else ["EMPTY"]