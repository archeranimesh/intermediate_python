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

    # Class methods, the @classmethod is a decorator
    # it takes a arguments which is cls and not self
    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels


if __name__ == "__main__":
    my_suburu = Car()

    # Class Method can be invoked by the instance.
    # Instance is aware of the class.
    print(my_suburu.get_number_of_wheels())

    # We can also invoke Class variables with the Class itself.
    print(Car.get_number_of_wheels())
