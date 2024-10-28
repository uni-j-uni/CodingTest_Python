def solution(order):
    return sum(5000 if 'latte' in money else 4500 for money in order)