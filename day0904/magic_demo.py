class Student:
    # Student类，表示学生信息
    def __init__(self, name, age):
        # 初始化方法，设置学生姓名和年龄
        self.name = name
        self.age = age

    def __str__(self):
        # 返回学生的描述性字符串
        return f'{self.name} is {self.age} years old'

    def __lt__(self, other):
        # 小于运算符重载，用于比较学生的年龄
        return self.age < other.age

    def __eq__(self, other):
        # 比较是否相等
        return self.age == other.age

stu1 = Student("布恩迪亚", 18)
stu2 = Student("蕾梅黛丝", 14)

print(stu1)
print(stu2)

print(stu1 > stu2)

x = 1 # type: int