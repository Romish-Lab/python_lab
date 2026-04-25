# 6. Write a python function that accepts radius and returns the area 
# and circumference of a circle. Import Pi from Math.
import math
def circle(r):
    area = math.pi * r **2
    circ = 2 * math.pi * r
    return area, circ
print(circle(5))