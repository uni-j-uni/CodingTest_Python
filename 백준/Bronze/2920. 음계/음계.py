list = list(map(int, input().split()))

if list.index(1) == 0:
    for i in range(1, 9):
        if i - 1 != list.index(i):
            print('mixed')
            break
        elif i == 8 and list.index(i) == 7:
            print('ascending')
elif list.index(1) == 7:
    for i in range(8, 0, -1):
        if i - 1 != list.index(9 - i):
            print('mixed')
            break
        elif i == 1 and list.index(i) == 7:
            print('descending')
else:
    print('mixed')