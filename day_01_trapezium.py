class Trapezium:

    def __init__(self, a, b, h):
        self._a = a
        self._b = b
        self._h = h

    @property
    def area(self):
        return (self._a + self._b) * self._h / 2

    @property
    def circumference(self):
        raise NotEnoughDataException


class Parallelogram(Trapezium):

    def __init__(self, a, h):
        super().__init__(a=a, b=a, h=h)


class Rectangle(Parallelogram):

    def __init__(self, a, b):
        super().__init__(a=a, h=b)

    @property
    def circumference(self):
        circumference = 2 * (self._a + self._h)
        return circumference


class Rhombus(Parallelogram):

    @property
    def circumference(self):
        circumference = 4 * self._a
        return circumference


class Square(Rhombus, Rectangle):

    def __init__(self, a):
        super().__init__(a=a, b=a)




mal = Parallelogram(2, 4)
print(mal.area)
