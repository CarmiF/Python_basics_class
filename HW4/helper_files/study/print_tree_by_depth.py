"""
This script is part of introduction of computer science for EE students.
"""
from binary_tree import Node


def print_by_depth(root):
    # Base Case
    if root is None:
        return

    # Create a queue for level order traversal and enqueue root
    queue = [root]

    while len(queue) > 0:
        # Print front of queue and remove it from queue
        node = queue.pop(0)
        print(node.data)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(16)
root.insert(3)
root.insert(8)

root.display()  # What is the order of printing
print('Naive order printing')
root.print_tree()  # What is the order of printing
print('print by depth:')
print_by_depth(root)
