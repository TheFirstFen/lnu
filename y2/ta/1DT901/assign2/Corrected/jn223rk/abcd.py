def reverse(s):
    reverse_s = ""
    for i in s:
        reverse_s = i + reverse_s
    return reverse_s


def main():
    abcd = 0
    dcba = 0

    for i in range(1000, 10000, 1):
        abcd = i
        # Statement to make sure to ignore cases such that a or d is equal to 0
        if abcd / 10 != abcd // 10:
            # print(i, end=" ")
            str_abcd = str(abcd)
            str_dcba = reverse(str_abcd)
            dcba = int(str_dcba)
            if 4 * abcd == dcba:
                # print(abcd, dcba)
                break
    print("DCBA = 4 * ABCD when ABCD = {} and DCBA = {}"
          .format(abcd, dcba))


if __name__ == "__main__":
    main()
