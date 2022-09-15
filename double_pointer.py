

def sort_squares(sorted_integer_list):
    start, end = 0 , len(sorted_integer_list) -1 
    pos = len(sorted_integer_list) -1 
    res = len(sorted_integer_list) * [0]

    while start < end:
        print(start)
        print(end)
        if abs(sorted_integer_list[start]**2) >  abs(sorted_integer_list[end]**2):
            res[pos] = abs(sorted_integer_list[start]**2)
            start += 1
        else:
            print(end)
            res[pos] = abs(sorted_integer_list[end]**2)
            end -= 1 
        pos -= 1
    return res    


if __name__ == "__main__":
    sorted_integer_list = [-5, -2, -1, 3, 7, 9, 11]
    print(sort_squares(sorted_integer_list))