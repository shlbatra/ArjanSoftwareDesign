# Inheritance - define interface to diff parts of program without relying on specific implementations of interface. Ex - generic class use have specific subclass - use objects of specific subclass
# dangrous when use complex hierarchy - super and sub class relationship strong - strong coupling. 
# abstract base class really only serves as an interface - define contract between diff parts of your application 
# In some cases, like in the Bridge class, the ABC has an instance variable (pointing to the second hierarchy of classes in that pattern). 
# And in a few other cases, such as the Decorator pattern, there are two layers of inheritance.
# nominal type relationship here (type hints so ignored) - types are related via inheritance Ex, Car(Vehicle) - typing error if Vehicle not shown in Pylance
# typing issue at instance creation
# use in case where super class defines useful methods for subclasses to use
# use if complete control over code base 

import math
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


class Vehicle(ABC):
    @abstractmethod   #subclass should implement abstract methods
    def reserve(self, start_date: datetime, days: int):
        """A vehicle can be reserved for renting"""

    @abstractmethod
    def renew_license(self, new_license_date: datetime):
        """Renews the license of a vehicle."""


@dataclass
class Car(Vehicle):
    model: str
    reserved: bool = False

    # if reserve method missing then get Type Error
    def reserve(self, start_date: datetime, days: int):
        self.reserved = True
        print(f"Reserving car {self.model} for {days} days at date {start_date}.")

    def renew_license(self, new_license_date: datetime):
        print(f"Renewing license of car {self.model} to {new_license_date}.")


@dataclass
class Truck(Vehicle):
    model: str
    reserved: bool = False
    reserved_trailer: bool = False

    def reserve(self, start_date: datetime, days: int):
        months = math.ceil(days / 30)
        self.reserved = True
        self.reserved_trailer = True
        print(
            f"Reserving truck {self.model} for {months} month(s) at date {start_date}, including a trailer."
        )

    def renew_license(self, new_license_date: datetime):
        print(f"Renewing license of truck {self.model} to {new_license_date}.")


# reserve vehicle and not deal with which one -> just need object with reserve method -> reservation system independent of which sub class - add third type of subclass easily
# and just add object of third subclass without changing reserve_now function
def reserve_now(vehicle: Vehicle):
    vehicle.reserve(datetime.now(), 40)


def main():
    car = Car("Ford")
    truck = Truck("DAF")
    reserve_now(car)
    reserve_now(truck)
    # what = Vehicle() - TypeError: Can't instantiate abstract class Vehicle with abstract methods renew_license, reserve, vehicle should only be interface. Error because abstractmethods defined


if __name__ == "__main__":
    main()
