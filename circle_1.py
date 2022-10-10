Pi = 3.14
class Circle:
    def __init__(self,r):
        self.r = r

    def get_circle_area(self):
        return Pi * (self.r**2)