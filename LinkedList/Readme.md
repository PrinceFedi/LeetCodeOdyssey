# Linked List

## What is a Linked List?

 A `Linked List` is a data structure which is comprised of a sequential collection of nodes, that does not have to be in order. Each node may contain any type of data and each node has a reference to the next node in the chain.

 Example: We can resemble it as a train 

- Both Trains and Linked List have both an `Head` & a `Tail`.
    - Head -> First node in our linked list
    - Tail -> Last node of linked list 

- Each Node/Train car is independent

- Nodes and Cars have data and links to the next node stored within. 
    - Passengers == Data
    - The links (next pointer) store the memory reference point to next node.


## Linked List vs Array List

### Python Lists

- Lists in python can be accessed through indexing

- Each element is stored contigious in memory

### Linked List

- Linked lists do not have index values to reference them

- Nodes are not stored in contigiously but are rather spread out in different places in memory.

    - In order to reference these points in memory, we use a pointer to track the next sequential node. Each node points to the next iteration with our last node pointing to NULL.

Time Complexity:
