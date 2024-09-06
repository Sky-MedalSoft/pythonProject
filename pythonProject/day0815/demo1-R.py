# %%
# R-2.4
class Flower:
    def __init__(self, name, num, price):
        self.name = name
        self.num = num
        self.price = price

    def get_name(self):
        return self.name

    def get_num(self):
        return self.num

    def get_price(self):
        return self.price

    def set_name(self, name):
        self.name = name

    def set_num(self, num):
        self.num = num

    def set_price(self, price):
        self.price = price


# %%
# P-2.33
import sympy as sp


# 定义一个函数来计算多项式的一阶导数
def polynomial(poly):
    # 定义变量
    x = sp.symbols('x')
    # 将多项式字符串转化为sympy表达式
    expression = sp.sympify(poly)
    # 计算导数
    derivative = sp.diff(expression, x)
    return derivative


# 示例
poly = "3*x**2 + 2*x + 1"
print(f"多项式{poly}的一阶导数是：{polynomial(poly)}")
# %%
# P-2.34
import matplotlib.pyplot as plt
from collections import Counter
import string


# 定义一个函数来绘制文档中每个字母出现频率的柱形图
def plot_letters_frequency(file_path):
    # 读取文件内容
    with open(file_path, 'r') as f:
        content = f.read().lower()  # 转换为小写以统一统计
    # 过滤出字母字符并统计每个字母出现的频率
    letters = [char for char in content if char in string.ascii_lowercase]
    letter_counts = Counter(letters)
    # 按字母顺序排序
    sorted_letter_counts = dict(sorted(letter_counts.items()))

    # 绘制柱形图
    plt.bar(sorted_letter_counts.keys(), sorted_letter_counts.values())
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Frequency of Letters')
    plt.show()


# 文件路径
file_path = 'D:\Code\Python\pythonProject\day0815\letters.txt'

plot_letters_frequency(file_path)
