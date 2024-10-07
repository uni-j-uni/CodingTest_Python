def solution(hp):
    answer = 0
    while (hp > 2):
        if hp >= 5:
            answer += hp // 5
            hp %= 5
        elif hp >= 3:
            answer += 1
            hp %= 3
    return answer + hp