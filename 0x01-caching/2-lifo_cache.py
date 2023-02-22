#!/usr/bin/env python3
"""LIFO caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """define LIFO Caching

    Args:
        BaseCaching (_type_): parent cache class
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """store cache data using LIFO algorithm

        Args:
            key (str): key
            item (str): value to store
        """
        if not key or not item:
            return

        updated = True if key in self.cache_data.keys() else False

        self.cache_data[key] = item

        if updated:
            self.updated_key = key
            return

        keys_list = list(self.cache_data.keys())

        if len(self.cache_data) > self.MAX_ITEMS:
            try:
                del self.cache_data[self.updated_key]
                print(f'DISCARD: {self.updated_key}')
            except Exception:
                del self.cache_data[keys_list[-2]]
                print(f'DISCARD: {keys_list[-2]}')

    def get(self, key):
        """get value associated with key

        Args:
            key (_type_): cache_data key

        Returns:
            _type_: None if unsuccessful else data at key
        """
        return self.cache_data.get(key)
