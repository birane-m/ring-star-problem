import unittest

from ring_star.distances import build_distance_matrix, euclidean_distance


class DistanceTests(unittest.TestCase):
    def test_euclidean_distance(self):
        self.assertEqual(euclidean_distance((0, 0), (3, 4)), 5.0)

    def test_distance_matrix_is_symmetric_with_zero_diagonal(self):
        matrix = build_distance_matrix(((0, 0), (3, 4), (6, 0)))

        self.assertEqual(matrix[0][0], 0.0)
        self.assertEqual(matrix[1][1], 0.0)
        self.assertEqual(matrix[2][2], 0.0)
        self.assertEqual(matrix[0][1], matrix[1][0])
        self.assertEqual(matrix[0][2], matrix[2][0])
        self.assertEqual(matrix[1][2], matrix[2][1])


if __name__ == "__main__":
    unittest.main()
