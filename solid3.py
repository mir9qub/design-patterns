"""
L (The Liskov Substitution Principle) – принцип подстановки Лисков, описывающий возможности заменяемости экземпляров
объектов. Простыми словами: дочерний класс должен следовать принципам родительского класса и не изменять их.
Пусть у нас есть класс Прямоугольник с методами, задающими ширину, высоту и рассчитывающим площадь. Теперь мы захотели
создать класс Квадрат. Квадрат – тот же самый прямоугольник, но с одинаковыми сторонами. Класс Квадрат наследуется от
класса Прямоугольник и переопределяет его методы: подставляем значения – все работает. Но если мы начнем использовать
класс Прямоугольник в качестве интерфейса, а работать будем с классом Квадрат, мы разом изменяем оба параметра.
Чтобы решить эту проблему, создается общий интерфейс для обоих классов и вместо наследования одного класса от другого
использовать этот самый интерфейс.
"""

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self._width}, height: {self._height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value

def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')

rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)

"""
Expected an area of 20, got 20
Expected an area of 50, got 100
"""