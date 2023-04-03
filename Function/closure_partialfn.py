# Closure - function define within another function - has access right to the outer function's variables -> nested function structure
# Partial function - function with some of the arguments already set and return new fn- functools 
# Currying -> function with n number of parameters -> n number of functions with 1 parameter each

from dataclasses import dataclass
from typing import Callable, List
from functools import partial


@dataclass
class Customer:
    name: str
    age: int


def is_eligible_for_promotion(cutoff_age: int = 1) -> Callable[[Customer], bool]:
    def is_eligible(customer: Customer) -> bool:
        return customer.age >= cutoff_age
    return is_eligible


def is_eligible_for_promotion_partial(customer: Customer, cutoff_age: int = 1) -> bool:
    return customer.age >= cutoff_age


def send_email_promotion(customer: list[Customer], is_eligible_fn: Callable[[int],Callable]) -> None:
    for c in customer:
        if is_eligible_fn(c):   # customize cut off age
            print(f"Sending email to {c.name}")
        else:
            print(f"Not sending email to {c.name}")


def main() -> None:
    customers = [
        Customer("Alice", 21),
        Customer("Bob", 34),
        Customer("Charlie1", 56),
        Customer("Charlie2", 36),
        Customer("Charlie3", 26),
        Customer("Charlie4", 66),
    ]
    # use closure function below
    send_email_promotion(customers, is_eligible_for_promotion(60))
    # create partial fn with new arguments 
    print("\n")
    is_eligible = partial(is_eligible_for_promotion_partial, cutoff_age=30)
    send_email_promotion(customers, is_eligible)

if __name__ == "__main__":
    main()