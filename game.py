import random

x = random.randint(1, 50)

for i in range(10):
    y = int(input("請猜一個數字"))
    n += 1
    if x == y:
        print(f"bingo,第{n}次猜對")
        break
    else:
        if x > y:
            print("猜高一點")
        else:
            print("猜低一點")

if x != y:
    print(f"答案為{x}")
