
# Longest Word (easy).
# https://coderbyte.com/information/Longest%20Word

import re

def LongestWord(sen):

  all_words = re.findall('[a-z]{1,}', sen)
  all_words.sort(key=lambda e: len(e), reverse=True)
  return all_words[0]

# keep this function call here 
print(LongestWord('hello --- Word'))