# Inheritance is used to share property and functionality across similar code.
# like car and 2 wheels
# It creates resuable code.
# Breaks code into hierarchy, more generics to more specific.
# Objects higher up in the hiearchy is more generics.
# Multiple inheritance is possible in Python.z


class Vehicle:
    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    # This method will be available to any object inheriting from this Class.
    def is_eco_friendly(self):
        if self.fuel == "gas":
            return True
        else:
            return False


# We inherit by sending the base class name as param during class creation.
class Car(Vehicle):
    def __init__(self, make, model, fuel="gas", num_wheels=4):
        # This calls the Vehicle's __init__()
        super().__init__(make, model)
        # Adds new functionality for this class.
        self.num_wheels = num_wheels


if __name__ == "__main__":
    four_by_four = Vehicle("No idea", "hello idea")
    print(
        four_by_four.make,
        four_by_four.model,
        four_by_four.fuel,
        four_by_four.is_eco_friendly(),
    )
    my_suburu = Car("Suburu", "XUV", fuel="diesel")
    print(my_suburu.make, my_suburu.model, my_suburu.fuel, my_suburu.is_eco_friendly())

