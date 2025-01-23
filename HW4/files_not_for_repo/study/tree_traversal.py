"""
This script is part of introduction of computer science for EE students.
"""


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:  # if new data is smaller insert in left
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:  # if new data is larger insert in right
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def display(self):
        lines, _, _, _ = self._display_recursive()
        for line in lines:
            print(line)

    def _display_recursive(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root. this is
           a utility function that gets used by the <display()> method for building pretty stdout
           visualization of the binary tree. """

        # No child exists.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child exists.
        if self.right is None:
            lines, n, p, x = self.left._display_recursive()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child exists.
        if self.left is None:
            lines, n, p, x = self.right._display_recursive()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children exist.
        left, n, p, x = self.left._display_recursive()
        right, m, q, y = self.right._display_recursive()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '

        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)

        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    # In order traversal
    def in_order_traversal(self):
        result = []
        if self.left:
            result.extend(self.left.in_order_traversal())
        result.append(self.data)
        if self.right:
            result.extend(self.right.in_order_traversal())
        return result

    # pre order traversal
    def pre_order_traversal(self):
        result = [self.data]
        if self.left:
            result.extend(self.left.pre_order_traversal())
        if self.right:
            result.extend(self.right.pre_order_traversal())
        return result

    # post order traversal
    def post_order_traversal(self):
        result = []
        if self.left:
            result.extend(self.left.post_order_traversal())
        if self.right:
            result.extend(self.right.post_order_traversal())
        result.append(self.data)
        return result


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.display()
print(root.in_order_traversal())
print(root.pre_order_traversal())
print(root.post_order_traversal())
