
class HashableList(list):  # warning, do not edit the list, it change the hash value.
    
    def __hash__(self):
        return hash(tuple(self))