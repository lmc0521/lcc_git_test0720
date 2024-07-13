import random

x = random.randint(1, 50)

while 1:
    y = int(input("請猜一個數字"))

    if x == y:
        print("bingo")
    else:
        print("猜錯了")
