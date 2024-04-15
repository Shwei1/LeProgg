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
                if key == "Circle":
                    f = Circle(*value)
                if key == "Rectangle":
                    f = Rectangle(*value)
                    figurines.append(f)
                if key == "Trapeze":
                    f = Trapezium(*value)
                    figurines.append(f)
                if key == "Parallelogram":
                    f = Parallelogram(*value)
                    figurines.append(f)
                if key == "Ball":
                    f = Sphere(*value)
                    figurines.append(f)
                if key == "TriangularPyramid":
                    f = Tetrahedron(*value)
                    figurines.append(f)
                if key == "QuadrangularPyramid":
                    f = QuadraticPyramid(*value)
                    figurines.append(f)
                if key == "TriangularPrism":
                    f = TriangularPrism(*value)
                    figurines.append(f)
                if key == "RectangularParallelepiped":
                    f = RectangularParallelepiped(*value)
                    figurines.append(f)
                if key == "Cone":
                    f = Cone(*value)
                    figurines.append(f)
        except(ValueError, AssertionError):
            figurines.append(f"Broken figure {key}")
        return figurines

    def measure_finder(self):
        figurines = self.initialiser()
        volumes = []
        for figurine in figurines:
            volumes.append(figurine.volume())
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





