
# Simplify Path
# https://leetcode.com/problems/simplify-path/


import re

def func(path: str) -> str:

    if len(path) == 0 or path[0] != '/':
        return 'InvalidPath' 
    
    if path[-1] != '/':
        path += '/'

    # merge "/" chars sucessive.
    path = re.sub(r'/{2,}', '/', path)
    # remove current folder anotation.
    path = re.sub(r'/\.{1}/', '/', path)
    # remove back last folder anotation.
    path = re.sub(r'/[^\/\.]+/\.{2}/', '/', path)  # can be improve, for case folder name contain dot.
    path = re.sub(r'^/(\.{2}/)+', '/', path)  # same, for when it start by back last folder.

    if len(path) > 1:
        path = path[:-1]

    return path



print(func('/home/'))  # /home
print(func('/home//foo/'))  # /home/foo
print(func('/home/user/Documents/../Pictures'))  # /home/user/Pictures
print(func('/../'))  # /
print(func('/../..'))  # /
print(func('/../../'))  # /
print(func('/../.././..'))  # /
print(func('/../../test/../..'))  # /
print(func('/.../a/../b/c/../d/./'))  # /.../b/d