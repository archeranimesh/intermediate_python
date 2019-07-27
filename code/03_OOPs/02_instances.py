class Car:
    runs = True

    def start(self, name):
        self.name = name
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken!!")


if __name__ == "__main__":
    my_suburu = Car()
    # Python has no protection for class variable.
    my_suburu.start("Suburu")
    my_suburu.runs = False  # Modified the class variable without a method.
    my_suburu.start("Suburu")
