def solution(myString):
    return ''.join(word if word > 'l' else 'l' for word in myString)