import re

# Count Minutes I (Easy).
# (?)

# take a string (like "9:00am-10:00am") and return an int of how many minutes is separated both.


def countMinutesI(line):

    # TODO: what suposed to do when the second is under the first time ? (return negative int or + 24hours).

    arr_hours = re.findall('[0-9]{1,2}[:][0-9]{2}[ap][m]', line)

    arr_minutes = [0, 0]
    for i in range(len(arr_hours)):
        h = arr_hours[i]

        if re.search('pm$', h) != None:
            arr_minutes[i] += 12 * 60

        h_hours_minutes = [ int(e) for e in re.findall('[0-9]{1,2}', h) ]
        arr_minutes[i] += h_hours_minutes[0] * 60
        arr_minutes[i] += h_hours_minutes[1]

    return arr_minutes[1] - arr_minutes[0]




print(countMinutesI('9:00am-10:00am'))
print(countMinutesI('9:00am-9:00pm'))
print(countMinutesI('8:00am-8:30am'))
print(countMinutesI('8:00am-8:00am'))