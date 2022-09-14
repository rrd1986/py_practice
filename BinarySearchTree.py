class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

class BinaryTree:
    def __init__(self,node):
        self.root = node

    def insert(self, node, value):
        if node.left == None and node.value > value:
            node.left = Node(value)
            return
        if node.right == None and node.value < value:
            node.right = Node(value)
            return            
        elif node.value < value:
            self.insert(node.right, value)
        elif node.value > value:
            self.insert(node.left, value)

    def traverse(self,node):
        if node != None:
            print(node.value)
            self.traverse(node.left)
            self.traverse(node.right)


if __name__ == "__main__":
    N1 = Node(5)
    print(N1)
    B = BinaryTree(N1)
    B.insert(N1, 10)
    B.insert(N1, 20)
    B.insert(N1, 15)
    B.insert(N1, 3)
    B.insert(N1, 99)
    B.insert(N1, 25)
    B.insert(N1, 60)

    B.traverse(N1)
    
