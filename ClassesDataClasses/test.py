import random 
import string
from enum import Enum, auto

a = "".join(random.choices(string.digits, k=2))
print(a)

def generate_vehicle_license() -> str:
    """Helper method for generating a vehicle license number."""

    digit_part = "".join(random.choices(string.digits, k=2))
    letter_part_1 = "".join(random.choices(string.ascii_uppercase, k=2))
    letter_part_2 = "".join(random.choices(string.ascii_uppercase, k=2))
    return f"{letter_part_1}-{digit_part}-{letter_part_2}"

b = generate_vehicle_license()
print(b)

class Accessory(Enum):
    AIRCO = auto()
    CRUISECONTROL = auto()
    NAVIGATION = auto()
    OPENROOF = auto()
    BATHTUB = auto()
    MINIBAR = auto()
    
c = Accessory.OPENROOF.name
print(c)