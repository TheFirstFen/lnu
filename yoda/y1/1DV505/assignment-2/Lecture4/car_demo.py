from car_class import Car

# original
cars = [Car("Volvo", "XC90"), Car("Volvo", "V60"), Car("Audi", "A6")]

print("Original cars")
for car in cars:
    print(car)

cars[1].set_make = "XC60"
print("\nAfter modifying the second car")
for car in cars:
    print(car)
