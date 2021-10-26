class A:
    def init(self):
        self.name = 'Thomas'

    def len(self):
        return len(self.name)

    def add(self, other):
        return self.name + other.name

    # 2 x toString metoder python

    # Formel præsentation med repr
    def repr(self):
        return f'{self.dict}'

    # Uformel
    def str(self):
        return self.name


print('hello')

# a = A()

# b = A()

# a + b

# print(a + b)

# print(len(a))

# print(len(b))

# print(repr(a))

# print(a)

# print(str(a))
