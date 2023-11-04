def main():
    birthday_candle_box_total = 0
    birthday_candle_remainder = 0

    for i in range(1, 101):
        birthday_candle_box = 0
        while (birthday_candle_remainder < i):
            birthday_candle_box += 1
            birthday_candle_remainder += 24
        birthday_candle_box_total += birthday_candle_box
        birthday_candle_remainder -= i
        birthday = "Before birthday {}, buy {} box(es)".format(
            i, birthday_candle_box
        )
        print(birthday)

    total_candles = "\nTotal number of boxes: {}, Remaining candles: {}"\
        .format(birthday_candle_box_total, birthday_candle_remainder)
    print(total_candles)

    print(211 * 24 - 14)
    print(210 * 24 + 10)
    print(5050 // 24 + 1, 24 - 5050 % 24)


if __name__ == "__main__":
    main()
