
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root):
        self.root = Node(root)

    def traverse(self, node):
        if node != None:
            print(node.val)
            self.traverse(node.left)
            self.traverse(node.right)

def right_View(root, temp_prev= None):
    #temp_prev = None
    if root != None:
        Right_view.append(root.val)
        temp_prev = root
        right_View(root.right, temp_prev= temp_prev)
    else:
        if temp_prev != None:
            right_View(temp_prev.left)



#           5
#
#     7               10
#
#12       24         


if __name__ == "__main__":
    T = Tree(5)
    T.root.left = Node(7)
    T.root.right = Node(10)
    T.root.left.left = Node(12)
    #T.root.left.right = Node(24)
    T.root.right.left = Node(24)

    T.traverse(T.root)


    Right_view = [] 
    right_View(T.root)
    print(Right_view)



    
