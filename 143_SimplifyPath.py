
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
    path = re.sub(r'/[^\/\.]+/\.{2}/', '/', path)  # FIXME: can be improve, for case folder name contain dot.
    path = re.sub(r'^/(\.{2}/)+', '/', path)  # same, for when it start by back last folder.

    if len(path) > 1:
        path = path[:-1]

    return path



print('< v1 >')
print(func('/home/'))  # /home
print(func('/home//foo/'))  # /home/foo
print(func('/home/user/Documents/../Pictures'))  # /home/user/Pictures
print(func('/../'))  # /
print(func('/../..'))  # /
print(func('/../../'))  # /
print(func('/../.././..'))  # /
print(func('/../../test/../..'))  # /
print(func('/.../a/../b/c/../d/./'))  # /.../b/d



def func_v2(path: str) -> str:

    # -- vertion split.
    if len(path) == 0 or path[0] != '/':
        return 'InvalidPath' 
    if len(path) == 1:
        return '/'
    if path[-1] == '/':
        path = path[:-1]
    
    arr_folder = path[1:].split('/')
    i = 0
    while i != len(arr_folder):
        match arr_folder[i]:
            case '.':
                arr_folder.pop(i)
                continue
            case '':
                arr_folder.pop(i)
                continue
            case '..':
                arr_folder.pop(i)
                if i > 0:
                    i -= 1
                    arr_folder.pop(i)
                continue
        i += 1

    return '/'+('/'.join(arr_folder))


print('< v2 >')
print(func_v2('/home/'))  # /home
print(func_v2('/home//foo/'))  # /home/foo
print(func_v2('/home/user/Documents/../Pictures'))  # /home/user/Pictures
print(func_v2('/../'))  # /
print(func_v2('/../..'))  # /
print(func_v2('/../../'))  # /
print(func_v2('/../.././..'))  # /
print(func_v2('/../../test/../..'))  # /
print(func_v2('/.../a/../b/c/../d/./'))  # /.../b/d