
# LRU Cache (Medium).
# (?)

# take an array of char, and place it one by one in an cache memory (length 5), and return what contain the cache at end of process.


def lruCache(arr, length_cache: int=5):

    cache = []
    for i in range(len(arr)):
        char = arr[i]

        if len(cache) < length_cache:
            cache.append(char)
        
        index_cach = i % length_cache
        cache[index_cach] = char

    return cache



print(lruCache(list('aabbcc')))
print(lruCache(list('aaaaaa')))
print(lruCache(list('abcabcabcabc')))