from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching and implements
        LFU caching mechanism.
    """
    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.usage_count = {}  # Tracks how often each key is used
        self.lru_order = {}    # Tracks the order of keys for LRU tie-breaking
        self.time = 0          # Simulates time to track LRU

    def put(self, key, item):
        """ Add an item to the cache. Evict the least frequently used item if necessary. """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update existing item and its usage frequency
            self.cache_data[key] = item
            self.usage_count[key] += 1
            self.time += 1
            self.lru_order[key] = self.time
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Eviction process: find the LFU and LRU key
                min_freq = min(self.usage_count.values())
                lfu_keys = [k for k in self.cache_data if self.usage_count[k] == min_freq]
                
                if len(lfu_keys) > 1:
                    # Tie-breaking with LRU
                    lru_key = min(lfu_keys, key=lambda k: self.lru_order[k])
                else:
                    lru_key = lfu_keys[0]

                # Remove the LFU item
                del self.cache_data[lru_key]
                del self.usage_count[lru_key]
                del self.lru_order[lru_key]
                print(f"DISCARD: {lru_key}")

            # Add new item to the cache
            self.cache_data[key] = item
            self.usage_count[key] = 1
            self.time += 1
            self.lru_order[key] = self.time

    def get(self, key):
        """ Get an item by key and update its usage frequency """
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency and LRU order
        self.usage_count[key] += 1
        self.time += 1
        self.lru_order[key] = self.time
        return self.cache_data[key]
