import pytest
from mtracker_jflavia import IosifeFlavia, execute_and_get_memory_usage


def test_josephus_small():
    arr = list(range(1, 14))
    result = IosifeFlavia(arr.copy(), 13, 3)
    assert result == 13


def test_josephus_k2():
    arr = list(range(1, 101))
    result = IosifeFlavia(arr.copy(), 100, 2)
    assert result == 73


def test_josephus_single():
    arr = [1]
    result = IosifeFlavia(arr.copy(), 1, 5)
    assert result == 1


def test_memory_wrapper_returns_value():
    def dummy(n):
        return n * 2

    result = execute_and_get_memory_usage(dummy, 10)
    assert result == 20


def test_memory_wrapper_with_josephus():
    def wrapped(n):
        return IosifeFlavia(list(range(1, n + 1)), n, 2)

    result = execute_and_get_memory_usage(wrapped, 100)
    assert result == 73