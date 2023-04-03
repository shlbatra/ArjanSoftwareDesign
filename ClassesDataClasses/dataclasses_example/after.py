"""
Class can be data focussed or behaviour focussed.
Data focussed class prefer using dataclass and remove boiler plate code ex. __init__ method
change values in data class as and when reqyuired 
encapsulation  - class hides implementation aspects from user so seperate code better (less coupling)
Ex. change accessories to dict from list and if no knows then change only in vehicle class
dataclass reduce encapsulation as access attributes directly (use public / private but not in python)
put _instance_variable -> users not suppose to change it
"""
import random
import string
from dataclasses import dataclass, field
from enum import Enum, auto
from datetime import datetime


def generate_vehicle_license() -> str:
    """Helper method for generating a vehicle license number."""

    digit_part = "".join(random.choices(string.digits, k=2))
    letter_part_1 = "".join(random.choices(string.ascii_uppercase, k=2))
    letter_part_2 = "".join(random.choices(string.ascii_uppercase, k=2))
    return f"{letter_part_1}-{digit_part}-{letter_part_2}"


class Accessory(Enum):
    AIRCO = auto()
    CRUISECONTROL = auto()
    NAVIGATION = auto()
    OPENROOF = auto()
    BATHTUB = auto()
    MINIBAR = auto()


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()

def default_accessories():
    return [Accessory.AIRCO]

@dataclass()  # frozen=True makes object of class immutable ie. object constant = doesnt change
class Vehicle:
    brand: str
    model: str
    color: str
    license_plate: str = field(init=False) # field(default_factory=generate_vehicle_license, init=False) # not initialize at object level
    fuel_type: FuelType = FuelType.ELECTRIC
    accessories: list[Accessory] = field(default_factory=lambda: [Accessory.AIRCO])
    # list[Accessory] = [] not allowed as list is mutable object so use default_factory
    # field(default_factory=list) is allowed as default factory tell how to generate default value
    # default factory expects a function that returns object of type list[Accessory]
    # field(default_factory=default_accessories) is also allowed
  
    def __post_init__(self):   # Method called after instance has been initialized, not work with frozen - True
        self.license_plate = generate_vehicle_license()  # license_plate is not initialized at object level
        if self.brand == "Tesla":
            self.license_plate += "-t"
        
    def reserve(self, date: datetime):
        print(f"Vehicle is reserved for {date}")


def main() -> None:
    """
    Create some vehicles and print their details.
    """

    tesla = Vehicle(
        brand="Tesla",
        model="Model 3",
        color="black",
        # license_plate=generate_vehicle_license(),
        accessories=[
            Accessory.AIRCO,
            Accessory.MINIBAR,
            Accessory.NAVIGATION,
            Accessory.CRUISECONTROL,
        ],
    )
    volkswagen = Vehicle(
        brand="Volkswagen",
        model="ID3",
        color="white",
        # license_plate=generate_vehicle_license(),
        accessories=[Accessory.AIRCO, Accessory.NAVIGATION],
    )
    bmw = Vehicle(
        brand="BMW",
        model="520e",
        color="blue",
        # license_plate=generate_vehicle_license(),
        fuel_type=FuelType.PETROL,   # support default value
        accessories=[Accessory.NAVIGATION, Accessory.CRUISECONTROL], 
    )
        

    print(tesla)   # __repr__ method is called - useful info is printed here
    print("\n") 
    print(volkswagen)
    print("\n")
    print(bmw)
    print("\n")
    bmw.reserve(datetime(2021, 12, 24))


if __name__ == "__main__":
    main()
