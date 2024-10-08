N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

print(sum((i + T - 1) // T for i in sorted(size)))
print(N // P, N % P)