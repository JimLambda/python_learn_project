class MyClass:
    """A simple test class."""
    i = 12345

    def fun(self_variable):
        print(self_variable)
        print(self_variable.__class__)
        return 'hello world!'

    def __init__(self, i):
        self.data2 = [123, 345]
        self.i = i
        print(self.data2)


my_class = MyClass(345)

print(my_class.i)
print(my_class.fun())


class NewMyClass(MyClass):
    def fun(self):
        print('hello world new!')


my_new_class = NewMyClass(1256)
my_new_class.fun()
super(NewMyClass, my_new_class).fun()


class Vector():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)


v1 = Vector(3, 7)
v2 = Vector(-1, -8)
v3 = v1 + v2
print(v3.a, v3.b)
print(v1 + v2)
