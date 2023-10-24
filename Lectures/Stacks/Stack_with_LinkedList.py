class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


class Stack:

    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        if stack.isEmpty():
            self.LinkedList.head = node
        else:
            node.next = self.LinkedList.head
            self.LinkedList.head = node

    def pop(self):
        if stack.isEmpty():
            print("No value to pop")
        else:
            node_value = self.LinkedList.head  # the value that we are popping
            self.LinkedList.head = self.LinkedList.head.next
            return node_value

    def peek(self):
        if stack.isEmpty():
            print("No value to peek")
        else:
            return self.LinkedList.head

    def clear(self):
        if stack.isEmpty():
            print("Our list is empty")
        else:
            self.LinkedList.head = None


stack = Stack()
print(stack.isEmpty())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
stack.pop()
print(stack.peek())
print(stack)
stack.clear()
stack.pop()
print(stack)
