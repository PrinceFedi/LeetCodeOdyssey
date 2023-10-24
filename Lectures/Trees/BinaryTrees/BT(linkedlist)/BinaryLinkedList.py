import Queue_Linked_List




class Treenode:

    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data


new_BT = Treenode("Drinks")
left_child = Treenode("Hot")
right_child = Treenode("Cold")
tea = Treenode("Tea")
coffee = Treenode("Coffee")
left_child.left = tea
left_child.right = coffee
new_BT.left = left_child
new_BT.right = right_child
fanta = Treenode("Fanta")
sprite = Treenode("Sprite")
right_child.left = fanta
right_child.right = sprite


# ------------------------------ Traversals -------------------------------------

def preorderTraversal(root):
    if not root:
        return
    print(root.data)
    preorderTraversal(root.left)
    preorderTraversal(root.right)


# preorderTraversal(new_BT)


def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.left)
    print(root.data)
    inOrderTraversal(root.right)


#inOrderTraversal(new_BT)


def postOrderTraversal(root):
    if not root:
        return
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data)


#postOrderTraversal(new_BT)


def levelOrderTraversal(root_node):
    if not root_node:
        return "The Binary does not exist"
    else:
        custom_queue = Queue_Linked_List.Queue()
        custom_queue.enqueue(root_node)
        while not (custom_queue.isEmpty()):
            root = custom_queue.dequeue()
            print(root.value.data)
            if root.value.left is not None:
                custom_queue.enqueue(root.value.left)
            if root.value.right is not None:
                custom_queue.enqueue(root.value.right)


# levelOrderTraversal(new_BT)


# ------------------------------ Search -------------------------------------

def searchBinarytree(root_node, value):
    if not root_node:
        return "The Binary does not exist"
    else:
        custom_queue = Queue_Linked_List.Queue()
        custom_queue.enqueue(root_node)
        while not (custom_queue.isEmpty()):
            root = custom_queue.dequeue()
            if root.value.data == value:
                return "Success"
            if root.value.left is not None:
                custom_queue.enqueue(root.value.left)
            if root.value.right is not None:
                custom_queue.enqueue(root.value.right)
        return "Not Found"


# print(searchBinarytree(new_BT, "Tea"))


# ------------------------------ Insert/Delete -------------------------------------


def insertNodeBT(root_node, new_node):
    if not root_node:
        rootNode = new_node
    else:
        customQueue = Queue_Linked_List.Queue()
        customQueue.enqueue(root_node)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.left is not None:
                customQueue.enqueue(root.value.left)
            else:  # This is our first open spot in our tree
                root.value.left = new_node
                return "Successfully inserted"
            if root.value.right is not None:
                customQueue.enqueue(root.value.right)
            else:
                root.value.right = new_node
                return "Successfully inserted"





