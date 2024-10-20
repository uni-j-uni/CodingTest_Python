def solution(age):
    return ''.join(chr(ord(word) + 49) for word in str(age))