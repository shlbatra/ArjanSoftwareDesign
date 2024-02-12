# Protocols are mainly useful to define the interface that you expect in certain areas of your code - interface segregation
# Python's structural typing system by using Protocols (Duct Typing) - no need for direct inheritance relationships
# typing issue when start using the class
# if use ABC here then truck inherit from both Rentable and LicenceHolder classes - protocol much cleaner way
# ABC hierarchy and Protocol where it is used. Rentable with reserve_now method - defines contract for what reserve_now expects
# use third party library and add function with them - add interface with them 
"""
Ex. with third party library
class EmailClient:
def __init__(
self,
smtp_server: SMTP,
credentials: tuple[str, str] = (LOGIN, PASSWORD),
):
# using the smtp server here

Currently, there's direct coupling with the SMTP class. What if you want to be independent of the smtplib module and be able to use a variety of SMTP server implementation? You can't use an ABC to solve this because then you would need to change the SMTP class to inherit from an abstract class. But with a Protocol class, you can do this:

class EmailServer(Protocol):
def connect(self, host: str, port: int) -> None:
...
def sendmail(self, from_address: str, to_address: str, message: str) -> None:
...

class EmailClient:
def __init__(
self,
smtp_server: EmailServer,
...etc
"""

import math
from dataclasses import dataclass
from datetime import datetime
from typing import Protocol


class Rentable(Protocol):    # alternate to class Vehicle in ABC
    def reserve(self, start_date: datetime, days: int):
        ...


class LicenseHolder(Protocol):
    def renew_license(self, new_license_date: datetime):
        ...


@dataclass
class Car:
    model: str
    reserved: bool = False

    def reserve(self, start_date: datetime, days: int):
        self.reserved = True
        print(f"Reserving car {self.model} for {days} days at date {start_date}.")


@dataclass
class Truck:
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
        print(f"Renewing the license until {new_license_date}.")


def reserve_now(rentable: Rentable):  # protocol relationship defined dyanmically
    rentable.reserve(datetime.now(), 1)


def renew_license(license_holder: LicenseHolder):
    license_holder.renew_license(datetime.now())


def main():
    car = Car("Ford")
    truck = Truck("DAF")
    reserve_now(car)  # only expect reserve methods
    reserve_now(truck)
    renew_license(truck) # only expect renew license methods
    # renew_license(car)   -> AttributeError: 'Car' object has no attribute 'renew_license' - based on protocol we need renew_licnese_method


if __name__ == "__main__":
    main()
