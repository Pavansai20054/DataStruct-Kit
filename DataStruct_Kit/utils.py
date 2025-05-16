# Utility functions
def is_sorted(arr: list) -> bool:
    """Checks if a list is sorted in ascending order."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))