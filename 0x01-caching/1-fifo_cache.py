#!/usr/bin/env python3

'''FIFO Caching'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''You must use `self.cache_data` - dictionary
    from the parent class
    You can overload `def __init__(self):`
    but don’t forget to call the parent init: `super().__init__()`
    '''

    def __init__(self):
        '''Initializing the class'''

        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        '''Must assign to the dictionary `self.cache_data`
        the item value for the key key'''

        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_discarded = self.key_indexes.pop(0)
                del self.cache_data[item_discarded]
                print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        '''Must return the value in `self.cache_data`
        linked to key'''

        if key in self.cache_data:
            return self.cache_data[key]
        return None
