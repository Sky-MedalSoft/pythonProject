from tortoise import Model, fields


class Student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, description="学生姓名")
    pwd = fields.CharField(max_length=50, description="学生密码")
    sCard = fields.CharField(max_length=50, description="学生身份")

    # 一对多
    clas = fields.ForeignKeyField('models.Clas', related_name='students', description="所属班级")

    # 多对多
    courses = fields.ManyToManyField('models.Course', related_name='classes', description="课程列表")


class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, description="课程名称")
    teacher = fields.ForeignKeyField('models.Teacher', related_name='courses', description="教师")


class Clas(Model):
    name = fields.CharField(max_length=50, description="班级名称")


class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, description="教师姓名")
