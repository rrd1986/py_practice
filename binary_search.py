


def find(l: list, no: int) -> bool:
    length = len(l)
    if length <= 0:
        return False

    mid = length//2
    if no == l[mid]:
        return True
    elif no < l[mid]:
        return find(l[:mid], no)
    elif  no > l[mid]:
        return find(l[mid + 1:], no)
    

if __name__ == "__main__":
    print(find([1,2,3,4,5,6,7], 2))
