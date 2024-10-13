def solution(myString):
    myString = myString.lower()
    return ''.join(word.upper() if word == 'a' else word for word in myString)