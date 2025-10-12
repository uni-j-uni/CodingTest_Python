def solution(babbling):
    answer = 0
    
    for word in babbling:
        word = word.replace("ayaaya", ".").replace("yeye", ".").replace("woowoo", ".").replace("mama", ".").replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ").strip()
        if (word == ""):
            answer += 1
    return answer