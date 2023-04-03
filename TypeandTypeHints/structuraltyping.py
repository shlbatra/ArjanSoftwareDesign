# structural vs nominal typing
# structure of object adheres to protocol then it works fine - duck typing

class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author} ({self.pages} pages)"

    def __len__(self):
        return self.pages


def main():
    my_str = "hello"
    print(len(my_str))
    my_list = [1, 2, 3]
    print(len(my_list))
    my_dict = {"a": 1, "b": 2}
    print(len(my_dict))
    my_book = Book("Harry Potter", "J.K. Rowling", 400)
    print(len(my_book))   # object has len method so it works - Duct typing


if __name__ == "__main__":
    main()