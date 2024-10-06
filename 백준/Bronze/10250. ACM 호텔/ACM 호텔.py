T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    room = N // H if N % H == 0 else N // H + 1
    floor = N % H * 100 if N % H != 0 else H * 100
    print(floor + room)