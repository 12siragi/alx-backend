#!/usr/bin/env python3
"""LIFO Cache module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching System"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Assign to the dictionary the item value for the key key"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key:
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")

        self.last_key = key

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        return self.cache_data.get(key, None)
