class stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]
