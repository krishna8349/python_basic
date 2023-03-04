class Stack():
    def __init__(self):
        self.item = []

    def add(self,element):
        self.item.append(element)
        print(element)

    def pop(self):
        self.item.pop()
    
    def peek(self):
        print(self.item[0])

    def size(self):
        print(len(self.item))

stack = Stack()

stack.add(10)
stack.add(2)
stack.add(4)
stack.size()
stack.pop()
stack.size()
stack.peek()