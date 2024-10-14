while(True):
    num = input()
    if num == '0': break
    if len(num) % 2 == 0:
        front = num[:len(num) // 2]  
        back = num[len(num) // 2:]
        if front == ''.join(reversed(back)):
            print('yes')
        else:
            print('no')
    else:
        front = num[:len(num) // 2]
        back = num[len(num) // 2 + 1:]
        if front == ''.join(reversed(back)):
            print('yes')
        else:
            print('no')