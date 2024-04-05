if __name__ == "__main__":
    three_digit_number = int(input("Provide a three digit number: "))

    # Condition to check that the integer has only three digits
    if three_digit_number > 99 and three_digit_number < 1000:
        first_digit = three_digit_number // 100
        second_digit = (three_digit_number % 100) // 10
        third_digit = ((three_digit_number % 100) % 10)
        sum = first_digit + second_digit + third_digit
        print("Sum of digits: {}".format(sum))
