

def reverse(l):
    rev_l = []
    length = len(l)
    for i in range(length):
        rev_l.append(length - i)
    return rev_l    



print(reverse([1, 2, 3]))

x = [2,3, 5, 6]

print(x[::-1])