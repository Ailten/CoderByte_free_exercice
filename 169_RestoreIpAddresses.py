
# restore IP Addresses.
# https://leetcode.com/problems/restore-ip-addresses/


import re

def restoreIpAddresses(s: str) -> list[str]:

    if re.match('^[0-9]{4,12}$', s) == None:
        return []
    if len(s) == 4:
        return ['.'.join(list(s))]
    
    def isNumValid(num: str) -> bool:
        if len(num) >= 2 and num[0] == '0':
            return False
        if int(num) > 255:
            return False
        return True
    
    def getBitPos(num: int, lenght:int=11) -> list[int]:
        bit_count = []
        for i in range(lenght):
            if num >> i & 1 == 1:
                bit_count += [i]
        return bit_count
    
    ip_valids = []

    last_path = ((1 << len(s)) -1 ) ^ ((1 << (len(s)-3)) -1 )  # 3 bite at end.
    first_path = 7  # 3 bite at start.
    for i in range(first_path, last_path):
        bit_pos = getBitPos(i)

        if len(bit_pos) != 3:
            continue
        if bit_pos[-1] == len(s) - 1:  # skip if last bit is making last ip_num empty.
            continue

        ip_nums = [
            s[:bit_pos[0]+1],
            s[bit_pos[0]+1:bit_pos[1]+1],
            s[bit_pos[1]+1:bit_pos[2]+1],
            s[bit_pos[2]+1:]
        ]
        try:
            if (
                not isNumValid(ip_nums[0]) or
                not isNumValid(ip_nums[1]) or
                not isNumValid(ip_nums[2]) or 
                not isNumValid(ip_nums[3])
            ):
                continue
        except:
            print('err')
            print(ip_nums)
            return []

        ip_valids.append('.'.join(ip_nums))

    return ip_valids

    

print(restoreIpAddresses('25525511135'))  # ['255.255.11.135', '255.255.111.35'].
print(restoreIpAddresses('0000'))  # ["0.0.0.0"].
print(restoreIpAddresses('101023'))  # ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"].