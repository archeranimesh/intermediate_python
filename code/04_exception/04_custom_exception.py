# Inheriting from Exception Class can generate custom exception.
# All Exceptions are subclass on Exception class.


class MyCustomException(Exception):
    pass


class IncorrectValueError(Exception):
    def __init__(self, value):
        message = f"Got a bad value {value}"
        # The init of Exception() takes a message argument.
        super().__init__(message)


if __name__ == "__main__":
    # This is, how we raise our custom exception.
    # raise MyCustomException()

    my_val = 999
    if my_val > 998:
        raise IncorrectValueError(my_val)
