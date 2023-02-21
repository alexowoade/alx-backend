#!/usr/bin/env python3
"""MRU caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU Cache class definition

    Args:
        BaseCaching (obj): parent class
    """

    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """add item to storage

        Args:
            key (str): key
            item (str): corresponding value at key
        """
        if not key or not item:
            return

        updated = True if key in self.cache_data.keys() else False

        self.cache_data[key] = item

        self.stack.append(key)

        if updated:
            self.updated_key = key
            first_index_of_key = self.stack.index(key)
            del self.stack[first_index_of_key]
            return

        if len(self.cache_data) > self.MAX_ITEMS:
            del self.cache_data[self.stack[-2]]
            print(f'DISCARD: {self.stack[-2]}')
            del self.stack[-2]

    def get(self, key):
        """get value at key

        Args:
            key (str): key

        Returns:
            str: value if successful else None
        """
        if key not in self.cache_data.keys():
            return None

        self.stack.append(key)
        first_index_of_key = self.stack.index(key)
        del self.stack[first_index_of_key]

        return self.cache_data.get(key)
