while True:
    lines = list(map(int, input().split()))
    if (lines.count(0) == 3): break
    lines.sort()
    print('right' if (lines[0] ** 2 + lines[1] ** 2 == lines[2] ** 2) else 'wrong')