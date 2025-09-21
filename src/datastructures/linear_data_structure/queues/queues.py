"""
A queue is a data structure that can hold many elements.
Think of a queue as people standing in line in a supermarket.

The first person to stand in line is also the first who can pay and leave the supermarket. This way of organizing elements is called FIFO: First In First Out.

Basic operations we can do on a queue are:

Enqueue: Adds a new element to the queue.
Dequeue: Removes and returns the first (front) element from the queue.
Peek: Returns the first element in the queue.
isEmpty: Checks if the queue is empty.
Size: Finds the number of elements in the queue.
Experiment with these basic operations in the queue animation above.

Queues can be implemented by using arrays or linked lists.

Queues can be used to implement job scheduling for an office printer, order processing for e-tickets, or to create algorithms for breadth-first search in graphs.

"""


class Queue:
    def __init__(self):
        self.queue = []

    # Add elements in queue (In last) using append
    def enqueue(self, data):
        self.queue.append(data)

    # Remove first element from queue
    def dequeue(self):
        return self.queue.pop(0)

    # Get Size
    def size(self) -> int:
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    # Remove using loop
    def dequeue_all(self):
        if not self.is_empty():
            while not self.is_empty():
                self.queue.pop(0)
        else:
            return None
    # Get Top element which is first element at 0
    def peek(self):
        if not self.is_empty():
           return self.queue.__getitem__(0)
    def display(self):
        for i in range(self.size()):
            print(f" {self.queue[i]} ",end= "->")
        print("\n")
if __name__ == '__main__':
    myQueue = Queue()

    myQueue.enqueue('A')
    myQueue.enqueue('B')
    myQueue.enqueue('C')
    print("Queue: ", myQueue.queue)

    print("Dequeue: ", myQueue.dequeue())
    myQueue.display()
    print("Peek: ", myQueue.peek())

    print("isEmpty: ", myQueue.is_empty())

    print("Size: ", myQueue.size())
    myQueue.dequeue_all()

