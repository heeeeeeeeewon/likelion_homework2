#2

import random

Q = input("로또 번호 추출을 시작합니까?(y/n) :")

if Q == "y":
    def Lotto():
        return random.randrange(1,46)

    lotto = []
    num = 0
    print("번호 추출중...");

    while True:
        num = Lotto()
        if lotto.count(num) == 0:
            lotto.append(num)
        if len(lotto) >= 6:
            break

    import time

    for i in range(1,6,1):
        time.sleep(1)
        print(i)
        
    print("로또 번호는!!\n")

    lotto.sort()

    for i in range(0,6):
        print("%d "%lotto[i],end = '') 

if Q == "n":
    print("로또 추출을 종료합니다.")

else:
    print("다시 입력하세요")
    

