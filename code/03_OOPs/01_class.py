# Everything is a object in Python, even int.
# Class is a template, blue print of a object.
# Instance is a specific creation of a class.


class Car:
    runs = True  # Class Variable

    def start(
        self, name
    ):  # self is a special variable name which is associated with an instance of object.
        self.name = name
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken!!")


if __name__ == "__main__":
    my_suburu = Car()
    print(my_suburu)
    print(my_suburu)
