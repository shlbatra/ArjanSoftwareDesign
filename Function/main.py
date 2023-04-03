# grouping of statements, function as an object - pass it around as an object - functional programming
# pure functions -> functions with argument and provide same return value 
# impure functions -> functions with argument and provide different return value ex. random number generator or rely on date
# functions with side effects -> effect things outside their scope
# the Callable type covers anything that implements the __call__ dunder method

CUSTOMERS = {
    "Alice": {"phone": "2341", "addr": "Foo drive 23"},
    "Beth": {"phone": "9102", "addr": "Bar street 42"},
}

def pure_function(x: int, y: int) -> int: # implementation of call method
    return x + y

def side_effect() -> None:  # change CUSTOMERS that is outside the scope of the function, hard to test
    # fix this by providing customer as argument but still not a great solution
    # def side_effect(customers: dict[str,Any]) -> None: - dependency injection
    CUSTOMERS["Alice"]["phone"] = "1234"

class MyClass:
    def __init__(self, x: int) -> None:
        self.x = x
        
    def __call__(self) -> int:   # convert class to callable
        return self.x

def main() -> None:
    print(CUSTOMERS)
    c = MyClass(5)
    print(c())  # or print(c.__call__())
    print((2).__class__)  # evrything is an object in python. 2 is as object of class int
    print(main.__class__)
    print(pure_function(1,2))
    print(pure_function.__call__(1,2))  # pure_function is object that has dunder methods defined
  
    
if __name__ == "__main__":
    main()
    