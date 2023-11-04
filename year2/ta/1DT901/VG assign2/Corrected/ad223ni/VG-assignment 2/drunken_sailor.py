import random


def simulate_drunken_sailors(size, num_steps, num_sailors):
    boundary = range(-size, size+1)
    sailors_fallen = 0

    for _ in range(num_sailors):
        x, y = 0, 0
        for _ in range(num_steps):
            direction = random.choice(['up', 'down', 'left', 'right'])
            if direction == 'up':
                y += 1
            elif direction == 'down':
                y -= 1
            elif direction == 'left':
                x -= 1
            elif direction == 'right':
                x += 1

            if x not in boundary or y not in boundary:
                sailors_fallen += 1
                break

    return sailors_fallen


size = int(input("Enter the size: "))
num_steps = int(input("Enter the number of steps: "))
num_sailors = int(input("Enter the number of sailors: "))

sailors_fallen = simulate_drunken_sailors(size, num_steps, num_sailors)
percentage_fallen = (sailors_fallen / num_sailors) * 100

print(f"Out of {num_sailors} drunk sailors, {sailors_fallen}, "
      f"({percentage_fallen: .2f}%) fell into the water.")
