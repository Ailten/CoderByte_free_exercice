
# Min Window Substring (medium).
# https://coderbyte.com/information/Min%20Window%20Substring

import re

def MinWindowSubstring(strArr):

  full_str = strArr[0]
  chars = strArr[1]

  for len_range in range(len(chars), len(full_str) + 1):  # try gradually all range from the shortest.
    
    for start_index in range(0, len(full_str) - len_range + 1):

      last_index = len_range + start_index

      str_crop = full_str[start_index:last_index]

      if is_valid(str_crop, chars):
        return str_crop

  return None


# function to verify.
def is_valid(str_test, chars):
  for c in chars:
    if not c in str_test:
      return False
    str_test = str_test.replace(c, '', 1)
  return True


# keep this function call here 
print(MinWindowSubstring(['---abc---', 'abc']))