
# Delete a Node
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class Linklist:

    def __init__(self):
        self.head = None

    def add_node_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(f"{current.data}",end="->")
            current = current.next
        print("null")

    # Insert node at a specific position
    def insert_at_specific_position(self,data,position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        # Traverse until the node just before position
        while current and count < position-1:
            current = current.next
            count+=1
        if not current:
            print(f"Position {position} out of range, inserting at end.")
            self.add_node_at_end(data)
            return
        new_node.next = current.next
        current.next = new_node


    # Delete a specific node
    def delete_node(self,data):
        # Check if deleted item is head or not
        current = self.head
        if current and current.data is data:
            self.head = current.next
            current = None
            return
        # Check if deleted Item is in middle or in last
        prev = None
        while current and current.data is not data:
            prev = current
            current = current.next
        prev.next = current.next
        current = None

        if current is None:
            return

if __name__ == '__main__':
    print("---------------------- Singly ------------------------", end="\n")
    linkList = Linklist()
    linkList.add_node_at_end(1)
    linkList.add_node_at_end(2)
    linkList.add_node_at_end(3)
    linkList.display()
    linkList.delete_node(3)
    linkList.display()

    # Insert at start
    linkList.insert_at_specific_position(22,1)
    linkList.display()