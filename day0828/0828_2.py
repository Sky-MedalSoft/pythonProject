money: int = 5000000

name: str = input("请输入您的姓名：")


def query():
    print(f"{name},您的余额为{money}")


def save(save_money):
    global money
    money += save_money
    print(money)


def pick(pick_money):
    global money
    money -= pick_money


def main():
    print("欢迎进入ATM")
    print(f"{name}，请输入您要进行的操作：")
    print("查询余额：\t输入【1】")
    print("存款：\t\t输入【2】")
    print("取款：\t\t输入【3】")
    print("退出：\t\t输入【4】")


while 1:
    main()
    operate = int(input())
    if operate == 1:
        query()
        continue
    elif operate == 2:
        save_money = int(input("请输入金额："))
        save(save_money)
        query()
    elif operate == 3:
        pick_money = int(input("请输入金额："))
        pick(pick_money)
        query()
    else:
        break
