class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_size = 0

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def get_head(self):
        return self.head.value

    def get_tail(self):
        return self.tail.value

    def length(self):
        return self.current_size

    def insert(self, value, location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current_size += 1
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.current_size += 1
            elif location == -1 or location > single_linked_list.length():
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
                self.current_size += 1

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
                self.current_size += 1

    def delete(self, location):
        if self.head is None:
            print("There is no linked list")
        else:
            if location >= single_linked_list.length():
                print("Your deletion index is greater then the length of the list")
            elif location == 0:
                if self.current_size == 1:
                    self.head = None
                    self.tail = None
                    self.current_size = 0
                else:
                    self.head = self.head.next
                    self.current_size -= 1
            elif location == -1:
                if self.current_size == 1:
                    self.head = None
                    self.tail = None
                    self.current_size = 0
                else:
                    node_before_last = self.head
                    while node_before_last is not None:
                        if node_before_last.next == self.tail:
                            break
                        node_before_last = node_before_last.next
                    node_before_last.next = None
                    self.tail = node_before_last
                    self.current_size -= 1
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
                self.current_size -= 1

    def clear(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            self.head = None
            self.tail = None

    def traverse(self):
        if self.head is None:
            print("The list does not exist goofy")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def search(self, value):
        if self.head is None:
            return "The list does not exist"
        else:
            node = self.head
            index = 0
            while node is not None:
                if node.value == value:
                    return f"the value {node.value} is located at the index {index} in the linked list"
                node = node.next
                index += 1
            return "The value does not exist"

    def reverse(self):
        if self.head is None:
            print("Our list does not exist")
        else:
            previous = None
            current = self.head
            while current is not None:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            self.tail = self.head
            self.head = previous

single_linked_list = SinglyLinkedList()
single_linked_list.insert(1, 1)
single_linked_list.insert(2, 1)
single_linked_list.insert(3, 3)
single_linked_list.insert(4, 3)
single_linked_list.insert(5, 6)
single_linked_list.delete(4)
print(single_linked_list.get_head())
print(single_linked_list.get_tail())
print([node.value for node in single_linked_list])

# single_linked_list.traverse()
# print(single_linked_list.search(4))
#
# single_linked_list.reverse()
# print(single_linked_list.get_head())
# print(single_linked_list.get_tail())
# single_linked_list.delete(5)
# print(single_linked_list.length())
# print([node.value for node in single_linked_list])






