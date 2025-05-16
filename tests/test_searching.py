import pytest
from DataStruct_Kit.searching import linear_search, binary_search

def test_linear_search():
    """Tests linear search with various inputs."""
    # Test found cases
    assert linear_search([1, 3, 5, 7, 9], 5) == 2
    assert linear_search(['a', 'b', 'c'], 'b') == 1
    
    # Test not found cases
    assert linear_search([1, 3, 5, 7, 9], 10) == -1
    assert linear_search([], 5) == -1

def test_binary_search():
    """Tests binary search with various inputs."""
    # Test found cases
    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    assert binary_search(['a', 'b', 'c'], 'b') == 1
    
    # Test not found cases
    assert binary_search([1, 3, 5, 7, 9], 10) == -1
    assert binary_search([], 5) == -1
    
    # Test invalid input
    with pytest.raises(ValueError):
        binary_search([3, 1, 2], 1)  # Unsorted list