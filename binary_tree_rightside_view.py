import queue

# This solution is not correct

# A binary tree node
class Node:
      
    # A constructor to create a new 
    # Binary tree Node
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.label_rightmost = None

# Function to print Right view of
# binary tree
def rightView(root):
      
    if root is None:
        return

    q = queue.Queue()
    q.put(root)

    while q.qsize() > 0:
            node = q.get()
            #print(f'Queue size: {q.qsize()}')
            if node.label_rightmost == True:
                print(f'{node.data} \n')
            if node.left:
                q.put(node.left)
            if node.right:
                node.right.label_rightmost = True
                q.put(node.right)

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
  
rightView(root)