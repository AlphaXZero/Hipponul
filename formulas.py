"""Formulas Module"""

import math

ALPHA = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def format_nibble(binary_repr, fill=0):
    """formats a list of characters into a single string of nibbles
    fill=1 optional to complete first nibble with 0"""
    if len(binary_repr) % 4 != 0 and fill == 1:
        for _ in range(4 - (len(binary_repr) % 4)):
            binary_repr.insert(0, "0")
    return " ".join(
        "".join(binary_repr[i : i + 4]) for i in range(0, len(binary_repr), 4)
    )


def str_to_list(entry):
    """takes a string representing a number in any base and returns a list of each of its digits
    from the integer part only"""
    entry = entry.split(".")[0]
    return list(map(ALPHA.index, entry.upper()))


def _get_msb(nbr, base):
    """takes a string representing a number in any base and his base and return the MSB"""
    if nbr == 0:
        return 0
    return int(math.log(nbr, base))


def dec_to_base_y(nbr, base):
    """takes a int and a base and returns a list of string of the number in the base wanted"""
    msb = _get_msb(nbr, base)
    rep = []
    for j in range(msb, -1, -1):
        rep.append(ALPHA[nbr // base**j])
        nbr %= base**j
    return rep


def base_x_to_base_y(nbr_repr, base_s, base_w):
    """take a string representing a number in any base, the starting base and the base wanted
    returns a list of characters representing the number in the base wanted"""
    return dec_to_base_y(int(nbr_repr, base_s), base_w)


def comma(nbr, nbr_bits=11):
    """take a float and return the non-integer part in a list
    optional nbr_bits = x where x is the number of bits wanted"""
    binary_rep = []
    nbr -= int(nbr)
    for _ in range(nbr_bits):
        nbr *= 2
        if nbr >= 1:
            binary_rep.append(1)
            nbr -= 1
        else:
            binary_rep.append(0)
    return binary_rep


def bin_to_comma(binary_repr):
    """takes a binary representation of a number as a list of ints and
    returns its value, but only after a leading"""
    nbr = 0
    for i, bit in enumerate(binary_repr):
        try:
            nbr += 1 / (bit * 2 ** (i + 1))
        except ZeroDivisionError:
            continue
    return nbr


def half_float_to_dec(binary_repr):
    """take a represention of a half-float as a list of ints and returns his value"""
    sign = -1 if binary_repr[0] == 1 else 1
    exponent = int("".join(map(str, binary_repr[1:6])), 2) - 15
    mantissa = 1 + bin_to_comma(binary_repr[6:])
    return sign * mantissa * (2**exponent)

#TODO marche pas nbr <1 && nbr <O.
def half_float(nbr):
    """take a a float and return his half_float representationa as a list of ints"""
    hf_final = [0] * 16
    hf_final[0] = 1 if nbr < 0 else 0
    nbr = abs(nbr)
    binary_repr = list(reversed(bin(int(nbr))[3:]))
    exponent_repr = list(bin(15 + len(binary_repr))[2:])
    comma_repr = list(reversed(comma(nbr)))
    for i in range(1,16):
        if 0 < i < 6:
            hf_final[i] = int(exponent_repr[i-1])
        else:
            if binary_repr:
                hf_final[i] = int(binary_repr.pop())
            else:
                hf_final[i] = comma_repr.pop()
    return hf_final


if __name__ == "__main__":
    print(base_x_to_base_y("0101 0111 1011 0000",2,16))
