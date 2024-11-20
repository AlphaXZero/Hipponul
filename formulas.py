"""Formulas Module"""

import math

ALPHA = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def add_zeros(binary_repr, count_bit):
    """If not enough bit in binary_repr add 0 in front of the list"""
    if len(binary_repr) % count_bit != 0:
        for _ in range(count_bit - (len(binary_repr) % count_bit)):
            binary_repr.insert(0, 0)
    return binary_repr


def format_nibble(binary_repr):
    """formats a list of characters into a single string of nibbles"""
    binary_repr = [str(i) for i in add_zeros(binary_repr, (len(binary_repr)+(4-len(binary_repr)%4)%4))]
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


def comma(nbr, nbr_bits=30):
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
        if bit:
            nbr += 1 / 2 ** (i + 1)
    return nbr


def half_float_to_dec(binary_repr):
    """take a represention of a half-float as a list of ints and returns his value"""
    binary_repr = (
        add_zeros(list(map(int, (base_x_to_base_y(binary_repr, 16, 2)))), 16)
        if len(binary_repr) == 4
        else binary_repr
    )
    if 1 not in binary_repr[1:6]:
        return "dénormalisé(Den) ou 0"
    if 0 not in binary_repr[1:6]:
        return "infini" if 1 not in binary_repr[6:] else "NaN"
    sign = -1 if binary_repr[0] == 1 else 1
    exponent = int("".join(map(str, binary_repr[1:6])), 2) - 15
    mantissa = 1 + bin_to_comma(binary_repr[6:])

    return sign * mantissa * (2**exponent)


def half_flaot_to_dec_2(binary_repr):
    """take a represention of a half-float as a list of ints and returns his value but with a sum of 2exponent"""
    binary_repr = (
        add_zeros(list(map(int, (base_x_to_base_y(binary_repr, 16, 2)))), 16)
        if len(binary_repr) == 4
        else list(map(int,binary_repr))
    )
    exponent = int("".join(map(str, binary_repr[1:6])), 2) - 15
    mantissa = [1] + binary_repr[6:]
    result=""
    for i, val in enumerate(mantissa):
        result += f" 2**{exponent-i} +" if val == 1 else ""
    return result[1:-2]


def half_float(nbr):
    """take a a float and return his half_float representationa as a list of ints"""
    if abs(nbr) > 65504:
        return "+infinity" if nbr > 65504 else "-infinty"
    hf_final = [0] * 16
    sign = [1] if nbr < 0 else [0]
    nbr = abs(nbr)
    binary_repr = [int(digit) for digit in bin(int(nbr))[2:]]
    comma_repr = comma(nbr)
    concatenate = binary_repr + comma_repr
    if 1 not in concatenate:
        return hf_final
    first_1 = concatenate.index(1)
    exponent_value = (
        15 - len(concatenate[:first_1])
        if binary_repr[0] == 0 and len(binary_repr) == 1
        else 14 + len(binary_repr)
    )
    concatenate = concatenate[first_1 + 1 : first_1 + 11]
    exponent_repr = add_zeros([int(digit) for digit in bin(exponent_value)[2:]], 5)
    return sign + exponent_repr + concatenate


if __name__ == "__main__":
    print(half_float_to_dec([0,1,0,0,1,1,0,1,1,0,1,0,0,0,0,0]))
    