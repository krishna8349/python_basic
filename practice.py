# linked list program
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node('head')
        self.size = 0

    def getsize(self):
        return self.size

    def isEmpty(self):
        if self.size == 0:
            print('YES')
        print('No')

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            print('Stack is empty')
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)

    print(stack)
    print(stack.size)
    stack.isEmpty
    for i in range(1, 5):
        remove = stack.pop()
        print(f"Pop: {remove}")
        print(stack.getsize())
