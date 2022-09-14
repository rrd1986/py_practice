x = [23, 34, 1, 56, 8, 67, 89]
def binarySearch(list, searchItem):

        if len(list) < 1:
            print(list)
            return False
        low = 0
        high = len(list)
        
        mid = ((low + high)) // 2
        #print(mid)
        if list[mid] == searchItem:
                return True
        elif list[mid] < searchItem:
                return binarySearch(list[mid + 1: high], searchItem)
        elif list[mid] > searchItem:
                return binarySearch(list[low:mid - 1], searchItem)
        
            
               
status = binarySearch(x, 89)
print (status)