A = int(input())
B = int(input())
C = int(input())

for i in range(10):
    print(list(map(int, str(A * B * C))).count(i))