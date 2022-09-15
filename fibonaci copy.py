
# 1, 1, 2, 3, 5

# 3 --> 1 + 2

def Fibonaci(n):
    if n < 2:
        return 1
    else:
        return Fibonaci(n -2) + Fibonaci(n -1 )

def FibonaciDecorator(n):
    x, y = 0, 1
    for i in range(n):
        x,y = y, x+ y
        yield x


def FibonaciMemoization(n, cache = {0 : 1, 1: 1}):
    if n in cache:
        return cache[n]
    else:
        cache[n] =  FibonaciMemoization(n -2 ) + FibonaciMemoization(n -1 )
        return cache[n]   

if __name__ == "__main__":
    f = []
    for i in range(4):
        f.append(Fibonaci(i))
    print(f)

    for i in FibonaciDecorator(10):
        print(i)

    fm = []
    for i in range(4):
        fm.append(Fibonaci(i))
    print(fm)
