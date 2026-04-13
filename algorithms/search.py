"""Search-related algorithms."""


def binary_search(arr: list[int], value: int) -> bool:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return True
        if arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return False
