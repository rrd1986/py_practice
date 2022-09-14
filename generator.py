

def Genearte(n):
    for i in range(n):
        yield i**i

x = Genearte(10)

for i in x:
    print(i)
