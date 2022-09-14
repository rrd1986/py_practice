
def decorator_func(f):
    def inner_func(*argv, **kwargv):
        print("just adding a print statements")
        return f(*argv, **kwargv)
    return inner_func

@decorator_func
def func(x):
    return x**x


if __name__ == "__main__":
    print(func(5))
