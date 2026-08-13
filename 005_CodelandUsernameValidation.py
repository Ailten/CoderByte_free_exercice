
# Codeland Username Validation (medium).
# https://coderbyte.com/information/Codeland%20Username%20Validation

import re

def CodelandUsernameValidation(strParam):

  matches = re.search('^[a-zA-Z][a-zA-Z0-9_]{2,23}[^_]$', strParam)
  return matches != None


# keep this function call here 
print(CodelandUsernameValidation('aaa_'))
