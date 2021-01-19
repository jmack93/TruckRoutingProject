# John R. McKahan II Student ID:

class Hashfile:


    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    #This returns the hash value, given the key
    def get_hash(self, key):
        hash = int(key) % len(self.table)
        return hash
    #This adds a new value to the hashtable, given a key value pair
    def add_value(self, key, value):
        hashkey = self.get_hash(key)
        valueinfo = [key, value]

        if self.table[hashkey] is None:
            self.table[hashkey] = list([valueinfo])
            return True
        else:
            for valuepairs in self.table[hashkey]:
                if valuepairs[0] == key:
                    valuepairs[1] = value
                    return True
            self.table[hashkey].append(valueinfo)
            return True
    #This returns a value from the hashtable, that corresponds with a key/value pair
    def get_value(self, key):
        hashkey = self.get_hash(key)
        if self.table[hashkey] is not None:
            for valuepairs in self.table[hashkey]:
                if valuepairs[0] == key:
                    return valuepairs[1]
        return None



    #This deletes a value from the hashtable
    def delete_value(self, key):
        hashkey = self.get_hash(key)
        if self.table[hashkey] is None:
            return False
        for i in range (0, len(self.table[hashkey])):
            if self.table[hashkey][i][0] == key:
                self.table[hashkey].pop(i)
                return True