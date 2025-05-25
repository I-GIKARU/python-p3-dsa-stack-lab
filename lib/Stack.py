class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            self.items = []
        else:
            self.items = list(items)  # make a copy to avoid shared mutable list
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        # Only push if not full
        if not self.full():
            self.items.append(item)
        else:
            # If full, ignore the push (as tests show no error, just no add)
            pass

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return self.size() >= self.limit

    def search(self, target):
        # How far from the top is target?
        # Top element has index -1 and distance 0
        # So distance = (size - 1) - index_of_target
        if target not in self.items:
            return -1
        index = self.items.index(target)
        return self.size() - 1 - index
