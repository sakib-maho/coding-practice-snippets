"""Backward-compatible wrapper for binary search demo."""

from algorithms.search import binary_search


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(arr, 11))
