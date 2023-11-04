class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def enqueue(self, data):

        while len(self.stack1) > 0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()
        self.stack1.append(data)

        while len(self.stack2) > 0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()

    def dequeue(self):

        if len(self.stack1) == 0:
            print("underflow")
            return
        else:
            val = self.stack1[-1]
            self.stack1.pop()
            return val


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.dequeue()
queue.dequeue()
print(queue.stack1)