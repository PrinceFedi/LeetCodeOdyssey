class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class Linkedlist:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Queue:

    def __init__(self):
        self.linked_list = Linkedlist()

    def __str__(self):
        values = [str(x.value) for x in self.linked_list]
        return '->'.join(values)

    def isEmpty(self):
        if self.linked_list.head is None:
            return True
        return False

    def enqueue(self, value):
        node = Node(value)
        if self.isEmpty():
            self.linked_list.head = node
            self.linked_list.tail = node
        else:
            self.linked_list.tail.next = node
            self.linked_list.tail = node

    def dequeue(self):
        if self.linked_list.head is None:
            return None
        else:
            node = self.linked_list.head
            if self.linked_list.head == self.linked_list.tail:
                self.linked_list.head = None
                self.linked_list.tail = None
            else:
                self.linked_list.head = self.linked_list.head.next
        return node

    def peek(self):
        if self.isEmpty():
            print("There is no node in the queue to check its head")
        return self.linked_list.head


queue = Queue()
queue.enqueue(1)
print(queue.isEmpty())
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue)
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

print(queue.isEmpty())
print(queue)
