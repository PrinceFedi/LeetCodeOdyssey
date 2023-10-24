import Queue_Linked_List


class BSTnode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# -------------------------------------- insertion / deletion ----------------------------------------
def insert(root_node, value):
    if root_node is None:
        root_node.data = value
    elif value < root_node.data:
        if root_node.left is None:
            root_node.left = BSTnode(value)
        else:
            insert(root_node.left, value)
    else:
        if root_node.right is None:
            root_node.right = BSTnode(value)
        else:
            insert(root_node.right, value)
    return "Node has been inserted"

def min_value(bstnode):  # Need this to find the succesor
    current = bstnode
    while current.left is not None:
        current = current.left
    return current


def delete_node(root_node, value):
    if root_node is None:
        return root_node
    if value < root_node.data:
        root_node.left = delete_node(root_node.left, value)
    elif value > root_node.data:
        root_node.right = delete_node(root_node.right, value)
    else:
        if root_node.left is None:
            temp = root_node.right
            root_node = None
            return temp

        if root_node.right is None:
            temp = root_node.left
            root_node = None
            return temp
        temp = min_value(root_node.right)
        root_node.data = temp.data
        root_node.right = delete_node(root_node.right, temp.data)
    return root_node


# -------------------------------------- traversal/search  ----------------------------------------

def pre_order(root_node):
    if not root_node:
        return
    print(root_node.data)
    pre_order(root_node.left)
    pre_order(root_node.right)


def in_order(root_node):
    if not root_node:
        return
    in_order(root_node.left)
    print(root_node.data)
    in_order(root_node.right)


def post_order(root_node):
    if not root_node:
        return
    post_order(root_node.left)
    post_order(root_node.right)
    print(root_node.data)


def level_order(root_node):
    if not root_node:
        return "Tree does not exist"
    else:
        queue = Queue_Linked_List.Queue()
        queue.enqueue(root_node)
        while not queue.isEmpty():
            root = queue.dequeue()
            print(root.value.data)
            if root.value.left is not None:
                queue.enqueue(root.value.left)
            if root.value.right is not None:
                queue.enqueue(root.value.right)


def search(root_node, node_value):
    if root_node is None:
        return f"{node_value} does not exist in the tree"

    else:

        if root_node.data == node_value:
            return f"{root_node.data} is found"

            # Key is greater than root's key
        if root_node.data < node_value:
            return search(root_node.right, node_value)

            # Key is smaller than root's key
        return search(root_node.left, node_value)

def clear(root_node):
    root_node.data = None
    root_node.left = None
    root_node.right = None
    return "the tree is cleared"


new_bst = BSTnode(70)
print(insert(new_bst, 50))
print(insert(new_bst, 90))
print(insert(new_bst, 30))
print(insert(new_bst, 60))
print(insert(new_bst, 80))
print(insert(new_bst, 100))
print(insert(new_bst, 20))
print(insert(new_bst, 40))

print("\nThis is pre-order traversal")
pre_order(new_bst)
print("\nThis is in-order traversal")
in_order(new_bst)
print("\nThis is post-order traversal")
post_order(new_bst)
print("\nThis is level-order traversal")
level_order(new_bst)

delete_node(new_bst, 70)
print("\nthis is after deletion")
level_order(new_bst)

