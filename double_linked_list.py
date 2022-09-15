class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Doubly_Linked_List:
    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        newNode = Node(data) 
        if self.head == None:
            self.head = newNode
        else:
            last = self.head
            while last.next != None:
                last = last.next
            last.next = newNode
            last.prev = last


    def listprint(self, node):
        while (node is not None):
            print(node.value)
            last = node
            node = node.next



if __name__ == "__main__":
    dllist = Doubly_Linked_List()

    dllist.insertEnd(9)
    dllist.insertEnd(45)

    dllist.listprint(dllist.head)