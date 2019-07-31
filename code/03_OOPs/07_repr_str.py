import datetime

# We can use str() and repr() to provide extra information about our class object.


class Car:
    # Class Variables
    runs = True
    number_of_wheels = 4

    def __init__(self, name):
        print("__init__()")
        self.name = name

    def start(self, name):
        self.name = name
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken!!")

    # __str__ is the function which is invoked when we call str() on our object.
    def __str__(self):
        return f"My car is {self.name} and it runs = {self.runs}"

    def __repr__(self):
        return f'Car("{self.name}")'

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels


if __name__ == "__main__":
    now = datetime.datetime.now()
    # str() rerturns a string representation of object.
    print(str(now))

    # repr() returns a string depicting the way an object be created.
    print((repr(now)))

    my_suburu = Car("Suburu")
    print(str(my_suburu))
    print(repr(my_suburu))
