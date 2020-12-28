class A:
    def __init__(self):
        self.name = 'A'
    def f1(self):
        print('阿银', self.name)


class B(A):
    def __init__(self):
        self.name = 'B'

    def f1(self):
        print('我是子类', self.name)

b = B()
b.f1()
