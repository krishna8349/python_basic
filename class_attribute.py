class Student:
    school_name = 'abc school' #public class

    def __init__(self, name, age):
        self.name = name
        self.age = age

std = Student("krushna", 20)
print(std.name)
print(std.age)
print(std.school_name)

class Student:
    _school_name = 'abc school' #protected class

    def __init__(self,name,age):
        self._name = name
        self._age = age

stdp = Student("kp",21)
print(stdp._name)

class Student:
    __school_name = 'abc school' #private class

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def __display(self):
        print("this is private")

stdpp = Student("Ram",12)
# print(stdpp.__name)
print(stdpp.__display())