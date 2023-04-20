#!/usr/bin/env python3

'''LRU Caching'''

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''You must use self.cache_data - dictionary
    from the parent class
    You can overload def __init__(self):
    but don’t forget to call the parent init: super().__init__()
    Least Recently Used Caching'''

    def __init__(self):
        '''Initializing class'''

        super().__init__()
        self.lru_order = OrderedDict()

    def put(self, key, item):
        '''Must assign to the dictionary self.cache_data
        the item value for the key key
        If key or item is None, this method should not do anything
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS:
        - you must discard the least recently used item (LRU algorithm)
        - you must print DISCARD: with the key discarded and
        following by a new line'''

        if key and item:
            self.lru_order[key] = item
            self.lru_order.move_to_end(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discarded = next(iter(self.lru_order))
            del self.cache_data[item_discarded]
            print("DISCARD:", item_discarded)

        if len(self.lru_order) > BaseCaching.MAX_ITEMS:
            self.lru_order.popitem(last=False)

    def get(self, key):
        '''Must return the value in self.cache_data linked to key
        '''
        if key in self.cache_data:
            self.lru_order.move_to_end(key)
            return self.cache_data[key]
        return None
