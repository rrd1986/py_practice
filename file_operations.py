

if __name__ == "__main__":
    fh = open("dummy.txt", "w+")
    fh.write("hello world\n")
    fh.write("hello world\n")
    fh.write("hello world\n")
    fh.write("hello world\n")
    fh.write("hello world\n")
    '''
    #fh.seek(0)
    while fh:
        l = fh.readline()
        print(l)
        if l == "":
            break
    '''
    #fh.seek(0)
    fh.close()
    fh = open("dummy.txt", "r")
    lines = fh.readlines()
    print(lines)
    fh.close()