# Tests for sorting algorithms
import pytest
from DataStruct_Kit.sorting import bubble_sort, merge_sort, quick_sort
from DataStruct_Kit.utils import is_sorted


@pytest.mark.parametrize(
    "func", [bubble_sort, merge_sort, quick_sort], ids=["bubble", "merge", "quick"]
)
def test_sorting(func):
    """Tests sorting functions with various inputs."""
    assert func([]) == []
    assert func([1]) == [1]
    assert func([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    assert is_sorted(func([64, 34, 25, 12, 22, 11, 90]))