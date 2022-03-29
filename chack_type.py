class Class1:
    def m(self):
        print("In Class1") 
      
class Class2(Class1):
    def m(self):
        print("In Class2")
 
class Class3(Class1):
    def m(self):
        print("In Class3")    
     
class Class4(Class3, Class2):
    pass
 
obj = Class4()
obj.m()

n = [1,2,3,4,5]

s = ""

for i in n:
    # if i <=n:
    s = s + str(i)

print(s)