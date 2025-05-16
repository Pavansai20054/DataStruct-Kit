from typing import List, TypeVar, Any

T = TypeVar('T', int, float, str)  # Supported types for sorting

def bubble_sort(arr: List[T]) -> List[T]:
    """
    Sorts a list using bubble sort algorithm.
    Time Complexity: O(n²)
    
    Args:
        arr: List of comparable elements (int/float/str)
        
    Returns:
        Sorted list in ascending order
        
    Raises:
        TypeError: If elements are not comparable
        
    Example:
        >>> bubble_sort([3, 1, 2])
        [1, 2, 3]
    """
    if not all(isinstance(x, (int, float, str)) for x in arr):
        raise TypeError("All elements must be of the same comparable type")
        
    n = len(arr)
    result = arr.copy()
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
                swapped = True
        if not swapped:
            break
    return result

def _merge(left: List[T], right: List[T]) -> List[T]:
    """Merges two sorted lists into one sorted list."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr: List[T]) -> List[T]:
    """Implements merge sort with O(n log n) complexity."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return _merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def quick_sort(arr: List[T]) -> List[T]:
    """Implements quick sort with average O(n log n) complexity."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)