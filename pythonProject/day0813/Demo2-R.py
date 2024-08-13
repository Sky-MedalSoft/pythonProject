# R-1.1编写一个Python函数is_multiple(n,m)，用来接收两个整数值n和m，如果n是m的倍数，即
# 存在整数i使得n=mi，那么函数返回True，否则返同False。
# R-1.2编写一个Python函数iseven（k)，用来接收一个整数k，如果k是偶数返回True，否则返同
# False。但是，函数中不能使用乘法、除法或取余操作。
# R-1.3编写一个Python函数minmax（data），用来在数的序列中找出最小数和最大数，并以一个长度
# 为2的元组的形式返回。注意：不能通过内置函数min和max来实现。
# R-1.4编写一个Python函数，用来接收正整数n，返同1～n的平方和。
# R-1.5基于Python的解析语法和内置函数sum，写一个单独的命令来计算练习R-1.4中的和。
# R-1.6编写一个Python函数，用来接收正整数n，并返回1～n中所有奇数的平方和。
# R-1.7基于Python的解析语法和内置函数sum，写一个单独的命令来计算练习R-1.6中的和。
# R-1.8Python允许负整数作为序列的索引l值，如一个长度为n的字符串s，当索引值-n≤k<0时，
# 所指的元素为s[k]，那么求一个正整数索引值j≥0，使得s[j]指向的也是相同的元素。
# R-1.9要生成一个值为50，60，70，80的排列，求range构造函数的参数。
# R-1.10要生成一个值为8,6,4，2.0，-2，-4,-6,-8的排列，求range构造函数中的参数。
# R-1.11演示怎样使用Python列表解析语法来产生列表[1，2，4，8，16，32，64，128，256]。
# R-1.12Python的random模块包括一个函数choice（data），可以从一个非空序列返回一个随机元素。
# Random模块还包含一个更基本的randrange函数，参数化类似于内置的range函数，可以在
# 给定范围内返回一个随机数。只使用randrange函数，实现自己的choice函数。
# R-1.1


def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False


print(is_multiple(10, 5))


# R-1.2
def is_even(k):
    """k & 1 进行按位与操作，结果为0表示k是偶数，结果为1表示k是奇数。因此，(k & 1) == 0 返回True表示k是偶数，返回False表示k是奇数。"""
    return (k & 1) == 0


print(is_even(10))


# R-1.3
def minmax(data):
    """遍历序列来找到最小值和最大值"""
    min = data[0]
    max = data[0]
    for i in data:
        if i > min:
            max = i
        if i < max:
            i = min
    return (max, min)


print(minmax([10, 20, 30, 40]))


# R-1.4
def parse_squares_sum(n):
    # 初始化平方和
    sum_squares = 0
    # 计算1-n的平方和
    for i in range(1, n + 1):
        sum_squares += i ** 2
    return sum_squares


print(parse_squares_sum(5))
# R-1.5
# %%
print(sum(i ** 2 for i in range(5)))


# %%
# R-1.6
def parse_squares_sum_odd(n):
    sum_squares = 0
    return sum(i ** 2 for i in range(1, n + 1) if i % 2 != 0)


print(parse_squares_sum_odd(5))
# R-1.7
# 同1.5
# R-1.8
# *
# %%
import random

# R-1.9
print(list(range(50, 90, 10)))  # [50, 60, 70, 80]
# R-1.10
print(list(range(8, -10, -2)))
# R-1.11
print([2 ** i for i in range(9)])
# R-1.12
print(random.choice([1, 2, 3, 4, 5]))
# choice（data），可以从一个非空序列返回一个随机元素。
def my_choice(data):
    index = random.randrange(0, len(data))
    return data[index]
print(my_choice([1, 2, 3, 4, 5]))