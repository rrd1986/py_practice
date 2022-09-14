from typing import List

def BubbleSort(usl: List[int]):
    l = len(usl)
    for i in range(l):
        for j in range(l):
            if usl[i] > usl[j]:
                # switch
                usl[i], usl[j] = usl[j], usl[i]
    return usl            



if __name__ == "__main__":
    usl = [23, 1, 65, 8, 34, 90]
    print(usl)
    print(BubbleSort(usl))






