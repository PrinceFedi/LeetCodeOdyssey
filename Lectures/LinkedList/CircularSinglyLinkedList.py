class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            if node == self.head:
                break

    def get_head(self):
        return self.head.value

    def get_tail(self):
        return self.tail.value

    def length(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            if node == self.tail:
                break
            node = node.next
        return count

    def insert(self, value, location):
        if self.head is None:
            node = Node(value)
            node.next = node
            self.head = node
            self.tail = node
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif location == -1 or location > circularSLL.length():
                new_node.next = self.tail.next
                self.tail.next = new_node
                self.tail = new_node
            else:
                curr_node = self.head
                index = 0
                while index < location - 1:
                    curr_node = curr_node.next
                    index += 1
                new_node.next = curr_node.next
                curr_node.next = new_node
                if curr_node == self.tail:
                    self.tail = new_node

    def traverse(self):
        if self.head is None:
            print("the list does not exist")
        node = self.head
        while node is not None:
            print(node.value)
            if node == self.tail:
                break
            node = node.next

    def search(self, value):
        if self.head is None:
            print("the list does not exist")
        else:
            node = self.head
            index = 0
            while node is not None:
                if node.value == value:
                    return f"The value {node.value} is found at index {index}"
                index += 1
                if node == self.tail:
                    break
                node = node.next
            return f"The value {value} does not exist"

    def delete(self, location):
        if self.head is None:
            print("Make your list")
        else:
            if location >= circularSLL.length():
                print(f"The deletion index {location} is bigger then the list")
            elif location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node_before_tail = self.head
                    while node_before_tail is not None:
                        if node_before_tail.next == self.tail:
                            break
                        node_before_tail = node_before_tail.next
                    node_before_tail.next = self.head
                    self.tail = node_before_tail
            else:
                curr_node = self.head
                index = 0
                while index < location-1:
                    curr_node = curr_node.next
                    index += 1
                next_node = curr_node.next
                curr_node.next = next_node.next
                if curr_node.next == self.head:
                    self.tail = curr_node

    def clear(self):
        if self.head is None:
            print("No list exist")
        else:
            self.head = None
            self.tail.next = None
            self.tail = None

    def reverse(self):
        if self.head is None:
            print("There is no list to reverse")
        previous = None
        current = self.head

        # Before our loop lets move to the second node in our list so our termination expression can work
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

        while current != self.head:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.tail = self.head  # In reverse order the first element is now the last and vice-versa
        self.head = previous  # Since we are reversing are list, our previous tail is now our head.
        self.tail.next = previous  # the next of tail is the head and previous is our new head after reversing


circularSLL = CircularSinglyLinkedList()
circularSLL.insert(0, 0)
circularSLL.insert(2, 1)
circularSLL.insert(10, -1)
circularSLL.delete(2)
circularSLL.insert(3, 3)
circularSLL.insert(1, -1)
# print(circularSLL.get_head())
# print(circularSLL.get_tail())
print([node.value for node in circularSLL])
# circularSLL.reverse()
# print(circularSLL.get_head())
# print(circularSLL.get_tail())
# print(circularSLL.search(1))
# circularSLL.delete(10)
# print(circularSLL.get_head())
# print(circularSLL.get_tail())
# circularSLL.clear()
# print([node.value for node in circularSLL])

