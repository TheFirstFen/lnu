def bitstring(x):  return bin(x)[2:]
def printlongdiv(lhs, rhs):
    rem = lhs
    div = rhs
    origlen = len(bitstring(div))

    # first shift left until the leftmost bits line up.
    count = 1
    while (div | rem) > 2*div:
        div <<= 1
        count += 1

    # now keep dividing until we are back where we started.
    quot = 0
    while count>0:
        quot <<= 1
        count -= 1
        print("%14s" % bitstring(rem))
        divstr = bitstring(div)
        if (rem ^ div) < rem:
            quot |= 1
            rem ^= div

            print(1, " " * (11-len(divstr)), divstr[:origlen])
        else:
            print(0, " " * (11-len(divstr)), "0" * origlen)
        print(" " * (13-len(divstr)), "-" * origlen)
        div >>= 1
    print("%14s <<< remainder" % bitstring(rem))
    print(" -> %10s <<< quotient" % bitstring(quot))

printlongdiv(0x1A8, 11)
