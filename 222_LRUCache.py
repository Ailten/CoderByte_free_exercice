

# LRU cache.
# https://leetcode.com/problems/lru-cache/

class BlockLRUValue:
    def __init__(self, key: int, value: int, index_last_edit: int):
        self.key = key
        self.value = value
        self.index_last_edit = index_last_edit

    def __str__(self) -> str:
        return f'({self.key}, {self.value})'


class LRUCache:

    def __init__(self, capacity: int):
        self.cache: list[BlockLRUValue] = []  # (key, val, index_last_edit)
        self.capacity = capacity
        self.index_action = 0
        

    def get(self, key: int) -> int:

        block_value = self.__get_by_key(key)  # get block.

        if block_value == None:  # not found.
            return -1
        
        self.index_action += 1  # edit last touch.
        block_value.index_last_edit = self.index_action

        return block_value.value
        

    def put(self, key: int, value: int) -> None:

        block_value = self.__get_by_key(key)  # get block.

        if block_value == None:

            if len(self.cache) == self.capacity:  # max capacity: remove the latest.
                self.cache.sort(key=lambda e: e.index_last_edit, reverse=True)
                self.cache.pop()
            
            block_value = BlockLRUValue(key, value, 0)  # add a new value.
            self.cache.append(block_value)

        self.index_action += 1  # edit touch.
        block_value.index_last_edit = self.index_action

        block_value.value = value  # apply value.


    def __get_by_key(self, key: int) -> BlockLRUValue | None:
        if len(self.cache) == 0:
            return None
        
        self.cache.sort(key=lambda e: e.key - key)
        return self.cache[0] if self.cache[0].key == key else None

    def __str__(self) -> str:
        return '[' + (', '.join([str(e) for e in self.cache])) + ']'


lRUCache = LRUCache(2)
lRUCache.put(1, 1)  # cache is {1=1}
lRUCache.put(2, 2)  # cache is {1=1, 2=2}
lRUCache.get(1)     # return 1
lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2)     # returns -1 (not found)
lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1)     # return -1 (not found)
lRUCache.get(3)     # return 3
lRUCache.get(4)     # return 4
print(lRUCache)

