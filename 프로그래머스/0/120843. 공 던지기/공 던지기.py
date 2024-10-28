def solution(numbers, k):
    i = 2 * k - 2
    if i > len(numbers):
        i %= len(numbers)
    return numbers[i] 