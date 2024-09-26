import functools
from memory_profiler import memory_usage
import requests

def memory_profiler_decorator(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        memory_usage_before = memory_usage(-1, interval=0.1, timeout=1)[0]
        result = f(*args, **kwargs)
        memory_usage_after = memory_usage(-1, interval=0.1, timeout=1)[0]
        memory_difference = memory_usage_after - memory_usage_before
        print(f"Memory used by {f.__name__}: {memory_difference:.4f} MiB")
        return result
    return wrapper

@memory_profiler_decorator
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content

fetch_url("http://google.com")
