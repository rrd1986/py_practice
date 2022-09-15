

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def right_side_view(node: Node, level: int, level_hash: dict):
    if node is not None:
        level_hash[level] = node.val
        right_side_view(node.left, level + 1, level_hash)
        right_side_view(node.right, level + 1, level_hash)

def right_side_view_BT(root):
    if root is None:
        return
    level_hash = {}
    right_side_view(root, 1, level_hash)
    print(list(level_hash.values()))

'''

                 1


        2                  3


    4        5         6        7


                            8

'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
  
right_side_view_BT(root)
