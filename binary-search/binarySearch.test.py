import unittest

from binarySearch import BinarySearch

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.func = BinarySearch()

    def test_searchBinary_long_list_should_return_correct_index_and_attempts(self):
        targetNumber = 11
        expectedIndexNumber = 5
        expectedAttemptsNumber = 1
        searchableList = [1, 3, 5, 7, 9, 11, 13, 14, 20, 30, 45, 66]
        resultAttempts, resultIndex = BinarySearch.calculateIndex(searchableList, targetNumber)

        self.assertEqual(resultIndex, expectedIndexNumber)
        self.assertEqual(resultAttempts, expectedAttemptsNumber)

    def test_searchBinary_short_list_should_return_correct_index_and_attempts(self):
        targetNumber = 3
        expectedIndexNumber = 2
        expectedAttemptsNumber = 2
        searchableList = [1, 2, 3, 4]
        resultAttempts, resultIndex = BinarySearch.calculateIndex(searchableList, targetNumber)

        self.assertEqual(resultIndex, expectedIndexNumber)
        self.assertEqual(resultAttempts, expectedAttemptsNumber)

if __name__ == '__main__':
    unittest.main()