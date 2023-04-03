# choose right datastructure for problem to be efficient for your problem
# DS - strutcture of data ex. int, lists, dict -> store in binary format in memory of computer space
# python store variable number of bits based on value of variable
# python doesnt have maximum integer value, overhead as extra data for how much memory is used
# float - 64 bits, faster and less precise than integer
# list - mutable ordered sequence of elements, dont worry about memory, overhead as scale with data, array less flexibile as fixed size so 
# faster, not work when need to search for element
# dict - searchable collections using keys, implemented as hash table - each element has hashed value (memory loc) so allow fast lookup in constant
# time, not ordered and require memory for storing keys.  Ex. game objects store in dict. Not for large lists - numpy array
# strings - f strings or format strings - insert variable into string, f"{var}" or "string {}".format(var)
# Enums - represent limited number of options. Ex - stages , 
# Tuples - immutable ordered sequence of elements, faster than list/instance objects, use when need to store data 
# that wont change, have 2-3 variables else use class, grouped variables where remember order, get object of diff 
# types that are related to each other whereas list have same type. 
# set -> list of unique elements, no duplicates, no order, no indexing, no slicing, no duplicates, no order, no indexing, no slicing,
# frozen set -> immutable set, hashable, can be used as key in dict, can be used in other sets
# deck -> add and remove elements at start and end of list efficient
# think about operations on datastructre. Ex search then dict, ordering in collection - list, several obj diff type - tuple



from enum import Enum

class Month(Enum):
    JANUARY = "january"
    FEBRUARY = "february"
    MARCH = "march"
    APRIL = "april"
    MAY = "may"
    JUNE = "june"
    JULY = "july"
    AUGUST = "august"
    SEPTEMBER = "september"
    OCTOBER = "october"
    NOVEMBER = "november"
    DECEMBER = "december"



def is_birthday(month: Month):
    return month == Month.JUNE

def birthday_month_year() -> tuple[Month, int]:
    return (Month.JUNE, 1990)


def main():
    x = 3.125e4
    l = [0, 1, 2]
    l_copy = l[:]  # deep copy so not change source copy
    my_dict = {"a": 1, "b": 2}
    print(my_dict["b"])
    amt: int = 3000
    formatted_str = f"${amt/100:.2f} is amount"
    print(formatted_str)
    # older version 
    name = "John"
    print("Hello, %s" % name)
    print(is_birthday(Month.JUNE))
    my_month, my_year = birthday_month_year()
    print(my_month, "-", my_year)
    print(1+3.3)
        
if __name__ == "__main__":
    main()