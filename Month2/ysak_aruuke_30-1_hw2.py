class Figure:
    unit = 'cm'

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def __info(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

  

    def __calculate_area(self):
        return f"Circle: {self.__radius / 2}"

    def __calculate_perimeter(self):
        return f"Perimeter: {3.14 * self.__radius ** 2}"

    def info(self):
        print( f'Circle radius: {self.__radius}'
               f'area: {self.__calculate_area()}\n' )


class RightTriangle:
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return f'Treugolnik: {self.__side_a * self.__side_b / 2}'

    def info(self):
        print( f'side_a: {self.__side_a}\n'
               f'side_b: {self.__side_b}\n'
               f'area: {self.calculate_area()}')


krug1 = Circle(20)
krug2 = Circle(30)
treugolnik1 = RightTriangle(10, 30)
treugolnik2 = RightTriangle(50, 10)
treugolnik3 = RightTriangle(40, 15)

list = [krug1, krug2, treugolnik1, treugolnik2, treugolnik3]

for i in list:
    i.info()


