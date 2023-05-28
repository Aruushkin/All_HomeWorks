class Transport:
    def __init__(self, the_model, the_year, the_color):
        # attributes/fields
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        # attributes/fields
        super().__init__(the_model, the_year, the_color)


class Car(Transport):
    # class attributes
    number_of_wheels = 4
    counter = 0

    # constructor
    def __init__(self, the_model, the_year, the_color, penalties=0.0):
        # attributes/fields
        super().__init__(the_model, the_year, the_color)
        self.penalties = penalties
        Car.counter += 1

    # methods
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')

    def make_signal(self, number_of_times):
        result = 'BEEP ' * number_of_times
        print(f'Car {self.model} {result}')


class Truck(Car):
    number_of_wheels = 10
    def __init__(self, the_model, the_year, the_color, penalties=0.0, load_capacity=0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, type, weight):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity}')
        else:
            print(f'You successfully loaded {type} of {weight} kg')


print(f'We need {10 * Car.number_of_wheels * 5000} soms to change lastics for summer')

bmw_car = Car('BMW X6', 2020, 'Red')
print(bmw_car)
print(f'Model: {bmw_car.model} Year: {bmw_car.year} Color: {bmw_car.color} Penalties: {bmw_car.penalties}')

honda_car = Car(the_color='Black', the_model='Honda Fit', the_year=2009, penalties=900)
print(f'Model: {honda_car.model} Year: {honda_car.year} Color: {honda_car.color} Penalties: {honda_car.penalties}')

bmw_car.drive('Osh')
honda_car.drive('Tokmok')

# honda_car.color = 'Green'
honda_car.change_color('Green')
print(f'Model: {honda_car.model} Year: {honda_car.year} NEW Color: {honda_car.color} Penalties: {honda_car.penalties}')

honda_car.make_signal(5)

print(f'We produced {Car.counter} cars')

boeing_plane = Plane('Boeing 737', 2022, 'White')
print(f'Model: {boeing_plane.model} Year: {boeing_plane.year} Color: {boeing_plane.color}')

volvo_truck = Truck('Volvo 365', 2018, 'Blue', 1200, 30000)
print(f'Model: {volvo_truck.model} Year: {volvo_truck.year} Color: {volvo_truck.color} '
      f'Penalties: {volvo_truck.penalties} Load Capacity: {volvo_truck.load_capacity}')
volvo_truck.load_cargo('Apples', 35000)
volvo_truck.load_cargo('Apples', 25000)
volvo_truck.drive('Naryn')

print(f'We need {5 * Truck.number_of_wheels * 5000} soms to change lastics for summer period of TRUCKS')