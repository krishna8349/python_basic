from re import A


class Parent:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b

class Child(Parent):
    def add(self):
        return self.a * self.b  * self.c

# parent = Parent(2,4)
# print(parent.add())

child = Child(2,3,4)
print(child.add())