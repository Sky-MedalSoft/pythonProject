# 工厂模式
class Person:
    pass
class Student(Person):
    pass

class Teacher(Person):
    pass
class Worker(Person):
    pass

class Factory:
    def create_class(self, class_type):
        if class_type == 'Student':
            return Student()
        elif class_type == 'Teacher':
            return Teacher()
        elif class_type == 'Worker':
            return Worker()

fac = Factory()
print(id(fac.create_class(Teacher)))