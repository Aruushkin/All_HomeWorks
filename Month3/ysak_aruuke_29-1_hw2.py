class Figure:
    unit = 'cm'

    def __init__(self, perimeter=0, ploshad=0):
        self.__Perimeter = perimeter
        self.__Ploshad = ploshad

    @property
    def perimeter(self, value):
        self.__Perimeter = value

    @perimeter.setter
    def perimeter(self, value):
        self.__Perimeter = value

    def __calculate_area(self, a=0, h=0):
        pass

    def __calculate_perimeter(self, a1=0, b1=0):
        pass

    def __info(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        super(Circle, self).__init__()
        self.__Radius = radius

    def __calculate_area(self, **kwargs):
        return f"Circle: {self.__Radius / 2}"

    def __calculate_perimeter(self, **kwargs):
        return f"Perimeter: {3.14 * self.__Radius ** 2}"

    def info(self):
        print( f'Circle radius: {self.__Radius}\n'
               f'area: {self.__calculate_area()}\n' )


class RightTriangle(Figure):
     def __init__(self, side_a, side_b):
        super(Figure, self).__init__()
        self.__side_a = side_a
        self.__side_b = side_b

     def __calculate_area(self, **kwargs):
         return f'ploshad: {self.__side_a * self.__side_b / 2}'

     def info(self):
         print( f'side_a: {self.__side_a}\n'
                f'side_b: {self.__side_b}\n'
                f'area: {self.__calculate_area()}\n' )


krug1 = Circle(10)
krug2 = Circle(20)
triangle1 = RightTriangle(10, 30)
triangle2 = RightTriangle(20, 40)
triangle3 = RightTriangle(40, 60)

list1 = [krug1, krug2, triangle1, triangle2, triangle3]


for i in list1:
    i.info()









