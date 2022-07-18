class Queue:
    q = []
    front = 0
    rear = -1

    def enqueue(self, value):
        self.q.append(value)
        self.rear += 1

    def dequeue(self):
        temp = self.q[self.front]
        self.q = self.q[self.front+1:self.rear]
        self.rear -= 1
        return temp

    def peek(self):
        return self.q[self.front]

queue1 = Queue()