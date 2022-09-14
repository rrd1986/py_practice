class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, node):
        self.root = node

    def display(self, node):
        if node != None:
            print(node.data)
            self.display(node.left)
            self.display(node.right)

    def preorder(self, node):
        if node == None:
            return []
        return self.preorder(node.left) + [node.data] + self.preorder(node.right)

    def inorder(self, node):
        if node == None:
            return []
        return  [node.data] + self.inorder(node.left) + self.inorder(node.right)



if __name__ == "__main__":
    BT = BinaryTree(Node(10))
    BT.root.left = Node(20)
    BT.root.right = Node(30)
    BT.root.left.left = Node(40)
    BT.root.left.right = Node(50)

    BT.display(BT.root)
    po = BT.preorder(BT.root)
    print(po)
    io = BT.inorder(BT.root)
    print(io)

