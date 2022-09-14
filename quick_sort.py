def Sort(list):
    if len(list) <= 1:
        return list
    mid = len(list)//2
    left = []
    right = []
    middle = []
    while mid >= 1:
        for i in list:
            if i < list[mid]:
                left.append(i)
            elif i > list[mid]:
                right.append(i)
            else:
                middle.append(i)
            print(left)
            print(right)
            print(middle)        
        return Sort(left) + middle + Sort(right)

print(Sort([4,1,3,10]))