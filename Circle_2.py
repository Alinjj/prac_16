from circle_1 import Circle

c1 = Circle(15)
c2 =Circle(25)

Circles = [c1,c2]
for figure in Circles:
    if isinstance(figure, Circle):
        print(figure.get_circle_area())
    else:
        pass


