# Example of using searching algorithms
from DataStruct_Kit.searching import linear_search, binary_search

if __name__ == "__main__":
    arr = [11, 12, 22, 25, 34, 64, 90]
    print("Array:", arr)
    print("Linear Search (22):", linear_search(arr, 22))
    print("Binary Search (22):", binary_search(arr, 22))