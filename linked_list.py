class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Linked_List:
    def __init__(self) -> None:
        self.start = None

    def insert(self, node: Node):
        if self.start == None:
            self.start = node
        else:
            temp_next = self.start
            while temp_next.next != None:
                temp_next = temp_next.next
            temp_next.next = node

    def insertAfter(self, element: int, value: int):
            temp_next = self.start
            while temp_next.value != element:
                temp_next = temp_next.next
            temp_next_next = temp_next.next
            newNode = Node(value)
            temp_next.next = newNode
            newNode.next = temp_next_next


    def Display(self):
        temp_next = self.start
        while temp_next.next != None:
            print (temp_next.value)
            temp_next = temp_next.next
        print (temp_next.value)    



LL = Linked_List()
LL.insert(Node(5))
LL.insert(Node(6))
LL.insert(Node(7))
LL.insert(Node(8))
LL.Display()
LL.insertAfter(6, 19)
LL.Display()