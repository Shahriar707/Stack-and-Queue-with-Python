class Stack:
    stack = []
    pointer = -1
    def push(self,element):
        self.stack.append(element)
        self.pointer += 1
    def peek(self):
        return (self.stack[self.pointer])
    def pop(self):
        value = self.stack[self.pointer]
        self.stack = self.stack[:-1]
        self.pointer -= 1
        return value

stack1 = Stack()