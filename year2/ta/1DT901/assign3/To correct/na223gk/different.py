import random


def different(lst):
    unique_elements = list(set(lst))
    unique_elements.sort()
    return unique_elements


def main():
    random_values = [random.randint(1, 200) for _ in range(100)]
    unique_elements = different(random_values)
    print(f"Original List: {random_values}")
    print(f"Unique Elements: {unique_elements}")


if __name__ == "__main__":
    main()
