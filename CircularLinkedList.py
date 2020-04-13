# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

    # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head
        else:
            self.head = newNode
            newNode.next = self.head

    def delete(self, key):
        if self.head:
            current = self.head
            if current.next == self.head:
                self.head = None
            elif current.data == key:
                self.head = current.next
            else:
                while current.next != self.head:
                    if current.next.data == key:
                        current.next = current.next.next
                        return
                    current = current.next
                print("Value {} not found in List".format(key))

    # print method for the linked list
    def printLL(self):
        current = self.head
        while current:
            print(current.data)
            if current.next == self.head:
                break
            current = current.next


# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()
