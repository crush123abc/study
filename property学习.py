# class Student:
#     teacher_class='9'
#
#     def __init__(self, name):
#         self.age = 18
#         self.name = name
#         self.__teacher = '1'
#
#     @property#@property装饰器会将方法转换为相同名称的只读属性
#     def nnn(self):
#         return self.__teacher
#
#     @nnn.setter
#     def nnn(self, value):
#         if 6<len(value)<8:
#             self.__teacher = value
#
#
# if __name__ == '__main__':
#     s = Student('h')
#     print(s.__dict__)
#     # s.teacher = 'lisi'
#     # s.teacher = 'lisi2'
#     # print(s.__dict__)
#     print(s.nnn)
#     s.nnn='2222228'
#     print(s.nnn)
#     print(s.__dict__)
#     print(s.teacher_class)
#
#


# class Student:
#     teacher = "王老师"  # 类属性
#
#     def __init__(self):
#         self.name = "张三"  # 实例属性
#
#     def get_teacher(self):
#         return Student.teacher
#
#     @classmethod#classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的cls参数，可以来调类的属性，类的方法，实例化对象等
#     def get_aa(cls):
#         return cls.teacher
#
#
# if __name__ == '__main__':
#     s1 = Student()
#     s2 = Student()
#     s3 = Student()
#     s1.teacher = "张老师"
#     print(f'{s1.teacher}--{s2.teacher}--{s3.teacher}--{Student.teacher}')
#     Student.teacher = "小名"
#     print(f'{s1.teacher}--{s2.teacher}--{s3.teacher}--{Student.teacher}')
#     print(s1.get_teacher())
#     print(s1.get_aa())
#     print(Student.get_aa())


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.shengang = ''

    def getshenggao(self):
        return self.shengang
class ClassStudent:
    def __init__(self, name):
        self.name = name
        self.students = []
    def add_stu(self, student):
        self.students.append(student)

    def jiaoxuefei(self):
        for i in self.students:
            print(f"{self.name}通知{i.name}交钱")

    def maixiaofu(self):
        for i in self.students:
            print(i.getshenggao())


a = Student("zhangsan",18)
b = Student("lisi",19)
c = Student("wangwu",20)
cc1 = ClassStudent("学前班")

cc1.add_stu(a)
cc1.add_stu(b)
cc1.add_stu(c)


cc1.jiaoxuefei()