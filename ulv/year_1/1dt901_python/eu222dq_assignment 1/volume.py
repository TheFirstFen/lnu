#make a program that calculates the volume of a sphere
import math
radius_of_sphere = float(input("Input your radius here: "))
volume_of_sphere = round((4/3)*(math.pi)*(radius_of_sphere**3),1)
print(volume_of_sphere)