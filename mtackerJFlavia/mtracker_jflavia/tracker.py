import sys
import tracemalloc

def execute_and_get_memory_usage(function, n):
    tracemalloc.start()
    before = tracemalloc.get_traced_memory()
    data = function(i)
    after = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"According to tracemalloc: {after[1] - before[1]}")
    print(f"According to sys: {sys.getsizeof(data)}")
    return data 