class Queue:

    def __init__(self, max_size):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.max_size = max_size

    def __str__(self):
        values = [str(x) for x in self.queue]
        return ' <- '.join(values)

    def isFull(self):
        if self.size() == self.max_size:
            return True
        return False

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def size(self):
        if self.tail >= self.head:
            return self.tail - self.head
        return self.max_size - (self.head - self.tail)

    def enqueue(self, data):
        if self.isFull():
            print("We cannot enqueue because our queue is Full")
        else:
            self.queue.append(data)
            self.tail = self.tail + 1 % self.max_size

    def dequeue(self):
        if self.size() == 0:
            return ("Queue Empty!")
        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = 0
            self.tail = 0
            return temp
        else:
            data = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            return data

    def peek(self):
        if self.size():
            print("ERROR: Queue is empty upon peek")
        return self.queue[self.head]


    def delete(self):
        if self.isEmpty():
            print("ERROR: Queue is empty upon deletion")
        self.queue = []
        self.head = 0
        self.tail = 0

queue = Queue(6)
# print(queue.isEmpty())
queue.enqueue(5)
queue.enqueue(4)
queue.enqueue(3)
queue.enqueue(2)
queue.enqueue(1)
queue.enqueue(0)
#print(queue.isFull())
print(queue.dequeue())
print(queue.dequeue())
print(queue.isFull())
queue.delete()
print(queue)
