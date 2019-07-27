class Car:
    runs = True

    # __init__ is a special function, which can be called a constructor.
    # self is a special variable which is always passed
    def __init__(self, name):
        print("__init__()")
        self.name = name

    def start(self):
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken!!")


if __name__ == "__main__":
    # Only name variable is explicitly passed,
    # Self is passed under the hood.
    my_suburu = Car("Suburu")
    my_suburu.start()
