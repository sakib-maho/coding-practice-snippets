"""Two Sum implementation."""


def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    seen: dict[int, int] = {}
    for idx, value in enumerate(nums):
        wanted = target - value
        if wanted in seen:
            return seen[wanted], idx
        seen[value] = idx
    raise ValueError("no valid pair found")
