

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def Pre_Order(root):
    if root is None:
        return []
    return Pre_Order(root.left) + [root.val] + Pre_Order(root.right)

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
  
print(Pre_Order(root))