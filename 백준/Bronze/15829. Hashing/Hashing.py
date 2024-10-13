L = map(int, input().split())
s = input()

answer = 0
i = 0
for ch in s:
    answer += (ord(ch) - 96) * pow(31, i)
    i += 1

print(answer)