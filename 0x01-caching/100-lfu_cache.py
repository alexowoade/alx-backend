#!/usr/bin/env python3
"""
LFU Cache Module
"""
from collections import defaultdict
from datetime import datetime
from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """
    LFU Cache Class
    """

    def __init__(self):
        """
        Initialize LFU Cache
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.last_used = {}

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.last_used[key] = datetime.now()
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            keys_with_min_freq = [k for k, v in self.frequency.items() if v == min_freq]
            if len(keys_with_min_freq) == 1:
                discarded_key = keys_with_min_freq[0]
            else:
                discarded_key = min(keys_with_min_freq, key=lambda k: self.last_used[k])
            del self.cache_data[discarded_key]
            del self.frequency[discarded_key]
            del self.last_used[discarded_key]
            print("DISCARD:", discarded_key)

        self.cache_data[key] = item
        self.frequency[key] = 1
        self.last_used[key] = datetime.now()

    def get(self, key):
        """
        Retrieve an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.last_used[key] = datetime.now()
        return self.cache_data[key]

