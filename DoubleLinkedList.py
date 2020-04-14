class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            newNode.prev = current
        else:
            self.head = newNode

    def prepend(self, data):
        if self.head:
            newNode = Node(data)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def printDLL(self):
        if self.head:
            current = self.head
            while current:
                print(current.data)
                current = current.next


DLL = DoubleLinkedList()
DLL.append(1)
DLL.append(2)
DLL.append(3)
DLL.append(4)
DLL.prepend(0)
DLL.prepend(-1)
DLL.printDLL()
