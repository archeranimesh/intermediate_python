class Car:
    # Class Variables
    runs = True
    number_of_wheels = 4

    def start(self, name):
        self.name = name
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken!!")

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels


if __name__ == "__main__":
    my_suburu = Car()
    print(type(my_suburu))

    # type of a class is type
    print(type(Car))

    # isinstance returns true if an object is instance of a class.
    print(isinstance(42, int))
    print(isinstance(my_suburu, Car))
    # Boolean is an instance of int.
    print(isinstance(True, int))

    # isSubclass returns true if an object is a subclass of a class.
    # all object are subclass of object.
    print(issubclass(int, object))
    # Bool is a subclass of int.
    print(issubclass(bool, int))

