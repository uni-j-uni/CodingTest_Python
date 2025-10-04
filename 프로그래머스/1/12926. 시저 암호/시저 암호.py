def solution(s, n):
    result = ''
    for word in s:
        if word == ' ':
            result += ' '
        elif 'A' <= word <= 'Z':
            result += chr((ord(word) - 65 + n) % 26 + 65)
        elif 'a' <= word <= 'z':
            result += chr((ord(word) - 97 + n) % 26 + 97)
    return result