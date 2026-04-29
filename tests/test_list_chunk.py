import pytest
from philiprehberger_list_chunk import (
    chunk,
    chunk_by,
    flatten,
    interleave,
    partition,
    sliding_window,
)


def test_chunk_even():
    assert chunk([1, 2, 3, 4], size=2) == [[1, 2], [3, 4]]


def test_chunk_uneven():
    assert chunk([1, 2, 3, 4, 5], size=2) == [[1, 2], [3, 4], [5]]


def test_chunk_with_pad():
    assert chunk([1, 2, 3], size=2, pad=0) == [[1, 2], [3, 0]]


def test_chunk_size_larger_than_list():
    assert chunk([1, 2], size=5) == [[1, 2]]


def test_chunk_empty():
    assert chunk([], size=3) == []


def test_chunk_size_one():
    assert chunk([1, 2, 3], size=1) == [[1], [2], [3]]


def test_chunk_invalid_size():
    with pytest.raises(ValueError):
        chunk([1, 2], size=0)


def test_chunk_by():
    result = chunk_by([1, 1, 2, 2, 3], key=lambda x: x)
    assert result == [[1, 1], [2, 2], [3]]


def test_chunk_by_custom_key():
    result = chunk_by(["aa", "ab", "ba", "bb"], key=lambda x: x[0])
    assert result == [["aa", "ab"], ["ba", "bb"]]


def test_sliding_window():
    result = sliding_window([1, 2, 3, 4, 5], size=3)
    assert result == [[1, 2, 3], [2, 3, 4], [3, 4, 5]]


def test_sliding_window_with_step():
    result = sliding_window([1, 2, 3, 4, 5], size=2, step=2)
    assert result == [[1, 2], [3, 4]]


def test_sliding_window_larger_than_list():
    assert sliding_window([1, 2], size=5) == []


def test_interleave():
    result = interleave([1, 2, 3], ["a", "b", "c"])
    assert result == [1, "a", 2, "b", 3, "c"]


def test_interleave_uneven():
    result = interleave([1, 2], ["a", "b", "c"])
    assert result == [1, "a", 2, "b"]


def test_flatten():
    result = flatten([[1, 2], [3, 4], [5]])
    assert result == [1, 2, 3, 4, 5]


def test_flatten_empty():
    assert flatten([]) == []


def test_partition_mixed():
    truthy, falsy = partition(range(6), lambda n: n % 2 == 0)
    assert truthy == [0, 2, 4]
    assert falsy == [1, 3, 5]


def test_partition_all_true():
    truthy, falsy = partition([1, 2, 3], lambda _: True)
    assert truthy == [1, 2, 3]
    assert falsy == []


def test_partition_all_false():
    truthy, falsy = partition([1, 2, 3], lambda _: False)
    assert truthy == []
    assert falsy == [1, 2, 3]


def test_partition_empty():
    truthy, falsy = partition([], lambda _: True)
    assert truthy == []
    assert falsy == []


def test_partition_preserves_order():
    truthy, falsy = partition(["b", "A", "c", "D"], str.isupper)
    assert truthy == ["A", "D"]
    assert falsy == ["b", "c"]
