list = list(map(int, input().split()))
list = [x ** 2 for x in list]

print(sum(list) % 10)