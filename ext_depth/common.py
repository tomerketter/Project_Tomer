def print_name():
    name = "Tomer"
    print(name)


def second_func():
    print("Kevin is in the room")


class Human:
    def __init__(self):
        self.name = "Unknown"  # this is a class variable. 'self' is a way to hold class variables and class functions

    def print_name(self):
        """Class functions are called methods"""
        print(self.name)
