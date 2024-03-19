class Wheel:
    pass

class Engine:
    pass

class Driver:
    def __init__(self, name):
        self._name = name
    def go(self):
        print("Driver is driving!")


class Car:
    def __init__(self, wheel):
        self._engine = Engine() # composition
        self._wheel = wheel # aggregation
        self._driver = None # during the production of a car, the driver is not mounted; **association**

    def set_driver(self, driver):
        self._driver = driver

    def drive(self):
        if self._driver is not None:
            self._driver.go()

if __name__ == "__main__":
    wheel = Wheel()
    car = Car(wheel)