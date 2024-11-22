import formulas

msg = formulas.base_x_to_base_y("3e0C4", 16, 2)
msg = [int(i) for i in msg]
print(msg)
CLEF = "110010100"
CLEF = [int(i) for i in CLEF]
maxi = len(msg)
a = 0
for i, data in enumerate(msg):
    if data == 1:
        for j, data2 in enumerate(CLEF):
            if i + j < maxi:
                msg[i + j] = int(data != data2)
            elif a < len(CLEF) - 1:
                msg.append(int(data != data2))
                a+=1
print(msg)
print(msg[maxi:])
