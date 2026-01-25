from abc import ABC, abstractmethod

class Ride(ABC):
    @abstractmethod
    def book_ride(self):
        pass


class BikeRide(Ride):
    def book_ride(self):
        print("Bike ride booked 🚲")


class CabRide(Ride):
    def book_ride(self):
        print("Cab ride booked 🚗")


class AutoRide(Ride):
    def book_ride(self):
        print("Auto ride booked 🛺")


# Polymorphism + Abstraction
rides = [
    BikeRide(),
    CabRide(),
    AutoRide()
]

for ride in rides:
    ride.book_ride()
