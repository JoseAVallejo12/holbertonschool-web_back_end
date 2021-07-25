#!/usr/bin/python3
"""class FIFOCache that inherits from BaseCaching."""


from typing import Union
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Fifo class

    Args:
        BaseCaching (class): base cache class
    """
    def __init__(self):
        super().__init__()

    def put(self, key: str, item: str) -> None:
        """Add value en cache."""
        if key and item and self.isCacheUpgradeable(key):
            self.cache_data[key] = item

    def get(self, key: str) -> Union[None, object]:
        """Get value of cache"""
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]

    def isCacheUpgradeable(self, key: str) -> bool:
        """check if cache not is fill"""
        if len(self.cache_data.keys()) >= self.MAX_ITEMS:
            print(f'DISCARD: {key}')
            return False
        return True
