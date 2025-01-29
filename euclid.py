a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
a1 = int(a)
b1 = int(b)

if a1 < b1:
    k = a1
    a1 = b1
    b1 = k

q = a1 // b1
r = a1 % b1

while r != 0:
    q = a1 // b1
    r = a1 % b1

    if r == 0:
        break
    
    a1 = b1
    b1 = r
    
if r == 0:
    print(b1)