import tkinter
from Triangle import *

key = int(input("Choose your animation: \n1) Rotation"
            "\n2) Deformation\n"))

triangle = generateTriangles(1)[0]
triangle.__init__(200, 0, 100, 173)
triangle.set_pivot(0, 57.7)

if key == 1:
        while True:
            triangle.draw()
            triangle.set_rotation(10)
            (x1, y1), (x2, y2) = triangle.rotated_vertices()
            triangle.__init__(x1, y1, x2, y2)
            triangle.cleaner()
elif key == 2:
    while True:
        triangle.set_pivot(0, 57.7)
        triangle.draw()
        triangle.set_distortion(1.05, 1.05)
        (x1, y1), (x2, y2) = triangle.stretched_vertices()
        triangle.__init__(x1, y1, x2, y2)
        triangle.cleaner()

tkinter.mainloop()

