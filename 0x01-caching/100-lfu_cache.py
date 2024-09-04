from base_caching import BaseCaching
from collections import defaultdict, OrderedDict

class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.freqs = defaultdict(int)  # Track frequencies
        self.usage_order = OrderedDict()  # Track order of usage

    def put(self, key, item):
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.cache_data[key] = item
            self.freqs[key] += 1
            self.usage_order.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_key = min(self.freqs, key=lambda k: (self.freqs[k], self.usage_order[k]))
                print(f"DISCARD: {lfu_key}")
                del self.cache_data[lfu_key]
                del self.freqs[lfu_key]
                del self.usage_order[lfu_key]

            self.cache_data[key] = item
            self.freqs[key] = 1
            self.usage_order[key] = None

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        
        self.freqs[key] += 1
        self.usage_order.move_to_end(key)
        return self.cache_data[key]
