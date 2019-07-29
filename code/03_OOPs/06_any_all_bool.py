if __name__ == "__main__":
    # Boolean is a subclass of int so we can do this.
    # this should be avoided.
    print(True + True)  # 2
    print({0, 1, True, False})  # 0,1

    # any returns true, if only one element is truthy
    print(any([1, 3, 0, 1]))
    print(any({0, 1, True, False}))

    # all returns true, if all element are true
    print(all([1, 3, 0, 1]))
