class Stack:

    def __init__(self):
        self.list = []

    def __str__(self):
        if self.list:
            values = [str(x) for x in self.list]
            values = values[::-1]
            return '\n'.join(values)
        return "Our stack does not exist"

    def isEmpty(self):
        if self.list is None:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack to pop"
        return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "there is nothing in this stack to peek at"
        else:
            return self.list[-1]

    def clear(self):
        self.list = None


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
print(stack.peek())
print(stack)
