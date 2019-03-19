#! python3
# Implementations of a queue (first-in, first-out)

from stack import stack

# standard first-in, first-out implementation
class queue():

    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.queue == 0

    def enqueue(self, x):
        self.queue.insert(0, x)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def head(self):
        if self.is_empty():
            return None
        else:
            return self.queue[-1]

    def tail(self):
        if self.is_empty():
            return None
        else:
            return self.queue[0]

# implementation of a queue as two stacks
class stack_queue():
    
    s = stack()
    temp = stack()

    def __init__(self):
        self.queue = self.s.stack

    def size(self):
        return self.s.size()

    def is_empty(self):
        return self.s.is_empty()

    # method turns one stack upside down into the other (think of a pile of plates
    # being inverted)
    def stack_swap(self):
        if self.size() != 0:
            for i in range(0, self.size()):
                self.temp.push(self.s.pop())
        elif self.temp.size() != 0:
            for i in range(0, self.temp.size()):
                self.s.push(self.temp.pop())

    # in order for the enqueued element to be in last, we invert the queue stack,
    # push the new element to this inverted stack, and invert the result once more
    def enqueue(self, x):
        self.stack_swap()
        self.temp.push(x)
        self.stack_swap()

    def dequeue(self):
        if self.size() == 0:
            return None
        else:
            return self.queue.pop()
    
    def head(self):
        if self.is_empty():
            return None
        else:
            return self.queue[-1]

    def tail(self):
        if self.is_empty():
            return None
        else:
            return self.queue[0]
