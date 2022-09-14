

# 1, 1, 2, 3, 5

def fibonaci(no: int) -> int:
    if no < 3:
        return 1
    else:
        return fibonaci(no -2 ) + fibonaci(no -1)


# use memoization
def fibonaci2(no: int, cache: dict  = {1: 1, 2: 1}) -> int:
    if no in cache:
        return cache[no]
    else:
        cache[no] = fibonaci(no -2 ) + fibonaci(no -1)
        return cache[no]

def finonaci3(no: int) -> int:
    x, y = 0, 1
    for i in range(no):
        x,y = y, x+y
        yield x 


if __name__ == "__main__":
    #for i in range(1, 10):
    #    print(fibonaci2(i))

    for i in finonaci3(10):
        print(i)

  