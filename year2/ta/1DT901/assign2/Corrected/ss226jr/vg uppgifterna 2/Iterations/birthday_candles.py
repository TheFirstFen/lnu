# start
def can():
    c = 0            # remaining candles
    b = 0            # total number of boxes
    for a in range(1, 101):
        c += a       # age
        if c >= 24:
            b2 = c // 24      # boxes per age
            b += b2
            c %= 24

            print(f'Before birthday {a}, buy {b2} box(es)')

    print(f'\nTotal number of boxes: {b}, Remaining candles: {c}')


can()
