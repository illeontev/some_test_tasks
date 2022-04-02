import unittest
import task1


class Task1Test(unittest.TestCase):

    def test_closest_zero_distance(self):
        # Test 1
        res = task1.closest_zero_distance(
            8,
            [2, 3, 0, 7, 9, 4, 8, 2]
        )
        self.assertEqual(res, [2, 1, 0, 1, 2, 3, 4, 5])

        # Test 2
        res = task1.closest_zero_distance(
            6,
            [0, 7, 9, 4, 8, 0]
        )
        self.assertEqual(res, [0, 1, 2, 2, 1, 0])

        # Test 3
        res = task1.closest_zero_distance(
            14,
            [0, 7, 9, 4, 8, 20, 0, 1, 2, 3, 0, 0, 0, 12]
        )
        self.assertEqual(res, [0, 1, 2, 3, 2, 1, 0, 1, 2, 1, 0, 0, 0, 1])


if __name__ == '__main__':
    unittest.main()
