class QueueTwoStacks(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self, ite,):
        if len(self.out_stack) == 0:

            # Move items from in_stack to out_stack reversing order

            while len(self.in_stack) > 0:
                newest_item_in_stack = self.in_stack.pop()
                self.out_stack.append(newest_item_in_stack)


            # If out_stack is still empty raise error
            if len(self.out_stack) == 0:
                raise IndexError

        return self.out_stack.pop()