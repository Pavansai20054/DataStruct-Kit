from typing import List, Optional, TypeVar, Any

T = TypeVar('T', int, float, str)  # Supported types for searching

def linear_search(arr: List[T], target: T) -> int:
    """
    Performs linear search on a list.
    
    Args:
        arr: List to search through
        target: Value to find
        
    Returns:
        Index of target if found, otherwise -1
        
    Example:
        >>> linear_search([1, 3, 5], 3)
        1
        >>> linear_search([1, 3, 5], 2)
        -1
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1  # Explicitly return -1 for not found

def binary_search(arr: List[T], target: T) -> int:
    """
    Performs binary search on a sorted list.
    
    Args:
        arr: Sorted list (ascending order)
        target: Value to find
        
    Returns:
        Index of target if found, otherwise -1
        
    Raises:
        ValueError: If input list is not sorted
        
    Example:
        >>> binary_search([1, 3, 5], 3)
        1
        >>> binary_search([1, 3, 5], 2)
        -1
    """
    if not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        raise ValueError("Input list must be sorted in ascending order")
        
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Explicitly return -1 for not found