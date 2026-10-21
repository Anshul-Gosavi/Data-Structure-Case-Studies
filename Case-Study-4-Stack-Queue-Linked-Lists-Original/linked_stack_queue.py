class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.top is None:
            return None
        return self.top.value

    def display(self):
        items = []
        current = self.top
        while current is not None:
            items.append(current.value)
            current = current.next
        return " -> ".join(items) if items else "(empty)"


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            return None
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        if self.front is None:
            return None
        return self.front.value

    def display(self):
        items = []
        current = self.front
        while current is not None:
            items.append(current.value)
            current = current.next
        return " -> ".join(items) if items else "(empty)"


def main():
    stack = Stack()
    print("STACK OF PLATES (LIFO)")
    for plate in ["Plate 1", "Plate 2", "Plate 3"]:
        stack.push(plate)
        print("Push:", plate)
    print("Top to bottom:", stack.display())
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    print("After pop:", stack.display())

    queue = Queue()
    print("\nCUSTOMER QUEUE (FIFO)")
    for customer in ["Customer A", "Customer B", "Customer C"]:
        queue.enqueue(customer)
        print("Join:", customer)
    print("Front to rear:", queue.display())
    print("Peek:", queue.peek())
    print("Serve:", queue.dequeue())
    print("After serving:", queue.display())


if __name__ == "__main__":
    main()
