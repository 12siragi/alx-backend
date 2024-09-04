#!/usr/bin/env python3
"""
BasicCache module
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that inherits from BaseCaching.
    This caching system doesn't have a limit on the number of items it stores.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key under which the item should be stored.
            item: The item to be stored in the cache.

        If key or item is None, this method should not do anything.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key corresponding to the item to retrieve.

        Returns:
            The value in self.cache_data linked to the key, or None if
            the key is None or doesn't exist in the cache.
        """
        return self.cache_data.get(key, None)
