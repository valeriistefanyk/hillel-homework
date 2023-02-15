class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return key % self.size

    def put(self, key, value):
        hash_key = self._hash_function(key)
        for index, element in enumerate(self.hash_table[hash_key]):
            if element[0] == key:
                self.hash_table[hash_key][index] = (key, value)
                return
        self.hash_table[hash_key].append((key, value))

    def get(self, key):
        hash_key = self._hash_function(key)
        for element in self.hash_table[hash_key]:
            if element[0] == key:
                return element[1]
        return None

    def delete(self, key):
        hash_key = self._hash_function(key)
        for index, element in enumerate(self.hash_table[hash_key]):
            if element[0] == key:
                del self.hash_table[hash_key][index]
                return


if __name__ == '__main__':
    ht = HashTable(5)

    ht.put(1, "one")
    ht.put(2, "two")
    ht.put(3, "three")

    print(ht.get(1))  # виведе: "one"
    print(ht.get(4))  # виведе: None

    ht.delete(2)
    print(ht.get(2))  # виведе: None
