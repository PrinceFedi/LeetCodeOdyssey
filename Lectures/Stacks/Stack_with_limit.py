class Stack_Limit:

    def __init__(self, max_size):
        self.list = []
        self.max_size = max_size
        self.count = 0
    def __str__(self):
        if self.list:
            values = [str(x) for x in self.list]
            values = values[::-1]
            return "\n".join(values)
        return "Our stack does not exist"

    def isEmpty(self):
        if self.list is None:
            return True
        else:
            return False

    def isFull(self):
        if self.count == self.max_size:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            print("Yo our stack is full trying to push")
        else:
            self.list.append(value)
            self.count += 1
    def pop(self):
        if self.isEmpty():
            print("Yo our stack is empty trying to pop")
        else:
            self.list.pop()
            self.count -= 1

    def peek(self):
        if self.isEmpty():
            print("What is blud peeking at lol")
        else:
            return self.list[-1]

    def delete(self):
        self.list = []


stack_with_limit = Stack_Limit(3)
print(stack_with_limit.isFull())
stack_with_limit.isEmpty()
stack_with_limit.push(1)
stack_with_limit.push(2)
stack_with_limit.push(3)
stack_with_limit.push(4)
print(stack_with_limit.isFull())
print(stack_with_limit)
# #print(f"{stack_with_limit.peek()} this is our top")
# stack_with_limit.delete()
# print(stack_with_limit)
