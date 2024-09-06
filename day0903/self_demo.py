class Student:
    name = None

    def sayHello(self):
        print(f'我是{self.name}')

stu = Student()
stu.name = "111"
stu.sayHello()

import winsound
winsound.Beep(1000,1000)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("init自动")

p1 = Person("小明",10)