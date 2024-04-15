from classes_331 import *

class Output:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, "rt") as inpf:
            data = dict()
            for line in inpf:
                datum = [el for el in line.split()]
                key = datum[0]
                values = [int(el) for el in datum[1:]]
                data.update({key: values})
        return data

    def initialiser(self):
        figurines = []
        try:
            for key, value in self.read_file().items():
                if key == "Triangle":
                    f = Triangle(*value)
                    figurines.append(f)
                elif key == "Circle":
                    f = Circle(*value)
                    figurines.append(f)
                elif key == "Rectangle":
                    f = Rectangle(*value)
                    figurines.append(f)
                elif key == "Trapeze":
                    f = Trapezium(*value)
                    figurines.append(f)
                elif key == "Parallelogram":
                    f = Parallelogram(*value)
                    figurines.append(f)
                elif key == "Ball":
                    f = Sphere(*value)
                    figurines.append(f)
                elif key == "TriangularPyramid":
                    f = Tetrahedron(*value)
                    figurines.append(f)
                elif key == "QuadrangularPyramid":
                    f = QuadraticPyramid(*value)
                    figurines.append(f)
                elif key == "TriangularPrism":
                    f = TriangularPrism(*value)
                    figurines.append(f)
                elif key == "RectangularParallelepiped":
                    f = RectangularParallelepiped(*value)
                    figurines.append(f)
                else:
                    f = Cone(*value)
                    figurines.append(f)
        except(ValueError, AssertionError):
            pass
        return figurines

    def measure_finder(self):
        figurines = self.initialiser()
        volumes = []
        try:
            for figurine in figurines:
                volumes.append(figurine.volume())
        except(ValueError, AssertionError):
            volumes.append(0)
        return volumes

    def largest_measure(self):
        volumes = self.measure_finder()
        data = self.initialiser()
        largest_figurine = data[0]
        try:
            for i in range(1, len(volumes)+1):
                if data[i].volume() > largest_figurine.volume():
                    largest_figurine = data[i]
        except(TypeError, AttributeError, IndexError):
            pass
        return largest_figurine

    def output(self, outfile):
        with open(outfile, "wt") as of:
            print(
                f"The figure with the largest measure in {self.filename} is {self.largest_measure()} with volume of {self.largest_measure().volume()}", file=of)




