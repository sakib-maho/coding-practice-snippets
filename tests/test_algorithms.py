import unittest

from algorithms import binary_search, is_valid_brackets, jewel_count, two_sum


class AlgorithmTests(unittest.TestCase):
    def test_two_sum(self) -> None:
        self.assertEqual(two_sum([3, 2, 4], 6), (1, 2))

    def test_binary_search(self) -> None:
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 4))
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 9))

    def test_brackets(self) -> None:
        self.assertTrue(is_valid_brackets("{[()]}"))
        self.assertFalse(is_valid_brackets("{[(])}"))

    def test_jewel_count(self) -> None:
        self.assertEqual(jewel_count("aA", "aAAbbbb"), 3)


if __name__ == "__main__":
    unittest.main()
