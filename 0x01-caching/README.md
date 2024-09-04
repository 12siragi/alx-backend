# BasicCache Module

This project implements a basic caching system using Python. The `BasicCache` class inherits from the `BaseCaching` class and allows storing key-value pairs without any limit on the number of items.

## Features

- Add items to the cache using the `put()` method.
- Retrieve items from the cache using the `get()` method.
- The cache has no limit on the number of stored items.

## Usage

To use the `BasicCache` class:

```python
from 0-basic_cache import BasicCache

my_cache = BasicCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
print(my_cache.get("A"))  # Output: Hello

