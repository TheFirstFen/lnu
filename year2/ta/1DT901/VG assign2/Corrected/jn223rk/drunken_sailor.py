from random import randint


def main():
    size = int(input("Enter the size: "))
    steps = int(input("Enter the number of steps: "))
    sailors = int(input("Enter the number of sailors: "))
    fall_count = 0

    for i in range(sailors):
        horizontal = 0
        vertical = 0

        for j in range(steps):
            # Take the absolute values of the values
            horizontal = (horizontal ** 2) ** (1 / 2)
            vertical = (vertical ** 2) ** (1 / 2)
            # Check to see if the absolute values of
            # the vertical or the horizontal is greater than
            # the absolute value of the size
            if (horizontal > size or vertical > size):
                fall_count += 1
                break
            else:
                direction = randint(1, 4)
                match direction:
                    case 1:
                        vertical += 1
                    case 2:
                        horizontal += 1
                    case 3:
                        vertical -= 1
                    case 4:
                        horizontal -= 1

    fall_ratio = fall_count / sailors
    fall_percentage = str(round(fall_ratio * 100, 2)) + "%"
    message = ("Out of {} drunk sailors, {} ({}) fell into the water").format(
        sailors, fall_count, fall_percentage)
    print(message)


if __name__ == "__main__":
    main()
