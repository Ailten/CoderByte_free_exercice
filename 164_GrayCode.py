
# gray code
# https://leetcode.com/problems/gray-code/


def grayCode(n: int) -> list[int]:

    def difBitCount(a: int, b: int, length: int=n) -> int:
        bit_count_a = 0
        bit_count_b = 0
        for i in range(n):
            if a >> i & 1 == 1:
                bit_count_a += 1
            if b >> i & 1 == 1:
                bit_count_b += 1
        return abs(bit_count_a - bit_count_b)
    
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
            if difBitCount(output[-1], 1) == 0:  # output valid.
                break

            #back_track_count = 1 if not is_back_track else back_track_count + 1
            is_back_track = True
            continue
        
        next_vals_allowed = [v for v in vals if difBitCount(v, output[-1])]
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


print(grayCode(2))  # [0,1,3,2]