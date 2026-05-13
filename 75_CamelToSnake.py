
# Camel to Snake (Easy).
# (None)

# cast a string camel case, in snake case.


import re

def camelToSnake(line: str) -> str:
    return re.sub(r'(.)([A-Z])', r'\1_\2', line).lower()

print(camelToSnake('aaaTest'))