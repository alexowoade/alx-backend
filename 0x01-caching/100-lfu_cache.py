#!/usr/bin/env python3
"""LFU caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """define LFUCache class

    Args:
        BaseCaching (obj): parent cache class
    """

    def __init__(self):
        super().__init__()
        self.frequency_tracker = OrderedDict()
        self.lru_stack = []
        self.max_frequency = 0

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if not key or not item:
            return

        updated = True if key in self.cache_data.keys() else False

        self.cache_data[key] = item
        self.frequency_tracker[key] = self.frequency_tracker.get(key, 0) + 1

        if self.frequency_tracker[key] > self.max_frequency:
            self.max_frequency = self.frequency_tracker[key]

        if not updated:
            self.lru_stack.append(key)
        else:
            if self.frequency_tracker[key] == self.max_frequency:
                self.lru_stack.remove(key)

            print(self.frequency_tracker, '   ', self.lru_stack)
            if not self.lru_stack:
                self.lru_stack = list(self.frequency_tracker.keys())
            return

        if len(self.cache_data) > self.MAX_ITEMS:
            if self.lru_stack:
                del self.cache_data[self.lru_stack[0]]
                print(f'DISCARD: {self.lru_stack[0]}')
                del self.frequency_tracker[self.lru_stack[0]]
                del self.lru_stack[0]

                print(self.frequency_tracker, '   ', self.lru_stack)
                return

            print('\n\n')
            first_key = next(iter(self.frequency_tracker.keys()))
            del self.cache_data[first_key]
            print(f'DISCARD: {first_key}')
            del self.frequency_tracker[first_key]

            print(self.frequency_tracker, '   ', self.lru_stack)

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key not in self.cache_data.keys():
            return None

        self.frequency_tracker[key] = self.frequency_tracker.get(key, 0) + 1

        if self.frequency_tracker[key] > self.max_frequency:
            self.max_frequency = self.frequency_tracker[key]

        if key in self.lru_stack:
            self.lru_stack.remove(key)
            if self.frequency_tracker[key] < self.max_frequency:
                self.lru_stack.append(key)

        print(self.frequency_tracker, '   ', self.lru_stack)

        if not self.lru_stack:
            self.lru_stack = list(self.frequency_tracker.keys())
        return self.cache_data.get(key)


# lru = min(self.cache_monitor, key=self.cache_monitor.get)
