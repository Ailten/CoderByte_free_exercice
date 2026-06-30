
# Add Binary.
# https://leetcode.com/problems/add-binary/


import re

def addBin(a: str, b: str) -> str:

    def castStrToBin(str_val: str) -> int:
        output = 0
        for i in range(len(str_val)):
            if str_val[i] == '0':
                continue
            inverted_i = len(str_val) - 1 - i
            output |= 1 << inverted_i
        return output
    
    def castBinToStr(bin_val: int, length_bin: int = 8) -> str:
        output = []
        for i in range(length_bin):
            inverted_i = length_bin - 1 - i
            output.append('1' if (bin_val >> inverted_i) & 1 == 1 else '0')
        return ''.join(output)
    

    int_a = castStrToBin(a)  # cast int, add, cast bin.
    int_b = castStrToBin(b)
    int_sum = int_a + int_b
    str_sum = castBinToStr(int_sum)

    #print(f'{a.rjust(8, "0")} + {b.rjust(8, "0")} = {str_sum}')  # debug.
    #print(f'{str(int_a).rjust(8, " ")} + {str(int_b).rjust(8, " ")} = {str(int_sum).rjust(8, " ")}')

    str_sum_match = re.search(r'1[01]*$', str_sum)  # remove '0' left.
    str_sum = '0' if str_sum_match == None else str_sum_match.group()
    return str_sum


print('< v1 >')
print(addBin('0','1'))  # 1.
print(addBin('1','0'))  # 1.
print(addBin('0','0'))  # 0.
print(addBin('1','1'))  # 10.
print(addBin('101','10'))  # 111.
print(addBin('101','11'))  # 1000.


# -----------> v2.


def addBin_v2(a: str, b: str) -> str:

    a = a[::-1]  # invert order.
    b = b[::-1]

    if len(a) > len(b):  # place a as min length of both.
        (a,b) = (b,a)

    output = []

    is_report = False
    for i in range(len(a)):
        bool_a = a[i] == '1'
        bool_b = b[i] == '1'
        is_digit = (bool_a ^ bool_b) ^is_report
        output.append('1' if is_digit else '0')
        is_report = (bool_a and bool_b) or (bool_a and is_report) or (bool_b and is_report)
    
    b = b[len(a):]
    if is_report:
        if len(b) == 0:
            output.append('1')
        else:
            for i in range(len(b)):
                if not is_report:
                    output.append(b[i:])
                    break
                b_bool = b[i] == '1'
                output.append('1' if b_bool ^ is_report else '0')
                is_report = b_bool and is_report
            if is_report:
                output.append('1')
    elif len(b) > 0:
        output.append(b)
    
    return (''.join(output))[::-1]



print('< v2 >')
print(addBin_v2('0','1'))  # 1.
print(addBin_v2('1','0'))  # 1.
print(addBin_v2('0','0'))  # 0.
print(addBin_v2('1','1'))  # 10.
print(addBin_v2('101','10'))  # 111.
print(addBin_v2('101','11'))  # 1000.