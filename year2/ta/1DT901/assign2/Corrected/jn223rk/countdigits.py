def main():
    n = input("Enter a large positive integer: ")
    count_even = 0
    count_zero = 0
    count_odd = 0
    for i in n:
        if int(i) == 0:
            count_zero += 1
        elif int(i) % 2 == 0:
            count_even += 1
        elif int(i) % 2 == 1:
            count_odd += 1
    print("Zeros: {}".format(count_zero))
    print("Odd: {}".format(count_odd))
    print("Even: {}".format(count_even))


if __name__ == "__main__":
    main()
