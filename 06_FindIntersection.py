
# Find Intersection (easy).
# https://coderbyte.com/information/Find%20Intersection

def FindIntersection(strArr):

  set_a = set(strArr[0].split(', '))
  set_b = set(strArr[1].split(', '))
  list_result = list(set_a & set_b)
  list_result.sort(key=lambda e: int(e))
  return list_result

# keep this function call here 
print(FindIntersection(input()))