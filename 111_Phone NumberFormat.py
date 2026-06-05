# Take an array with numbers from 0-9, return 'Invalid Format' if the format isn't valid
# If the array has 10 numbers and doesn't begin with a 0 or a 1, the format should be XXX-XXX-XXXX.
# If the array begins with a 1 and has 11 numbers it should have a format of +1 (XXX) XXX-XXXX.
# If the array begins with 800 or 888 and has 10 numbers, the format should be (XXX) XXX-XXXX.

import re

def format_phone_number(numbers: list[int]) -> str:
    
    num_str = ''.join([ str(n) for n in numbers ])
    if re.search(r'^[2-9][0-9]{9}$', num_str) != None:
        return re.sub(r'^([0-9]{3})([0-9]{3})([0-9]{4})$', r'\1-\2-\3', num_str)
    if re.search(r'^1[0-9]{10}$', num_str) != None:
        return re.sub(r'^([0-9]{3})([0-9]{3})([0-9]{4})$', r'+1 (\1) \2-\3', num_str)
    if re.search(r'^(800|888)[0-9]{7}$', num_str) != None:
        return re.sub(r'^([0-9]{3})([0-9]{3})([0-9]{4})$', r'(\1) \2-\3', num_str)
    return 'Invalid Format'



def test_code(test_value, correct_value):
    if test_value == correct_value:
        print(f'Test passed succesfully ! ({test_value})')
    else:
        print(f'Test failed ! Given value was {test_value} but correct value was {correct_value}')



test_code(format_phone_number([1,1,5,4,4,8,6,8,5,2,3]), '+1 (154) 486-8523')
test_code(format_phone_number([1,8,5,7,6,3,6,4,8,2,3]), '+1 (857) 636-4823')
test_code(format_phone_number([8,8,8,4,8,6,8,5,6,2]), '(888) 486-8562')
test_code(format_phone_number([8,0,0,4,8,6,1,5,8,2]), '(800) 486-1582')
test_code(format_phone_number([2,5,8,6,3,4,5,8,9,6]), '258-634-5896')
test_code(format_phone_number([8,6,2,4,7,9,2,1,0,3]), '862-479-2103')
test_code(format_phone_number([8,6,2,4,7,9,2,1,3]), 'Invalid Format')
test_code(format_phone_number([1,6,2,4,7,9,2,1,3,8]), 'Invalid Format')
test_code(format_phone_number([0,5,8,9,6,3,4,7,8,9]), 'Invalid Format')
test_code(format_phone_number([2,1,5,4,4,8,6,8,5,2,3]), 'Invalid Format')
test_code(format_phone_number([1,1,5,4,4,8,6,8,5,2,3,8]), 'Invalid Format')
test_code(format_phone_number([]), 'Invalid Format')