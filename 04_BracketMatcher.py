
# Bracket Matcher (medium).
# https://coderbyte.com/information/Bracket%20Matcher

def BracketMatcher(strParam):

  open_count = 0
  for s in strParam:
    is_bracket_open = s == '('
    is_bracket_close = s == ')' 

    if not is_bracket_open and not is_bracket_close:
      continue

    if is_bracket_open:
      open_count += 1
      continue

    if is_bracket_close:
      if open_count == 0:
        return 0
      open_count -= 1

  return 1 if open_count == 0 else 0


# keep this function call here 
print(BracketMatcher('(hello())'))