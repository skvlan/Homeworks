import functools
import requests
from collections import OrderedDict


def lfu_cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                # переносимо в кінець списку
                deco._cache.move_to_end(cache_key, last=True)
                deco._use_count[cache_key] += 1
                return deco._cache[cache_key]
            result = f(*args, **kwargs)
            if len(deco._cache) >= max_limit:
                least_used_key = min(deco._use_count, key=deco._use_count.get)
                deco._cache.pop(least_used_key)
                deco._use_count.pop(least_used_key)
            deco._cache[cache_key] = result
            deco._use_count[cache_key] = 1
            return result
        deco._cache = {}
        deco._use_count = OrderedDict()
        return deco
    return internal


@lfu_cache(max_limit=64)
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content

fetch_url("http://google.com")
