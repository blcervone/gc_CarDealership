# Create a base class named Vehicle to store the data about each vehicle. This class should contain these specifications:
# Initialization (self, make, miles, price)
    # Sets the make, miles and price properties
    # Also sets a engine_on property to False
# Methods
    # start_engine()
        # Prints a message: “Starting engine…”
        # Sets engine_on to True
    # make_noise()
        # Prints a message: “Beep beep!”
# Create a derived class from Vehicle named Truck to store the data about each vehicle. This class should contain these specifications:
# Initialization (self, make, miles, price)
    # Sets the make, miles and price properties
    # Also sets a cargo property to False
# Additional Methods
    # load_cargo()
        # Prints a message: “Loading the truck bed…”
        # Sets cargo to True
# Create a derived class from Vehicle named Motorcycle to store the data about each vehicle. This class should contain these specifications:
# Initialization (self, make, miles, price, top_speed)
    # Sets the make, miles and price properties
    # Sets additional method of top_speed
# Override Methods
    # make_noise()
    # Prints a message: “Vroom vroom!”


# ==================================================================================================================== #

class Vehicle:

    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False

    def start_engine(self):
        print("Starting engine...")
        self.engine_on = True

    def make_noise(self):
        print("Beep beep!")


class Truck(Vehicle):

    def __init__(self, make, miles, price):
        Vehicle.__init__(self, make, miles, price)
        self.cargo = False

    def load_cargo(self):
        print("Loading the truck bed...")
        self.cargo = True

    def __str__(self):
        return f"{self.make}: with {self.miles} miles, costs ${self.price}"


class Motorcycle(Vehicle):

    def __init__(self, make, miles, price, top_speed):
        Vehicle.__init__(self, make, miles, price)
        self.top_speed = top_speed

    def make_noise(self):
        print("Vroom vroom!")

    def __str__(self):
        return f"{self.make}: with {self.miles} miles, and a top speed of {self.top_speed}, costs ${self.price}"
