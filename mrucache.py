class MRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.access_history = []

    def get(self, key):
        if key in self.cache:
            self.access_history.remove(key)
            self.access_history.append(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.access_history.remove(key)
        else:
            if len(self.cache) >= self.capacity:
                mru_key = self.access_history.pop()
                del self.cache[mru_key]
            self.cache[key] = value
        self.access_history.append(key)
mru_cache = MRUCache(3)
mru_cache.put(1, 'One')
mru_cache.put(2, 'Two')
mru_cache.put(3, 'Three')
print(mru_cache.get(1))  # Output: 'One'
mru_cache.put(4, 'Four')
print(mru_cache.get(3)) 
