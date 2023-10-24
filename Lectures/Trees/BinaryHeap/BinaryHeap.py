class Heap:

    def __init__(self, size):
        self.list = (size + 1) * [None]
        self.heap_size = 0
        self.max_size = size + 1


def peek(root_node):
    if not root_node:
        return
    return root_node.list[1]


def size(root_node):
    if not root_node:
        return
    return root_node.heap_size


def preorder_traversal(heap, i, result):
    if i >= heap.max_size:
        return
    result.append(heap[i])
    preorder_traversal(heap, 2 * i + 1, result)
    preorder_traversal(heap, 2 * i + 2, result)


def postorder_traversal(heap, i, result):
    if i >= heap.max_size:
        return
    postorder_traversal(heap, 2 * i + 1, result)
    postorder_traversal(heap, 2 * i + 2, result)
    result.append(heap[i])


def inorder_traversal(heap, i, result):
    if i >= heap.max_size:
        return
    inorder_traversal(heap, 2 * i + 1, result)
    result.append(heap[i])
    inorder_traversal(heap, 2 * i + 2, result)


def level_order_traversal(root_node):
    if not root_node:
        return
    else:
        for i in range(1, root_node.heap_size + 1):
            print(root_node.list[i])


