from math import pi
sphere = "cell"
#radius = int(input("Cell radius (int): "))
with open("sphere_diameter.txt") as in_file:
    for radius in in_file:
        radius = radius.strip()
        radius = float(radius)
        volume = 4 / 3 * pi * radius ** 3
        print("The volume of a %s of radius %d is %10f" %(sphere, radius, volume))
