'''
Visit()
www.google.com   <----
www.facebook.com
www.hp.com   <----pointer always stays on last visit


Back(noOfPages)
it will return (current page - noOfPages) page visited
Back(2) ---> www.google.com and pointer will move back to google.com

Forward(noOfPages)
it will return (current page + noOfPages) page visited
Forward(2) ---> www.hp.com
if already on the top, then return ""

'''

class BrowserHistory:
    def __init__(self):
        self.history = []
        self.top = -1

    def Visit(self, site):
        self.history.append(site)
        self.top = len(self.history) - 1

    def Current(self):
        return self.history[self.top]

    def Back(self, no):
        self.top = self.top - no
        if self.top <= -1:
            self.top = -1
            return ""
        return self.history[self.top]

    def Forward(self, no):
        self.top = self.top + no
        if self.top >= len(self.history):
            self.top = len(self.history) - 1
            return ""
        else:
            return self.history[self.top]

if __name__ == "__main__":
    bh = BrowserHistory()
    bh.Visit("www.google.com")
    bh.Visit("www.facebook.com")
    bh.Visit("www.hp.com")

    print(bh.history, bh.top)
    print(bh.Back(1))
    print(bh.Back(1))
    print(bh.history, bh.top)
    print(bh.Back(1))
    print(bh.Back(1))
    print(bh.history, bh.top)
    print(bh.Forward(2))
    print(bh.history, bh.top)
    print(bh.Visit("www.dell.com"))
    print(bh.Current())
    print(bh.history, bh.top)
    print(bh.Back(3))


    


        




