class Auto:

    def __init__(self, mark, colour, velocity):
        self.mark = mark
        self.velocity = velocity
        self.colour = colour

    def go(self):
        print(f"{self.mark}: go...")
        print("PHONK DRIFT, say hi to Allah")

    def showColour(self):
        print(f"{self.colour} is wild for {self.mark}!")


if __name__ == "__main__":
    mercedes = Auto("Mercedes", "scarlet", 200)
    mazda = Auto("Mazda", "red", 200)
    mazda.go()
    print(mercedes.mark)
    print(mazda.mark)
    mazda.showColour()
