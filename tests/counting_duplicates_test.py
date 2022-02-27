import unittest

from src.counting_duplicates import duplicate_count


class CountingDuplicatesTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(duplicate_count(""), 0)
        self.assertEqual(duplicate_count("abcde"), 0)
        self.assertEqual(duplicate_count("abcdeaa"), 1)
        self.assertEqual(duplicate_count("abcdeaB"), 2)
        self.assertEqual(duplicate_count("Indivisibilities"), 2)


if __name__ == "__main__":
    unittest.main()
