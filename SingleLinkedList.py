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

    # insertion stat of the linked list
    def insert_prefix(self, data):
        newNode = Node(data)
        current = newNode
        current.next = self.head
        self.head = newNode

    def insert_in_between(self, data, location):
        count = 1
        current = self.head
        while current.next:
            if count == location - 1:
                newNode = Node(data)
                newNode.next = current.next
                current.next = newNode
                return
            current = current.next
            count += 1

    # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def search_in_list(self, value):
        count = 1
        if self.head:
            current = self.head
            while current.next:
                if current.data == value:
                    print("Value found at node {} and at location {}".format(count, current))
                    return
                current = current.next
                count += 1
            print("Value not found!!")

    def delete(self, key):
        if self.head:
            current = self.head
            if current.next is None:
                self.head = None
            elif current.data == key:
                self.head = current.next
            else:
                while current.next:
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
            current = current.next


# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(3)
LL.insert(4)
# LL.insert(5)
# LL.insert_prefix(2)
# LL.insert_prefix(1)
# LL.insert_in_between(3.5, 4)
# LL.insert_in_between(2.5, 3)
# LL.insert_in_between(0.5, 1)
print("List before Deletion")
LL.printLL()
# LL.search_in_list(6)
LL.delete(4)
print("List after Deletion")
LL.printLL()
