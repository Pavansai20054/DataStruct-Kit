# Example of using sorting algorithms
from DataStruct_Kit.sorting import bubble_sort, merge_sort, quick_sort

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", arr)
    print("Bubble Sort:", bubble_sort(arr))
    print("Merge Sort:", merge_sort(arr))
    print("Quick Sort:", quick_sort(arr))