#!/usr/bin/env python3
"""Python Caching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """define basic cache class

    Args:
        BaseCaching (class): Parent cache class
    """

    def put(self, key, item):
        """add data to cache_data

        Args:
            key (_type_): cache_data key
            item (_type_): corresponding value to key
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get value associated with key

        Args:
            key (_type_): cache_data key

        Returns:
            _type_: None if unsuccessful else data at key
        """
        return self.cache_data.get(key)
