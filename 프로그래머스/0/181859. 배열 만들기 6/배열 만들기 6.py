def solution(arr):
    stk = []
    i = 0
    while (i < len(arr)):
        if not stk: stk.append(arr[i])
        elif stk[-1] == arr[i]: del stk[-1]
        else: stk.append(arr[i])
        i += 1
    return stk or [-1]