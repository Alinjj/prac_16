class Rectangle:
    def __init__(self,a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def display(self):
        print(self.get_area())

r1 = Rectangle(5,10)
r1.display()