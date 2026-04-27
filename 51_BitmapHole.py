
# Bitmap Hole (Medium).
# (?)

# take an array fo array (of 0 and 1), and return how many '0' is surrend by '1' (in eatch direction).


def bitmapHole(arr):

    zero_count = 0

    for y in range(1, len(arr) - 1):
        for x in range(1, len(arr) - 1):
            if arr[y][x] != 0:
                continue
            if (
                arr[y+1][x  ] == 1 and
                arr[y-1][x  ] == 1 and
                arr[y  ][x+1] == 1 and
                arr[y  ][x-1] == 1
            ):
                zero_count+=1

    return zero_count




print(bitmapHole([
    [0,0,1,0],
    [0,1,0,0],
    [0,0,0,0],
    [0,0,1,0],
]))
print(bitmapHole([
    [0,1,0,0],
    [1,0,1,0],
    [0,1,0,0],
    [0,0,1,0],
]))
print(bitmapHole([
    [0,1,0,0],
    [1,0,1,1],
    [0,1,0,1],
    [0,0,1,0],
]))