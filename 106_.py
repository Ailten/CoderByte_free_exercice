
# take a string (repr of an int), invert these digit, and return an array of all digit added.


def func(line: str) -> list(str):

    num = int(line)
    num_invert = int(line[::-1])
    return list(str(num + num_invert))


print(func('123'))  # 4,4,4.