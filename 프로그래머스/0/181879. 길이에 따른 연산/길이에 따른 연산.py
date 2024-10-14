def solution(num_list):
    answer = 1
    if len(num_list) > 10:
        answer = sum(num_list)
    else:
        for num in num_list:
            answer *= num
    return answer