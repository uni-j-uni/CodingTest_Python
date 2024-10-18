def solution(my_string):
    answer = []
    for word in my_string:
        if word in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            answer.append(int(word))
    return sorted(answer)