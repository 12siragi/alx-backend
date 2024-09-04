#!/usr/bin/env python3
"""MRU Cache module"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU Caching System"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assign to the dictionary the item value for the key key"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
