"""
Stacks
A stack is a data structure that can hold many elements, and the last element added is the first one to be removed.

Like a pile of pancakes, the pancakes are both added and removed from the top. So when removing a pancake, it will always be the last pancake you added. This way of organizing elements is called LIFO: Last In First Out.

Basic operations we can do on a stack are:

Push: Adds a new element on the stack.
Pop: Removes and returns the top element from the stack.
Peek: Returns the top (last) element on the stack.
isEmpty: Checks if the stack is empty.
Size: Finds the number of elements in the stack.
Stacks can be implemented by using arrays or linked lists.

Stacks can be used to implement undo mechanisms, to revert to previous states, to create algorithms for depth-first search in graphs, or for backtracking.

Stacks are often mentioned together with Queues, which is a similar data structure described on the next page.
"""
from inspect import stack

print("-------------------- Stacks ----------------------\n")


class Stack:
    def __init__(self):
        self.stack = []

    # Add elements in stack using append
    def add_elements(self, data):
        self.stack.append(data)

    # insert at specific position in stack using insert
    def insert(self, data, position):
        self.stack.insert(position, data)

    # Stack size
    def get_stack_size(self):
        return len(self.stack)

    # Return top element of stack
    def get_top_element(self):
        return self.stack[-1]

    # Remove and return top element from stack
    def get_element(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        else:
            return "Stack is empty"

    # Remove certain element from stack
    def get_certain_element(self, data):
        found = False
        if len(self.stack) != 0:
            for i in range(len(self.stack)):
                if self.stack[i] is data:
                    found = True

            if not found:
                return "No data is found"
            elif found:
                return data

        else:
            return "Stack is empty"

    # Remove from certain position
    def remove_from_certain_position(self, position):
        if len(self.stack) != 0:
            return self.stack.pop(position)
        else:
            return "Stack is empty"
    def display_stack(self):
        for i in self.stack:
            print(f" {i} ",sep= "",end="->")

if __name__ == '__main__':
    stack = Stack()
    print("\n---------------------- Append elements ------------------------", end="\n")
    stack.add_elements(1)
    stack.add_elements(2)
    stack.add_elements(4)
    stack.display_stack()
    print("\n---------------------- insert elements ------------------------", end="\n")
    stack.insert(3,2)
    stack.display_stack()
    print("\n---------------------- Get Stack Size ------------------------", end="\n")
    print(f"Stack Size:: {stack.get_stack_size()}")

    print("\n---------------------- Get Stack Top element ------------------------", end="\n")
    print(f"Stack Top element:: {stack.get_top_element()}")

    print("\n---------------------- Get Stack Top element ------------------------", end="\n")
    print(f"Stack Top element:: {stack.get_certain_element(2)}")
    stack.display_stack()
    print("\n---------------------- Remove element from certain position ------------------------", end="\n")
    print(f"Stack Top element:: {stack.remove_from_certain_position(2)}")
    stack.display_stack()