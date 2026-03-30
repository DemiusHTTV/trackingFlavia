import sys
import tracemalloc
from functools import wraps

def execute_and_get_memory_usage(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        before = tracemalloc.get_traced_memory()

        data = func(*args, **kwargs)

        after = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"According to tracemalloc: {after[1] - before[1]}")
        print(f"According to sys: {sys.getsizeof(data)}")

        return data

    return wrapper