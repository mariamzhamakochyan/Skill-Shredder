from collections import defaultdict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.freq = defaultdict(list)
        self.min_freq = 0

    def _update_freq(self, key):
        freq = self.cache[key][1]
        self.freq[freq].remove(key)
        if not self.freq[self.min_freq]:
            self.min_freq += 1
        self.freq[freq + 1].append(key)
        self.cache[key][1] += 1

    def get(self, key):
        if key in self.cache:
            self._update_freq(key)
            return self.cache[key][0]
        return None

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            self._update_freq(key)
            self.cache[key][0] = value
        else:
            if len(self.cache) >= self.capacity:
                lfu_key = self.freq[self.min_freq].pop(0)
                del self.cache[lfu_key]
            self.cache[key] = [value, 1]
            self.freq[1].append(key)
            self.min_freq = 1
lfu = LFUCache(3)
lfu.put(1, 'One')
lfu.put(2, 'Two')
lfu.put(3, 'Three')
print(lfu.get(1))  
lfu.put(4, 'Four')
print(lfu.get(2)) 
