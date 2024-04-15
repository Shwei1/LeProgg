from reader import Output
from classes_331 import *
files = ["input01.txt", "input02.txt", "input03.txt"]
for filename in files:
    print(f"The figure with the largest measure in {filename} is {Output(filename).largest_measure()} with {'area' if Output(filename).largest_measure().dimension() == 2 else 'volume'} of {Output(filename).largest_measure().volume()}")
