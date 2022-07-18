class Node2:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue1:
    head = None
    tail = None

    def enqueue(self, data):
        n = Node2(data)
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def dequeue(self):
        temp = self.head
        self.head = self.head.next
        print("Removed: ", temp)
        temp.value = None
        temp.next = None

    def peek(self):
        return self.head.value

queue2 = Queue1()