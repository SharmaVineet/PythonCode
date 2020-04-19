class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def append_item(self, data):
        newNode = Node(data)
        if self.head:
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode

    def peek(self):
        print(self.head.data)
        pass

    def pop_item(self):
        self.head = self.head.next

    def print_stack(self):
        if self.head:
            current = self.head
            while current:
                print(current.data)
                current = current.next


s = Stack()
s.append_item("Harry Potter")
s.append_item("Game Of thrones")
s.append_item("Friends")
s.append_item("Breaking Bad")
s.append_item("Big Bang Theory")
s.print_stack()
# s.pop_item()
s.print_stack()
s.peek()
