class A(object):
    a = 0
    def __str__(self):
        return 'Yahoo!!'

    def __init__(self):
        self.b = 10

if __name__ == '__main__':
    a = A()
    print(a)
    print(a.__str__())
    print(a.__dict__)
    print(A.__dict__)
