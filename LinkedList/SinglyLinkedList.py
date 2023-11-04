


class Node:
    def __init__(self, value):
        """
        Constructor for Node class
        :param value: value to be stored in the node
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.value = value
        self.next = None

class SingleLinkedList:

    def __init__(self):
        """
        Constructor for SingleLinkedList class
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self) -> str:
        """
        Returns a string representation of the linked list
        """
        curr_node = self.head
        result = ""
        while curr_node is not None:
            result += str(curr_node.value)
            if curr_node.next is not None:
                result += " -> "
            curr_node = curr_node.next
        return result
    
    def __len__(self):
        """
        Returns the length of the linked list
        """
        return self.length
 
    def append(self, value):
        """
        Adds a node to the end of the linked list
        :param value: value to be stored in the node
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        """
        Adds a node to the beginning of the linked list
        :param value: value to be stored in the node
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next  = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        """
        Inserts a node at a given index
        :param index: index to insert the node
        :param value: value to be stored in the node
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr_node = self.head
            for _ in range(index-1):
                curr_node = curr_node.next
            # 
            new_node.next = curr_node.next 
            curr_node.next = new_node

            # If the new node is the last node, update the tail

            if new_node.next is None:
                self.tail = new_node
        self.length += 1

    def traverse(self): 


    
    





# Our main function
if __name__ == "__main__":
    new_linked_list = SingleLinkedList()
    new_linked_list.append(10)
    new_linked_list.append(5)
    new_linked_list.prepend(1)
    
    print(f"The length of my linked list is: {new_linked_list.length}")
    print(new_linked_list)



        





