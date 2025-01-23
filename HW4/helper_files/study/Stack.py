from copy import copy


class MyStack:
    def __init__(self):
        self.stack_vals = []
        self.len = 0

    def push(self, val):
        self.stack_vals.append(val)
        self.len += 1

    def pop(self):
        if self.is_empty():
            return None
        to_pop = self.stack_vals[-1]
        self.stack_vals = self.stack_vals[:-1]
        self.len -= 1
        return to_pop

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_vals[-1]

    def reverse_stack(self):
        """Reverse the stack"""
        temp = copy(self)
        # Empty stack
        while not self.is_empty():
            self.pop()
        # move from temp to stack
        while not temp.is_empty():
            self.push(temp.pop())

    def __len__(self):
        return self.len

    def is_empty(self):
        return not self.len

    def __repr__(self):
        return str(self.stack_vals) + " <-- head"
