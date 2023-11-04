class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):
        if self.items:
            values = [str(x) for x in self.items]
            return ''.join(values)
        return "Queue is empty"

    def isEmpty(self):
        if self.items:
            return False
        return True

    def enqueue(self, value):
        return self.items.append(value)

    def dequeue(self):
        if self.isEmpty():
            print("Yo your queue is empty")
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            print("Nothing to peek at")
        return self.items[0]

    def clear(self):
        if self.isEmpty():
            print("Nothing to clear")
        self.items = None
