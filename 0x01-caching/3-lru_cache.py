#!/usr/bin/env python3
"""LRU caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Cache class definition

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
            self.stack.remove(key)
            return

        if len(self.cache_data) > self.MAX_ITEMS:
            del self.cache_data[self.stack[0]]
            print(f'DISCARD: {self.stack[0]}')
            del self.stack[0]

    def get(self, key):
        """get value at key

        Args:
            key (str): key

        Returns:
            str: value if successful else None
        """
        if key in self.cache_data.keys():
            self.stack.append(key)
            self.stack.remove(key)

        return self.cache_data.get(key)
