from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_CONDITIONERS = 0.9

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_used = (self.fuel_consumption + Car.AIR_CONDITIONERS) * distance
        if fuel_used <= self.fuel_quantity:
            self.fuel_quantity -= fuel_used
            return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITIONERS = 1.6
    FUEL_LOST_FACTOR = 0.95

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_used = (self.fuel_consumption + Truck.AIR_CONDITIONERS) * distance
        if fuel_used <= self.fuel_quantity:
            self.fuel_quantity -= fuel_used
            return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel * Truck.FUEL_LOST_FACTOR


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)