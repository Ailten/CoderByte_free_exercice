
# Tree Constructor (medium).
# https://coderbyte.com/editor/Tree%20Constructor:Python3

import re

def TreeConstructor(strArr):

  dico = dict()
  for e in strArr:

    values_str = re.findall('[0-9]{1,}', e)
    if len(values_str) < 2:
      return None

    child = values_str[0]
    parent = values_str[1]

    if not parent in dico:
      dico.update({ parent: ( child, None ) })
    elif dico[parent][1] == None:
      dico[parent] = (dico[parent][0], child)
    else:
      return False

  return True


# keep this function call here 
print(TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]))