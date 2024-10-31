def solution(picture, k):
    return [picxel.replace('.', '.' * k).replace('x', 'x' * k) for picxel in picture for i in range(k)]