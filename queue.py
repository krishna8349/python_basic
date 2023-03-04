class Queue:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        if len(self.item)==0:
            print('Is empyty')
        else:
            print('Not empty')

    def add(self,element):
        self.item.append(element)
        print(element)

    def dequeue(self):
        return self.item.pop(0)

    def size(self):
        print(len(self.item))

    def peek(self):
        print(self.item[-1])

queue = Queue()


queue.add(1)
queue.isEmpty()
queue.add(5)
queue.add(3)
queue.peek()
queue.dequeue()
queue.dequeue()
queue.size()