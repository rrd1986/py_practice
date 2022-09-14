class A(object):
    def __init__(self):
        pass

    @staticmethod
    def check_static_method(self):
        print("i am in static method")

    @classmethod
    def check_class_method(self):
        print("i am in class method")



if __name__ == "__main__":
    a = A()
    a.check_class_method()
    a.check_static_method(A)

    A.check_class_method()
    A.check_static_method(A)


    