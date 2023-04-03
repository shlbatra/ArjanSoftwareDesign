# functions are objects that can pass along
# higher order fn that can have fn as an arg or return fn

from dataclasses import dataclass
from typing import Callable, List

@dataclass
class Customer:
    name: str
    age: int
    
    
def is_eligible_for_promotion(customer: Customer) -> bool:
    return customer.age >= 31
    
    
def send_email_promotion(customer: list[Customer], is_eligible_for_promotion: Callable[[Customer],bool]) -> None:
    for c in customer:
        if is_eligible_for_promotion(c):
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
    
    send_email_promotion(customers, is_eligible_for_promotion)
    # alternate use lambda function
    print("\n")
    send_email_promotion(customers, lambda customer: customer.age >= 31)
    
if __name__ == "__main__":
    main()