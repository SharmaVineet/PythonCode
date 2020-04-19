class Stack():
    def __init__(self):
        self.items = []

    def append_item(self, item):
        self.items.append(item)

    def pop_item(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def delete_stack(self):
        self.items = []

    def print_stack(self):
        return self.items


s = Stack()
s.append_item("Harry Potter")
s.append_item("Game Of thrones")
s.append_item("Friends")
s.append_item("Breaking Bad")
s.append_item("Big Bang Theory")
print(s.print_stack())
print(s.pop_item())
print(s.print_stack())
s.delete_stack()
print(s.print_stack())
