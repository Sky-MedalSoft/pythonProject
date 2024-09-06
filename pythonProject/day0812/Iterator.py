# 定义迭代器类
class MyIterator:
    """ 初始化方法 """
    """ __init__方法在创建类时被调用"""

    def __init__(self, data):
        self.data = data
        self.index = 0

    """ __iter__ 方法返回一个迭代器对象 """

    def __iter__(self):
        return self

    """__next__ 方法用于获取迭代器的下一个元素。"""

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


# 使用迭代器
dateDemo = [1, 2, 3, 4]
iterator = MyIterator(dateDemo)

for i in iterator:
    print(i)


# 生成器 (Generator)
# 生成器是使用yield关键字的函数。
# 每次调用生成器的__next__()方法时，生成器函数会运行到下一个yield语句，并返回其值。
# 生成器在函数执行完毕后会自动引发StopIteration异常。

def my_generrator():
    yield '执行语句1'
    yield '执行语句2'
    yield '执行语句3'
    yield '执行语句4'


# 使用生成器
gen = my_generrator()
for i in gen:
    print(i)
