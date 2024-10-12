N = int(input())

answer = 0

for i in range(N - 1):
    rest = 0
    num = i
    while (num > 0):
        rest += num % 10
        num //= 10
    if (i + rest == N):
        answer = i
        break
    
print(answer)