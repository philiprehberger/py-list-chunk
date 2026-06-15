"""Split iterables into evenly sized chunks."""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from itertools import islice
from typing import Any, Callable, TypeVar


__all__ = [
    "chunk",
    "chunk_by",
    "sliding_window",
    "interleave",
    "flatten",
    "partition",
    "transpose",
    "pairwise",
]

T = TypeVar("T")


def chunk(items: Iterable[T], size: int, *, pad: T | None = None) -> list[list[T]]:
    """Split an iterable into fixed-size chunks.

    Args:
        items: The iterable to split.
        size: Maximum items per chunk.
        pad: If provided, pad the last chunk to *size* with this value.

    Returns:
        List of chunks (lists).
    """
    if size < 1:
        msg = "Chunk size must be at least 1"
        raise ValueError(msg)

    result: list[list[T]] = []
    it = iter(items)

    while True:
        batch = list(islice(it, size))
        if not batch:
            break
        if pad is not None and len(batch) < size:
            batch.extend([pad] * (size - len(batch)))
        result.append(batch)

    return result


def chunk_by(items: Iterable[T], key: Callable[[T], Any]) -> list[list[T]]:
    """Group consecutive elements by a key function.

    Args:
        items: The iterable to group.
        key: Function returning a grouping key for each item.

    Returns:
        List of groups where consecutive items share the same key.
    """
    result: list[list[T]] = []
    current_group: list[T] = []
    current_key: Any = object()

    for item in items:
        k = key(item)
        if k != current_key:
            if current_group:
                result.append(current_group)
            current_group = [item]
            current_key = k
        else:
            current_group.append(item)

    if current_group:
        result.append(current_group)

    return result


def sliding_window(items: list[T], size: int, *, step: int = 1) -> list[list[T]]:
    """Generate sliding window views over a list.

    Args:
        items: The list to window over.
        size: Window size.
        step: Step size between windows.

    Returns:
        List of windows (lists).
    """
    if size < 1:
        msg = "Window size must be at least 1"
        raise ValueError(msg)
    if step < 1:
        msg = "Step must be at least 1"
        raise ValueError(msg)

    return [items[i : i + size] for i in range(0, len(items) - size + 1, step)]


def interleave(*iterables: Iterable[T]) -> list[T]:
    """Round-robin interleave multiple iterables.

    Stops when the shortest iterable is exhausted.

    Args:
        *iterables: Iterables to interleave.

    Returns:
        Interleaved list.
    """
    iterators = [iter(it) for it in iterables]
    result: list[T] = []

    while True:
        exhausted = False
        for it in iterators:
            try:
                result.append(next(it))
            except StopIteration:
                exhausted = True
                break
        if exhausted:
            break

    return result


def flatten(nested: Iterable[Iterable[T]]) -> list[T]:
    """Flatten one level of nesting.

    Args:
        nested: Iterable of iterables.

    Returns:
        Flat list.
    """
    result: list[T] = []
    for item in nested:
        result.extend(item)
    return result


def transpose(matrix: Iterable[Iterable[T]]) -> list[list[T]]:
    """Transpose a 2D iterable (rows become columns).

    Jagged input is truncated to the shortest row, so the result has no holes.

    Args:
        matrix: Iterable of row iterables.

    Returns:
        Transposed list of lists. Empty input returns ``[]``.
    """
    rows = [list(row) for row in matrix]
    if not rows:
        return []
    width = min(len(r) for r in rows)
    return [[rows[i][j] for i in range(len(rows))] for j in range(width)]


def pairwise(items: Iterable[T]) -> list[tuple[T, T]]:
    """Return consecutive overlapping pairs from *items*.

    Mirrors :func:`itertools.pairwise` but materializes a list.

    Args:
        items: The iterable to pair.

    Returns:
        List of ``(a, b)`` tuples where each ``b`` follows ``a``. Returns
        ``[]`` when *items* has fewer than two elements.
    """
    it = iter(items)
    try:
        prev = next(it)
    except StopIteration:
        return []
    result: list[tuple[T, T]] = []
    for current in it:
        result.append((prev, current))
        prev = current
    return result


def partition(
    items: Iterable[T],
    predicate: Callable[[T], Any],
) -> tuple[list[T], list[T]]:
    """Split *items* into two lists based on *predicate* in a single pass.

    Args:
        items: The iterable to partition.
        predicate: A callable returning a truthy value for items that should
            land in the first list.

    Returns:
        ``(truthy, falsy)`` — items for which *predicate* returns truthy come
        first, the rest come second.  Original order is preserved within each
        list.
    """
    truthy: list[T] = []
    falsy: list[T] = []
    for item in items:
        if predicate(item):
            truthy.append(item)
        else:
            falsy.append(item)
    return truthy, falsy
