#!/usr/bin/python3
""" 100-lfu_cache.py """

from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """LFUCache defines a cache with the Least Frequently Used (LFU) algorithm"""

    def __init__(self):
        """Initialize the LFUCache"""
        super().__init__()
        self.frequency = {}
        self.usage_order = []

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item value for the key key"""
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_frequent = min(self.frequency.values())
                least_used_keys = [k for k, v in self.frequency.items() if v == least_frequent]
                if len(least_used_keys) > 1:
                    lru_key = None
                    for k in self.usage_order:
                        if k in least_used_keys:
                            lru_key = k
                            break
                    self.cache_data.pop(lru_key)
                    self.frequency.pop(lru_key)
                    self.usage_order.remove(lru_key)
                    print("DISCARD:", lru_key)
                else:
                    lfu_key = least_used_keys[0]
                    self.cache_data.pop(lfu_key)
                    self.frequency.pop(lfu_key)
                    self.usage_order.remove(lfu_key)
                    print("DISCARD:", lfu_key)

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
