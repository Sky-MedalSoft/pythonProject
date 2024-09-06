# 装饰器
def sleep():
    import time
    import random
    print("程序开始睡眠")
    time.sleep(random.randint(1, 3))
    print("结束")


# sleep()

def outer(func):
    def inner():
        print("start")
        func()
        print("end")

    return inner


fn = outer(sleep)
fn()


# %%
# 装饰器
def outer(func):
    def inner():
        print("start")
        func()
        print("end")

    return inner


@outer
def sleep():
    import time
    import random
    print("程序开始睡眠")
    time.sleep(random.randint(1, 3))
    print("结束")


sleep()
