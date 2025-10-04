def solution(sizes):
    w, h = 0, 0
    for list in sizes:
        if (max(list) > w):
            w = max(list)
        if (min(list) > h):
            h = min(list)
    return w * h