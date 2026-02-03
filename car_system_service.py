class Car:
    def service(self):
        print("General car service")


class ElectricCar(Car):
    def service(self):
        print("Electric car service: Battery check and software update")


class DieselCar(Car):
    def service(self):
        print("Diesel car service: Engine oil and filter replacement")


class PetrolCar(Car):
    def service(self):
        print("Petrol car service: Engine tuning and oil change")


# Polymorphism in action
cars = [
    ElectricCar(),
    DieselCar(),
    PetrolCar()
]

for car in cars:
    car.service()
