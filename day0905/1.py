# 闭包
def outer(logo):
    def inner(msg):
        print(f"{logo}{msg}{logo}")
    return inner

in1 = outer("Hello World")
in1("信息")

#%%
def money_create(money = 0):
    def atm(num, save = True):
        nonlocal money
        if save == True:
            money += num
            print(f"存钱{num}，当前余额为{money}")
        else:
            money -= num
            print(f"取钱{num}，当前余额为{money}")
    return atm

sava1 = money_create()
sava1(100)
sava1(100)
sava1(50, save = False)