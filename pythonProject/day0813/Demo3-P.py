# P-1.29编写一个Python程序，输出由字母c，a，t，d，o，'g组成的所有可能的字符串（每个字母只
# 使用1次）。
# P-1.30编写一个Python程序，输人一个大于2的正整数，求将该数反复被2整除直到商小于2为止
# 的次数。
# P-1.31编写一个可以“找零钱”的Python程序。程序应该将两个数字作为输人，一个是需要支付的
# 钱数，另一个是你给的钱数。当你需要支付的和所给的钱数不同时，它应该返回所找的纸币
# 和硬币的数量。纸币和硬币的值可以基于之前或现任政府的货币体系。试设计程序，以便返
# 回尽可能少的纸币和硬币。
# P-1.32编写一个Python程序来模拟一个简单的计算器，使用控制台作为输人和输出的专用设备。也
# 就是说，计算器的每一次输人做一个单独的行，它可以输人一个数字（如1034或12.34）或操
# 作符（如+或=）。每一次输入后，应该输出计算器显示的结果并将其输出到Python控制台。
# P-1.33编写一个Python程序来模拟一个手持计算器，程序应该可以处理来自Python控制台（表示
# push按钮）的输入，每个操作执行完毕后将内容输出到屏幕。计算器至少应该能够处理基本
# 的算术运算和复位/清除操作。
# P-1.34一种惩罚学生的常见方法是让他们将一个句子写很多次。编写独立的Python程序，将以下句
# 子“Iwill never spammy friends again.”写100次。程序应该对每个句子进行计数，另外，
# 应该有8次不同的随机输入错误。
# P-1.35生日论是说，当房间中人数n超过23时，那么该房间里有两个人生日相同的可能性是一半
# 以上。这其实不是一个论，但许多人觉得不可思议。设计一个Python程序，可以通过一系
# 列随机生成的生日的实验来测试这个学论，例如可以n=5，10,15,20，，100测试这个论。
# P-1.36编写一个Python程序，输人一个由空格分隔的单词列表，并输出列表中的每个单词出现的次
# 数。在这一点上，你不需要担心效率，因为这个问题会在这本书后面的部分予以解决。

# %%
# P-1.29
# 编写一个Python程序，输出由字母c，a，t，d，o，g组成的所有可能的字符串（每个字母只
# 使用1次）。
import itertools

# 定义字母集合
letters = 'catdog'
# 生成所有排序
permutations = itertools.permutations(letters)
# 将每个排序转换为字符串并输出
for perm in permutations:
    print(''.join(perm))


# %%
# P-1.30
def divide_by_two(n):
    counter = 0
    while n >= 2:
        n /= 2
        counter += 1
    return counter


print(divide_by_two(9))


# %%
# P-1.34
def copy_statement():
    s = "I will never spam my friends again."
    count = 0
    for i in range(100):
        print(s)
        count += 1
    return count


# copy_statement()
print(copy_statement())
# %%
import random

sentence = "I will never spam my friends again."
errors = ["I will never spam my friends aaaaa.",
          "i will never spam my friends bbbbb.",
          "I will never spam my friends ccccc."]
positions = random.sample(range(100), 8)
for i in range(100):
    if i in positions:
        print(f"{i + 1}:{random.choice(errors)}")
    else:
        print(f"{i + 1}:{sentence}")
# %%
import random


def check_duplicate(n, num_trials=10000):
    success_count = 0
    for _ in range(num_trials):
        # 生成n个随机生日
        birthdays = [random.randint(1, 365) for _ in range(n)]
        if len(birthdays) > len(set(birthdays)):
            success_count += 1
    # 计算成功率
    success_rate = success_count / num_trials
    return success_rate


# 测试不同值
for n in [5, 10, 15, 20, 23, 30, 50, 100]:
    print(f"n={n}:{check_duplicate(n)}")
