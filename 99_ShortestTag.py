
# Shortest tag html.
# /

# take a string, return the shortest tag-name balise html on it.

import re

def shortestBalise(line: str) -> str:

    tags = re.findall(r'<(.+?)>', line)
    tags.sort(key=lambda e: len(e))
    return tags[0]



print(shortestBalise('aabb<ab>tde<a>zdfdg<abb>'))