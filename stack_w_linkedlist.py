class Node1:
    def __init__(self,value):
        self.value = value
        self.ref = None

class Stack1:
    head = None
    def push(self, data):
        if self.head==None:
            self.head= Node1(data)
        else:
            n = Node1(data)
            n.ref = self.head
            self.head = n
    def peek(self):
        return(self.head.value)
    def pop(self):
        temp = self.head
        self.head = self.head.ref
        temp.value = None
        temp.ref = None

stack2 = Stack1()
