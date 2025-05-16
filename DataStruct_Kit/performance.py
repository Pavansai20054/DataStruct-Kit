import timeit
from typing import Callable, Any, Dict
from functools import partial

def measure_time(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Dict[str, float]:
    """
    Measures execution time with statistics.
    
    Returns:
        Dictionary with min/max/avg times in microseconds
    """
    timer = timeit.Timer(partial(func, *args, **kwargs))
    times = timer.repeat(repeat=5, number=1000)
    return {
        'min': min(times) * 1e6,
        'max': max(times) * 1e6,
        'avg': sum(times) / len(times) * 1e6
    }

def benchmark_algorithms():
    """Example benchmark comparing sort algorithms."""
    from DataStruct_Kit import bubble_sort, quick_sort
    test_data = [3, 1, 4, 1, 5, 9, 2, 6]
    
    print("Bubble Sort:", measure_time(bubble_sort, test_data.copy()))
    print("Quick Sort:", measure_time(quick_sort, test_data.copy()))