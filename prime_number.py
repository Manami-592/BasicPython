a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
def NumberJudge(n):
    digits = list(n) #小数でNone返す
    for digit in digits:
        if digit == '.':
            raise TypeError('not integer')
    
    if int(n) <= 0:
        raise ValueError('not natual number')
    elif int(n) == 1:
        return False 

    k = int(n) - 1
    judge = True
    
    while judge:
        if k == 1:
            break
        elif int(n) % k == 0:
            judge = False
            break
        else:
            k -= 1
    
    if not judge:
        return False
    return True

arrays = [a, b]
for array in arrays:
    print(NumberJudge(array))
