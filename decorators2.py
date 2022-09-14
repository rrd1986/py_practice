

def decorate(f):
    def inner(*argv, **kwargv):
        print("function is getting decorated")
        return f(*argv, **kwargv)
    return inner

@decorate
def dummy(x):
    print(x)

if __name__ == "__main__":
    dummy("check decoration")


