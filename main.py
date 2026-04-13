"""Demo runner for algorithm toolkit."""

from algorithms import binary_search, is_valid_brackets, jewel_count, two_sum


if __name__ == "__main__":
    print("two_sum:", two_sum([3, 2, 4], 6))
    print("binary_search:", binary_search([1, 2, 3, 4, 5], 4))
    print("is_valid_brackets:", is_valid_brackets("{[()]}"))
    print("jewel_count:", jewel_count("aA", "aAAbbbb"))
