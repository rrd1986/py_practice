
class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []
        self.current_size = 0

    def push(self, val):
        if self.current_size < self.max_size:
            self.stack.append(val)
            self.current_size += 1
        else:
            print("stack is full")

    def display(self):
        for i in range (self.max_size - self.current_size):
            print("____")
            print (f'|   |')            

        for i in self.stack[::-1]:
            print("____")
            print (f'| {i} |')

    def pop(self):
        if self.current_size == 0:
            print("stack is empty")
        else:
            self.stack.pop()
            self.current_size -= 1


if __name__ == "__main__":
    S1 = Stack(7)
    S1.push(1)
    S1.push(2)
    S1.push(3)
    S1.push(4)
    #S1.display()
    S1.pop()
    S1.pop()
    S1.display()





