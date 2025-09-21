"""
A Linked List is, as the word implies, a list where the nodes are linked together. Each node contains data and a pointer.
The way they are linked together is that each node points to where in the memory the next node is placed.


Linked Lists
A linked list consists of nodes with some sort of data, and a pointer, or link, to the next node.

[data|next] -> [data|next] -> [data|next] -> [data|next] -> null

A singly linked list.
A big benefit with using linked lists is that nodes are stored wherever there is free space in memory, the nodes do not have to be stored contiguously right after each other like elements are stored in arrays. Another nice thing with linked lists is that when adding or removing nodes, the rest of the nodes in the list do not have to be shifted.
"""
from src.basic.datatypes.casting.casting import height


# Singly linklist
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Only for doubly


class LinkList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("null")


# Doubly linklist
class DoublyLinkList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def print_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")


# Circular Single linklist
class CircularLinkList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next is not self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def display(self, count):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        i = 0
        lowest = current.data
        while i < count:
            if current.data < lowest:
                lowest = current.data
            print(current.data, end=" -> ")
            current = current.next
            i += 1
        print("None", end=" \n")
        print(f"Lowest value is: {lowest}", end="\n")


if __name__ == '__main__':
    # Singly
    print("---------------------- Singly ------------------------", end="\n")
    linkList = LinkList()
    linkList.add_node(1)
    linkList.add_node(2)
    linkList.add_node(3)
    linkList.display()
    # Doubly
    print("---------------------- Doubly ------------------------", end="\n")
    doubly = DoublyLinkList()
    doubly.add_node(11)
    doubly.add_node(12)
    doubly.add_node(13)
    doubly.print_forward()
    doubly.print_backward()
    # Circular
    print("---------------------- Circular ------------------------", end="\n")
    circular = CircularLinkList()
    circular.add_node(111)
    circular.add_node(112)
    circular.add_node(113)
    circular.display(4)
