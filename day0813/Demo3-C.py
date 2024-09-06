# C-1.13编写一个函数的伪代码描述，该函数用来逆置n个整数的列表，使这些数以相反的顺序输出，
# 并将该方法与可以实现相同功能的Python函数进行比较。
# C-1.14编写一个Python函数，用来接收一个整数序列，并判断该序列中是否存在一对乘积是奇数的
# 互不相同的数。
# C-1.15编写一个Python函数，用来接收一个数字序列，并判断是否所有数字都互相不同（即它们是
# 不同的）。
# C-1.16在1.5.1节scale函数的实现中，循环体内执行的命令data[i]*=factor。我们已经说过这个数
# 字类型是不可变的，操作符*=在这种背景下使用是创建了一个新的实例（而不是现有实例的
# 变化）。那么scale函数是如何实现改变调用者发送的实际参数呢？
# C-1.171.5.1节scale函数的实现如下。它能正常工作吗？请给出原因。
# def scale(data,factor):
# for val in data:
# val *= factor
# C-1.18演示如何使用Python列表解析语法来产生列表[0,2,6,12,20,30,42,56,72,90]。
# C-1.19演示如何使用Python列表解析语法在不输人所有26个英文字母的情况下产生列表[a，b，'c.,z]。
# C-1.20Python的random模块包括一个函数shuffle（data)，它可以接收一个元素的列表和一个随机的
# 重新排列元素，以使每个可能的序列发生概率相等。random模块还包括一个更基本的函数
# randint（a，b），它可以返回一个从a到b（包括两个端点）的随机整数。只使用randint函数，
# 实现自己的shuffle函数。
# C-1.21编写一个Python程序，反复从标准输人读取一行直到抛出EOFError异常，然后以相反的顺
# 序输出这些行（用户可以通过键按Ctrl+D结束输人）。
# C-1.22编写一个Python程序，用来接收长度为n的两个整型数组a和b并返回数组a和b的点积。
# 也就是返回一个长度为n的数组c，即c[]=a[]·b[],fori=0,",n-1。
# C-1.23给出一个Python代码片段的例子，编写一个索引可能越界的元素列表。如果索引越界，程序
# 应该捕获异常结果并打印以下错误消息：
# “Don’t try buffer overflow attacks in Python!”
# C-1.24编写一个Python函数，计算所给字符串中元音字母的个数。
# C-1.25编写一个Python函数，接收一个表示一个句子的字符串s，然后返回该字符串的删除了所有
# 标点符号的副本。例如，给定字符串"Let'stry，Mike.”，这个函数将返回"LetstryMike”。
# C-1.26编写一个程序，需要从控制台输人3个整数a、b、c，并确定它们是否可以在一个正确的算术
# 公式（在给定的顺序）下成立，如“a+b=c”“a=b-c”或“a*b=c”
# C-1.27在1.8节中，我们对于计算所给整数的因子时提供了3种不同的生成器的实现方法。1.8节末
# 尾处的第三种方法是最有效的，但我们注意到，它没有按递增顺序来产生因子。修改生成器，
# 使得其按递增顺序来产生因子，同时保持其性能优势。
# C-1.28在n维空间定义一个向量v=（v，v2，v）的p范数，如下所示：
# l=/v²+v+··+v
# 对于p=2的特殊情况，这就成了传统的欧几里得范数，表示向量的长度。例如，一个二维向量坐
# 标为（4,3）的欧儿里得范数为√4²+3²=√16+.9=√25=5。编写norm函数，即norm（v,p），返
# 回向量v的p范数的值，norm（v)，返回向量v的欧几里得范数。你可以假定v是一个数字列表。
# %%
# C-1.13
import string


def reverse(string):
    # 使用切片语法
    return string[::-1]


print(reverse("hello"))


# %%
# C-1.14
def has_odd_product_pair(sequence):
    # 获取序列长度
    n = len(sequence)

    # 遍历序列中的每一对不同的数
    for i in range(n):
        for j in range(i + 1, n):
            # 获取当前的一堆数
            a, b = sequence[i], sequence[j]
            # 检查这对数的乘积是否为奇数
            if (a * b) % 2 != 0:
                return True
    return False


print(has_odd_product_pair([1, 2, 3, 4, 5]))


# %%
# C-1.15
def check_same(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                return False
    else:
        return True


def check_same2(sequence):
    """集合是一种无序且不重复的元素集合，可以利用集合的特性来判断序列中的元素是否唯一。"""
    # 将序列转化为集合
    unique_elements = set(sequence)
    return len(unique_elements) == len(sequence)


print(check_same([1, 2, 3, 4, 5]))
print(check_same2([1, 2, 3, 4, 5]))


# %%
# C-1.16
def scale(data, factor):
    for i in range(len(data)):
        data[i] *= factor


numbers = [1, 2, 3, 4, 5]
scale(numbers, 2)
print(numbers)
# C-1.17
# %%
# C-1.18
# 使用列表解析来生成列表
sequence = [n * (n + 1) for n in range(10)]
print(sequence)
# %%
# C-1.19
print([chr(i) for i in range(ord('A'), ord('Z') + 1)])
# %%
# C-1.20
import random


def mu_shuffle(data):
    for i in range(len(data) - 1, 0, -1):
        # 生成一个从0到i的随机整数
        j = random.randint(0, i)
        # 交换data[i]和data[j]
        data[i], data[j] = data[j], data[i]


data = [1, 2, 3, 4, 5]
mu_shuffle(data)
print(data)


# %%
# C-1.21
def reverse_input():
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        for line in reversed(lines):
            print(line)


reverse_input()


# %%
# C-1.22
def dot_product(a, b):
    """检查两个数组长度是否相等"""
    if len(a) != len(b):
        # raise关键字用于引发一个指定的异常或错误
        raise ValueError("两个数组长度必须相等")
    # 计算点积
    c = [a[i] * b[i] for i in range(len(a))]
    return c


a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
print(dot_product(a, b))


# %%
# C-1.23
def safe_access(lst, index):
    try:
        return lst[index]
    except  IndexError:
        print("Don't try buffer overflow attacks in Python")


my_list = [1, 2, 3, 4, 5]
safe_access(my_list, 10)


# %%
# C-1.24
def count_vowels(s):
    """
        计算字符串中元音字母的个数。
        参数:
        s (str): 输入的字符串。
        返回:
        int: 元音字母的个数。
        """
    # 计算原音字母集合
    vowels = 'aeiou'
    # 初始化计数器
    count = 0
    # 遍历字符串中的每个字符
    for c in s:
        # 如果字符为元音字母，则计数器加一
        if c in vowels:
            count += 1
    # 返回原音字母个数
    return count


# %%
# C-1.25
import string


def remove_punctuation(s):
    # 使用字符串模块中的标点符号集合
    punctuation_set = set(string.punctuation)
    # 使用生成器表达式过滤掉标点符号
    result = ''.join(char for char in s if char not in punctuation_set)
    return result


print(remove_punctuation("Let's try,Mike"))


# %%
# C-1.26
def check_arithmetic_formula(a, b, c):
    if a + b == c:
        print(f"{a} + {b} = {c}")
        return True
    if a == b - c:
        print(f"{a} - {b} = {c}")
        return True
    if a * b == c:
        print(f"{a} * {b} = {c}")
        return True
    return False


a = int(input("请输入第一个整数： a: "))
b = int(input("请输入第一个整数： b: "))
c = int(input("请输入第一个整数： c: "))
if not check_arithmetic_formula(a, b, c):
    print("没有公式成立")


# %%
# C-1.27
# C-1.27
def factors(n):
    """
    生成给定整数 n 的所有因子，按递增顺序排列。

    参数:
    n (int): 输入的整数。

    返回:
    generator: 生成 n 的所有因子。
    """
    k = 1
    # 生成较小的因子
    while k * k < n:
        if n % k == 0:
            yield k
        k += 1
    # 如果 n 是平方数，生成平方根
    if k * k == n:
        yield k
    k -= 1
    # 生成较大的因子
    while k > 0:
        if n % k == 0:
            yield n // k
        k -= 1


# 示例调用
for factor in factors(100):
    print(factor)


# %%
# C-1.28
def norm(v, p=2):
    sum_of_powers = sum(x ** p for x in v)
    return sum_of_powers ** (1 / p)


v = [4, 3]
print(norm(v))
print(norm(v, p=3))
print(norm(v, p=1))
# .2
import math


def norm(v, p=2):
    return math.pow(sum(math.pow(x, p) for x in v), 1 / p)


print(norm([4, 3]))
