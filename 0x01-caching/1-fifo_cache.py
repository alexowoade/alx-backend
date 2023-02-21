#!/usr/bin/env python3
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """define class for FIFO caching

    Args:
        BaseCaching (class): parent class
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """store cache data

        Args:
            key (_type_): key
            item (_type_): value
        """
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            keys_list = list(self.cache_data.keys())
            del self.cache_data[keys_list[0]]
            print(f'DISCARD: {keys_list[0]}')

    def get(self, key):
        """get value associated with key

        Args:
            key (_type_): cache_data key

        Returns:
            _type_: None if unsuccessful else data at key
        """
        return self.cache_data.get(key)
