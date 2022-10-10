from rectangle import Rectangle, Square

r1 = Rectangle(3,4)
r2 = Rectangle(12,5)

print(r1.get_area())
print(r2.get_area())

sq1 = Square(5)
sq2 = Square(10)

print(sq1.get_area_square(),sq2.get_area_square())

figures = [r1,r2,sq1,sq2]
for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())