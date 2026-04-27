
# Biger Divider (Medium).
# (?)

# take two number, and return the bigest commun divider.

def bigerDivider(num_a: int, num_b: int) -> int:

    if num_b < num_a:
        (num_a, num_b) = (num_b, num_a)

    for i in range(num_a, 1, -1):
        if num_b % i == 0 and num_a % 2 == 0:
            return i
    return 1
        
print(bigerDivider(8,16))
print(bigerDivider(5,3))