"""
PyDataStruct - A Python package implementing essential data structures and algorithms.
"""

__version__ = "0.1.0"

from . import graphs
from . import trees
from .hashtables import HashTable
from .searching import binary_search, linear_search
from .sorting import bubble_sort, merge_sort, quick_sort

__all__ = [
    "graphs",
    "trees",
    "HashTable",
    "binary_search",
    "linear_search",
    "bubble_sort",
    "merge_sort",
    "quick_sort",
]