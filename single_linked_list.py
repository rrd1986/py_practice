class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.start = None

    def insertEnd(self, data):
        if self.start == None:
            self.start = Node(data)
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = Node(data)
    
    def insertBegin(self, data):
        if self.start == None:
            self.start = Node(data)
        else:
            startNode = Node(data)
            startNode.next = self.start
            self.start = startNode

    def delete(self, data):
            if self.start.value == data:
                self.start = self.start.next
            else:
                tempPrev = self.start
                tempCurrent = self.start.next
                while tempCurrent != None:
                    if tempCurrent.value == data:
                        tempPrev.next = tempCurrent.next
                        break
                    tempPrev = tempPrev.next
                    tempCurrent = tempCurrent.next

    def display(self):
        temp = self.start
        while temp != None:
            print(temp.value)
            temp = temp.next

    def display(self, node):
        while node.next != None:
            print(node.value)
            node = node.next

if __name__ == "__main__":
    sll = SingleLinkedList()
    sll.insertEnd(3)
    sll.insertEnd(4)
    sll.insertEnd(5)
    sll.insertEnd(6)
    #sll.display()
    sll.insertBegin(10)
    sll.insertBegin(11)
    #sll.display()
    sll.delete(5)
    sll.delete(4)
    sll.display(sll.start)




                    





