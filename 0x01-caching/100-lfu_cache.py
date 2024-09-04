from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching and implements
        LFU caching mechanism.
    """
    def __init__(self):
        """ Initialize class instance. """
        super().__init__()
        self.usage_count = {}  # Track the frequency of usage for each key
        self.lru_order = []    # Track the order for LRU in case of tie

    def put(self, key, item):
        """ Add an item in the cache.
            If the cache is full, remove the least frequently used item.
        """
        if key is None or item is None:
            return

        # If the key already exists, just update the value and frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_count[key] += 1
            self.lru_order.remove(key)
            self.lru_order.append(key)
        else:
            # Check if the cache is full
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used key(s)
                min_freq = min(self.usage_count.values())
                min_freq_keys = [k for k, v in self.usage_count.items() if v == min_freq]

                # If there is a tie, use LRU to remove the oldest
                if len(min_freq_keys) > 1:
                    lru_key = next(k for k in self.lru_order if k in min_freq_keys)
                else:
                    lru_key = min_freq_keys[0]

                # Remove the least frequently used item
                del self.cache_data[lru_key]
                del self.usage_count[lru_key]
                self.lru_order.remove(lru_key)
                print(f"DISCARD: {lru_key}")

            # Add the new item
            self.cache_data[key] = item
            self.usage_count[key] = 1
            self.lru_order.append(key)

    def get(self, key):
        """ Get an item by key. """
        if key is None or key not in self.cache_data:
            return None
        # Update the usage count and move the key to the end of the LRU order
        self.usage_count[key] += 1
        self.lru_order.remove(key)
        self.lru_order.append(key)
        return self.cache_data[key]
