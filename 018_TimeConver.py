
# Time Convert (Easy).
# (?)

# cast a num (amount of minutes), in string "hh:mm".


def timeConvert(num):

    hours = num // 60
    minutes = num % 60

    return f'{hours:0>2}:{minutes:0>2}'




print(timeConvert(00))
print(timeConvert(30))
print(timeConvert(60))
print(timeConvert(90))
print(timeConvert(120))
