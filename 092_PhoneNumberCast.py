
# phone number cast
# /

# take a string of phone number "040 00 00 000" ad convert it to an international number "+32 00 00 00 000"

import re

def toInterPhoneNum(phone_num: str) -> str:

    return re.sub(r'^[0-9]([0-9]{2})', r'+32 \1', phone_num)



print(toInterPhoneNum('042 12 23 345'))  # '+32 42 12 23 345'