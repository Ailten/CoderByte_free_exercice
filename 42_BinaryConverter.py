
# Binary Converter (Medium).
# (?)

# convert a string (represent of binary) into a base 10 number.

def binaryConverter(binary: str) -> int:

    int_out = 0
    for b in binary:
        int_out <<= 1
        int_out += 1 if b == '1' else 0
    return int_out

print(binaryConverter('001'))
print(binaryConverter('010'))
print(binaryConverter('011'))
print(binaryConverter('100'))
print(binaryConverter('101'))