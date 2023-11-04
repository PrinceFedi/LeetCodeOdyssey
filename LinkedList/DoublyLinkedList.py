class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def get_head(self):
        return self.head.value

    def get_tail(self):
        return self.tail.value

    def length(self):
        node = self.head
        length = 0
        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, value, location):
        if self.head is None:
            node = Node(value)
            node.next = None
            node.prev = None
            self.head = node
            self.tail = node
        else:
            new_node = Node(value)
            if location == 0:
                new_node.prev = None
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif location == -1 or location > dLL.length():
                new_node.next = None
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                curr_node = self.head
                index = 0
                while index < location - 1:
                    curr_node = curr_node.next
                    index += 1

                new_node.next = curr_node.next
                new_node.prev = curr_node
                curr_node.next = new_node
                if new_node.next is None:
                    self.tail = new_node
                else:
                    new_node.next.prev = new_node

    def traverse(self):
        if self.head is None:
            print("The list does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def reverse_traversal(self):
        if self.head is None:
            print("The list does not exist")
        else:
            node = self.tail
            while node is not None:
                print(node.value)
                node = node.prev

    def reverse(self):
        if self.head is None:
            print("This shit don't exist")
        previous = None
        current = self.head
        while current:
            previous = current.prev
            current.prev = current.next
            current.next = previous
            current = current.prev
        self.tail = self.head
        self.head = previous.prev

    def search(self, value):
        if self.head is None:
            print(f"The value {value} does not exist in this list")
        else:
            node = self.head
            index = 0
            while node is not None:
                if node.value == value:
                    return f"The value {value} is at index {index}"
                node = node.next
                index += 1
            return "The node does not exist"

    def delete(self, location):
        if self.head is None:
            print("There is no list to delete any elements")
        else:
            if location >= dLL.length():
                print("The given deletion index is greater then the length of the list")
            elif location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                curr_node = self.head
                index = 0
                while index < location - 1:
                    curr_node = curr_node.next
                    index += 1
                next_node = curr_node.next
                curr_node.next = next_node.next
                if curr_node.next is None:
                    self.tail = curr_node

    def clear(self):
        if self.head is None:
            print("There is no linked list to clear")
        else:
            self.head = None
            self.tail = None

dLL = DoublyLinkedList()
dLL.insert(1, 0)
dLL.insert(2, 1)
dLL.insert(3, 2)
dLL.delete(2)
dLL.insert(4, -1)
dLL.insert(5, 4)
# dLL.clear()
print(dLL.get_head())
print(dLL.get_tail())

#dLL.reverse_traversal()
# print(dLL.get_head())
# print(dLL.get_tail())
print([node.value for node in dLL])
#dLL.reverse()
# print(dLL.get_head())
# print(dLL.get_tail())
# print(dLL.search(4))
#
# print([node.value for node in dLL])
