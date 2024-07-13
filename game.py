import random

x = random.randint(1, 50)

for i in range(10):
    y = int(input("請猜一個數字"))

    if x == y:
        print("bingo")
    else:
        print("猜錯了")
