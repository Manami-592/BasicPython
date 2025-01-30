a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
arrays = [int(a), int(b)]

for array in arrays:
    judge = True

    if array == 1:
        judge = False

    k = array - 1

    while judge:
        if k == 1:
            break
        elif array % k == 0:
            judge = False
            break
        else:
            k -= 1

    if judge:
        print('{}は素数'.format(array))
    else:
        print('{}は素数でない'.format(array))
        