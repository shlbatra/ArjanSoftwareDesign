# Python dyanmically and strongly typed. Variables can change type but not values assigned to them
# use structural typing (structure of object - two objects with same func name, duct typing) instaed of nominal typing (use name of type ex. inheritance)
# callable -> function, class method, property, etc

from typing import Callable

IntFunction = Callable[[int], int]  # function that takes an int and returns an int


def multiple_by_two(x: float) -> float:
    return x * 2


def add_three(x: int) -> int:  # python interpreter will ignore this but it is good code practice
    return x + 3


def compute_stats(users, plans, products): # what type of arguments are passed here by doc or by code - type hints
    # some complicated code here that does something 
    pass
    
    
def main():
    my_var = "hello"
    my_var = str(5) + "hello"  # strongly typed so here we get an error at run time for 5 + "hello"
    print(my_var)
    my_val = add_three(5)
    print(my_val)
    my_func: IntFunction = add_three
    my_func: IntFunction = multiple_by_two  # pylant error here because multiple_by_two returns a float
    print(my_func(5))
    
    
if __name__ == "__main__":
    main()