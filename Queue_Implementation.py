class Queue:
    def __init__(self):
        self.lst = []

    def insert_queue(self, val):
        self.lst.append(val)

    def remove_queue(self):
        if self.lst:
            self.lst.pop(0)

    def is_empty(self):
        return self.lst == []

    def print_queue(self):
        return self.lst

    def empty_queue(self):
        self.lst = []


q = Queue()
q.insert_queue("hello")
q.insert_queue("my")
q.insert_queue("name")
q.insert_queue("is")
q.insert_queue("James Bond")
print(q.print_queue())
print(q.is_empty())
q.empty_queue()
print(q.is_empty())
