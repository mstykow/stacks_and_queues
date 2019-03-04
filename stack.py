#! python3
# Implementation of a stack (last in, first out)

class stack():

    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]