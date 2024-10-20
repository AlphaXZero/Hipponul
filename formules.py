"""Formulas Module"""

ALPHAS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHA = [x for x in ALPHAS]

def dec_to_bin(nbr, nbits=0):
    binary_repr = []
    abs(nbr)
    while nbr > 0:
        if nbr%2==0:
            binary_repr.insert(0, 0)
        else:
            binary_repr.insert(0, 1)
        nbr //= 2
    while nbits > len(binary_repr):
        binary_repr.insert(0, 0)
    return binary_repr


def bin_to_dec(binary_repr):
    result = 0
    size = len(binary_repr)
    while len(binary_repr) > 0:
        result += (2 ** (size - len(binary_repr))) * binary_repr.pop()
    return result


def bit_fort(nbr, x):
    i = 0
    while True:
        if nbr <= (x**i) - 1:
            return i
        i += 1


def x_to_dec(representation, x):
    oui = str_to_list(representation)
    tot = 0
    for i in range(len(oui)):
        if oui[i] >= x:
            return "overflow"
        tot += oui[-i - 1] * x**i
    return tot


def dec_to_y(nbr, x):
    val_actu = nbr
    bitfort = bit_fort(val_actu, x)
    oui = []
    for j in range(1, bitfort + 1):
        for i in range(x - 1, -1, -1):
            if (val_actu - (i * x ** (bitfort - j))) >= 0:
                oui.append(ALPHA[i])
                val_actu -= i * x ** (bitfort - j)
                break
    return oui

def x_to_y(nbr,x,y):
    return dec_to_y(x_to_dec(nbr,x),y)


def virgule(nbr, oui=11):
    representation_binaire = []
    nbr = nbr - int(nbr)
    for _ in range(oui):
        nbr *= 2
        if nbr >= 1:
            representation_binaire.append(1)
            nbr -= 1
        else:
            representation_binaire.append(0)
    return representation_binaire


def half_float(nbr_dec):
    hf_final = [0 for i in range(16)]
    if nbr_dec < 0:
        hf_final[0] = 1
        nbr_dec *= -1
    binary_repr = dec_to_bin(int(nbr_dec))
    rBin_unsigned = binary_repr[1:]
    exponent=15+len(rBin_unsigned)
    exponent_bits = dec_to_bin(exponent, 5)
    for i in range(len(rBin_unsigned)):
        if i >= 10:
            break
        hf_final[i + 6] = rBin_unsigned[i]
    for i in range(5):
        hf_final[i + 1] = exponent_bits[i]
    vir = virgule(nbr_dec)
    for i in range(10 - len(rBin_unsigned)):
        if i >= 0:
            hf_final[i + 6 + len(rBin_unsigned)] = vir[i]
        else:
            break
    return hf_final


def float_format(nbr_dec, tot=32, mantisse=23):
    hf_final = [0 for i in range(tot)]
    if nbr_dec < 0:
        hf_final[0] = 1
        nbr_dec *= -1
    binary_repr = dec_to_bin(int(nbr_dec))
    rBin_unsigned = binary_repr[1:]
    for i in range(len(rBin_unsigned)):
        if i >= mantisse:
            break
        hf_final[i + (tot - mantisse)] = rBin_unsigned[i]
    n = dec_to_bin(127 + (len(rBin_unsigned)), tot - mantisse - 1)
    for i in range(tot - mantisse - 1):
        hf_final[i + 1] = n[i]
    vir = virgule(nbr_dec, mantisse)
    for i in range(mantisse - len(rBin_unsigned)):
        if i >= 0:
            hf_final[i + (tot - mantisse) + len(rBin_unsigned)] = vir[i]
        else:
            break
    return hf_final


def half_float_to_dec(binary_repr):
    sign = -1 if binary_repr[0] == 1 else 1
    exposant = bin_to_dec(binary_repr[1:6]) - 15
    mantisse = 1 + bin_to_virgule(binary_repr[6:])
    return sign * mantisse * (2**exposant)


def bin_to_virgule(binary_repr):
    nbr = 0
    for i in range(len(binary_repr)):
        try:
            nbr += 1 / (binary_repr[i] * 2 ** (i + 1))
        except:
            continue
    return nbr


def tranfo_neg(binary_repr):
    for i in range(1, len(binary_repr)):
        if binary_repr[-i] == 1:
            for j in range(1, len(binary_repr) - i):
                binary_repr[j] = 0 if binary_repr[j] == 1 else 1
            return binary_repr


def formatage(oui, nbrBits=8):
    if len(oui) < nbrBits:
        for i in range(nbrBits - len(oui)):
            oui.insert(0, 0)
    return oui


def pribi(b):
    oui = ""
    non = ""
    for i in range(len(b)):
        oui += "{}".format(b[i])
    for i in range(len(b)):
        non += " {}".format(b[i]) if (len(oui) - i) % 4 == 0 else "{}".format(b[i])
    return non


def str_to_list(entry):
    array = []
    for i in entry:
        if i ==".":
            break
        try:
            array.append(ALPHA.index(i))
        except ValueError:
            continue
    return array
    # TODO map


if __name__ == "__main__":
    print(pribi(half_float(16)))
    print(half_float_to_dec(str_to_list("0100 1100 0000 0000")))

