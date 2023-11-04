def get_number(a, b, c, d):
    """Converts digits a, b, c, d into a four-digit integer abcd."""
    return (a * 1000) + (b * 100) + (c * 10) + d


def main():
    for a in range(1, 10):
        for b in range(10):
            for c in range(10):
                for d in range(1, 10):
                    abcd = get_number(a, b, c, d)
                    dcba = get_number(d, c, b, a)
                    if dcba == 4 * abcd:
                        print(f"A = {a}, B = {b}, C = {c}, D = {d}")
                        return


if __name__ == "__main__":
    main()
