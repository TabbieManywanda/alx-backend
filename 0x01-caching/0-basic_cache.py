#!/usr/bin/python 3

'''Basic dictionary'''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''You must use `self.cache_data` - dictionary
    from the parent class
    This caching system doesn’t have limit'''

    def put(self, key, item):
        '''assigns to the dictionary `self.cache_data`
        the `item` value for the `key` key'''

        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''returns value in `self.cache_data`
        linked to key'''

        if key in self.cache_data:
            return self.cache_data[key]
        return None
