a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
#最大公約数(問3)
def euclid(a, b):

    if a < b:
        a, b = b, a

    while b > 0:
        a, b = b, a % b
    
    return a

print(euclid(int(a), int(b)))


#互いに素か判定(問4)
def judge(a, b):
    return euclid(a, b) == 1

#エクストラ
import random
def p():   
    sum = 0 #互いに素なときの数

    for i in range(100000):
        a = random.randrange(1, 10001)
        b = random.randrange(1, 10001)

        if judge(a, b) == True:
            sum +=1

    print(sum / 100000)

p()
