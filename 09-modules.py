# Modules in Python
# Modules are files containing Python code. They can define functions, classes, and variables.

# Built-in modules
# import the module
import math

print(math.pi)

print(math.sqrt(25))

#calendar module
import calendar

print(calendar.month(2025, 2))

print(calendar.isleap(2024))

# External Modules
# Python Pypi contains all the modules

import numpy as np

q1 = np.array([[200, 220, 250],
                [150, 180, 210], 
                [300, 320, 350]])

q2 = np.array([[209, 230, 260], 
               [160, 190, 220], 
               [310, 330, 360]])

print(q1 + q2)

print(q1 - q2)


# User-defined modules
from myutils import volume_cylinder

print(volume_cylinder(2, 5))

from myutils import volume_triangle

print(volume_triangle(2, 5))


import myutils

print(myutils.volume_cylinder(7, 10))

print(myutils.volume_triangle(12, 9))

