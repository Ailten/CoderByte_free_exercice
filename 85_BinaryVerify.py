
# binary verify
# /

# 


def binaryVerify(value_base: int, value_filter: int) -> bool:

    output = 0

    for byte_index in range(0, 7):
        is_byte_filter = (value_filter >> byte_index) % 2 == 1
        if not is_byte_filter:
            continue
        
        is_byte_base = (value_base >> byte_index) % 2 == 1
        if not is_byte_base:
            return False

    return True



print(binaryVerify(7, 1))  # true.
print(binaryVerify(6, 1))  # false.
print(binaryVerify(6, 2))  # true.
print(binaryVerify(7, 3))  # true.
print(binaryVerify(7, 5))  # true. 