class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None

    def insert_queue(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def remove_queue(self):
        if self.head:
            current = self.head
            self.head = self.head.next
            current.next = None

    def print_queue(self):
        if self.head:
            current = self.head
            while current:
                print(current.data)
                current = current.next

    def empty_queue(self):
        self.head = []

    def is_full(self):
        pass


q = Queue()
q.insert_queue("hello")
q.insert_queue("world")
q.insert_queue("This")
q.insert_queue("is")
q.insert_queue("Python")
q.print_queue()
q.empty_queue()
q.print_queue()
