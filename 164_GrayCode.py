
# gray code
# https://leetcode.com/problems/gray-code/


def grayCode(n: int) -> list[int]:

    def difBitCount(a: int, b: int, length: int=n) -> int:
        bit_dif_count = 0
        for i in range(n):
            if (a >> i & 1 == 1) ^ (b >> i & 1 == 1):
                bit_dif_count += 1
        return bit_dif_count

    def countBit(a: int, length: int=n) -> int:
        bit_count_a = 0
        for i in range(n):
            if a >> i & 1 == 1:
                bit_count_a += 1
        return bit_count_a
    
    def makeHashPath(list_of_elem: list[int], next_elem: int|None = None):
        hash_path = '.'.join([str(e) for e in list_of_elem])
        if next_elem != None:
            hash_path += '.'+str(try_next_val)
        return hash_path

    vals = list(range(pow(2,n)))
    output = [vals.pop(0)]
    is_back_track = False
    #back_track_count = 0
    path_eroned = []

    while len(vals) != 0:

        if is_back_track:

            if len(output) == 1:  # back track found no possible case.
                return []
            
            path_eroned.append(makeHashPath(output))
            
            #for i in range(back_track_count):
            vals.append(output.pop())
            is_back_track = False
            continue

        if len(vals) == 0:
            if countBit(output[-1]) == 1:  # output valid.
                break

            #back_track_count = 1 if not is_back_track else back_track_count + 1
            is_back_track = True
            continue
        
        next_vals_allowed = [v for v in vals if difBitCount(v, output[-1]) == 1]
        if len(next_vals_allowed) == 0:

            #back_track_count = 1 if not is_back_track else back_track_count + 1
            is_back_track = True
            continue

        next_val = None
        for try_next_val in next_vals_allowed:
            if not makeHashPath(output, try_next_val) in path_eroned:
                next_val = try_next_val
                break
        if next_val == None:

            #back_track_count = 1 if not is_back_track else back_track_count + 1
            is_back_track = True
            continue

        is_back_track = False
        output.append(next_val)
        vals.remove(next_val)

    return output


#print(grayCode(2))  # [0,1,3,2]

#v = 3
#r = grayCode(v)
#for e in r:
#    s = []
#    for i in range(v):
#        if e >> i & 1 == 1:
#            s.append('1')
#        else:
#            s.append('0')
#    print('-' + ''.join(s[::-1]))
#print(r)



# ----> v2

# by switching byte only (with a rule).
def grayCode_v2(n: int) -> list[int]:

    output = [0]
    for i in range(1, 1 << n):
        output.append(i ^ (i >> 1))
    return output


print(grayCode_v2(2))  # [0,1,3,2]





