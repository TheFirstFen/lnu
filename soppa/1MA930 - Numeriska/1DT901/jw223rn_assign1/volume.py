import math

rad = int(input("Provide a radius: "))

volume = (4/3) * (math.pi)*(rad**3)
rvolume = round(volume,1)

print(f"The volume is: {rvolume}")