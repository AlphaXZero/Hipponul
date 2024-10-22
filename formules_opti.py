import math

ALPHA = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def format_nibble(binary_repr):
    """formats a list of characters into a single string of nibbles"""
    if len(binary_repr) % 4 != 0:
        for _ in range(4 - (len(binary_repr) % 4)):
            binary_repr.insert(0, "0")
    return " ".join(
        "".join(binary_repr[i : i + 4]) for i in range(0, len(binary_repr), 4)
    )


def bit_fort(nbr, base):
    """takes a string representing a number in any base and his base and return the MSB"""
    if nbr == 0:
        return 0
    return int(math.log(nbr, base))


def dec_to_y(nbr, base):
    """takes a int and a base and returns a list of string of the number in the base wanted"""
    MSB = bit_fort(nbr, base)
    rep = []
    for j in range(MSB, -1, -1):
        rep.append(ALPHA[nbr // base**j])
        nbr %= base**j
    return rep


if __name__ == "__main__":
    print(math.log(120, 2))
    print(dec_to_y(120, 16))
