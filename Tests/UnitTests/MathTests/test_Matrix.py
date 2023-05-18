from unittest import TestCase
from lib.Math.Matrix import Matrix


class TestMatrix(TestCase):
    def test_get_minor(self):
        matrix = Matrix(elements=[[4, 5, 6, 1, 2],
                                  [0, 0, 2, 7, -5],
                                  [2, 2, 2, -3, 1],
                                  [1, 0, 1, 0, 1],
                                  [1, 2, 3, 4, 5]])

        minor = [[0, 7, -5], [0, 0, 1], [2, 4, 5]]

        self.assertEqual(matrix.get_minor([0, 2], [0, 2])[:], minor)

    def test_determinant(self):
        matrix = Matrix(elements=[[4, 5, 6, 1, 2],
                                  [0, 0, 2, 7, -5],
                                  [2, 2, 2, -3, 1],
                                  [1, 0, 1, 0, 1],
                                  [1, 2, 3, 4, 5]])

        self.assertEqual(matrix.determinant(), 60)

    def test_transpose(self):
        matrix = Matrix(elements=[[4, 5, 6, 1, 2],
                                  [0, 0, 2, 7, -5],
                                  [2, 2, 2, -3, 1],
                                  [1, 0, 1, 0, 1],
                                  [1, 2, 3, 4, 5]])

        transposed_matrix = Matrix(elements=[[4, 0, 2, 1, 1],
                                             [5, 0, 2, 0, 2],
                                             [6, 2, 2, 1, 3],
                                             [1, 7, -3, 0, 4],
                                             [2, -5, 1, 1, 5]])

        self.assertEqual(matrix.transpose()[:], transposed_matrix[:])

    def test_inverse(self):
        matrix = Matrix(elements=[
            [1, 3, -2],
            [2, 5, 1],
            [1, 2, -5]
        ])
        ans_inverse_matrix = [[-3.375, 1.375, 1.625],
                              [1.375, -0.375, -0.625],
                              [-0.125, 0.125, -0.125]]

        self.assertEqual((~matrix)[:], ans_inverse_matrix)

    def test_identity(self):
        ident_matrix = Matrix().identity(3)
        ident_matrix_ans = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

        self.assertEqual(ident_matrix[:], ident_matrix_ans)

    def test_euclid_norm(self):
        matrix = Matrix(elements=[
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]
        ])

        self.assertEqual((-0.03 < matrix.euclid_norm() - 6.48 < 0.03), True)

    def test_norm(self):
        a = Matrix(elements=[[100, -101, 25, 6],
                             [-25, 6, 6, 11],
                             [19, -18, 0, 0],
                             [1, 1, 11, 5]])

        self.assertEqual(a.norm(), 156)

    def sum_matrix(self):
        a = Matrix(elements=[[1, 2, 3, 4],
                             [6, 6, 6, 6],
                             [0, -5, 4, 4],
                             [0, 1, 0, 1]])
        b = Matrix(elements=[[5, 5, 5, 5],
                             [-6, -1, 2, -3],
                             [1, 1, 0, 2],
                             [4, -3, -3, -3]])

        ans = Matrix(elements=[[6, 7, 8, 9],
                               [0, 5, 8, 3],
                               [1, -4, 4, 6],
                               [4, -2, -3, -2]])

        self.assertEqual((a + b)[:], ans[:])

    def sub_matrix(self):
        a = Matrix(elements=[[1, 2, 3, 4],
                             [6, 6, 6, 6],
                             [0, -5, 4, 4],
                             [0, 1, 0, 1]])
        b = Matrix(elements=[[5, 5, 5, 5],
                             [-6, -1, 2, -3],
                             [1, 1, 0, 2],
                             [4, -3, -3, -3]])
        ans = Matrix(elements=[[-4, -3, -2, -1],
                               [12, 7, 4, 9],
                               [-1, -6, 4, 2],
                               [-4, 4, 3, 4]])

        self.assertEqual((a - b)[:], ans[:])

    def mul_matrix_by_number(self):
        a = Matrix(elements=[[2, 2, 0],
                             [3, 4, 2],
                             [2, 2, 2]])
        ans = Matrix(elements=[[1.0, 1.0, 0.0],
                               [1.5, 2.0, 1.0],
                               [1.0, 1.0, 1.0]])
        self.assertEqual((a * 0.5)[:], ans[:])

    def mul_matrix_by_matrix(self):
        a = Matrix(elements=[[2, 2, 0],
                             [3, 4, 2],
                             [2, 2, 2]])
        b = Matrix(elements=[[1, 0, 0],
                             [0, 0, 1],
                             [2, 2, 2]])
        ans = Matrix(elements=[[2, 0, 2],
                               [7, 4, 8],
                               [6, 4, 6]])

        self.assertEqual((a * b)[:], ans[:])

    def div_matrix_by_number(self):
        a = Matrix(elements=[[2, 2, 0],
                             [3, 4, 2],
                             [2, 2, 2]])
        ans = Matrix(elements=[[1.0, 1.0, 0.0],
                               [1.5, 2.0, 1.0],
                               [1.0, 1.0, 1.0]])
        self.assertEqual((a / 2)[:], ans[:])

    def div_matrix_by_matrix(self):
        a = Matrix(elements=[[2, 2, 0],
                             [3, 4, 2],
                             [2, 2, 2]])
        b = Matrix(elements=[[1, 0, 0],
                             [0, 0, 1],
                             [2, 2, 2]])
        ans = Matrix(elements=[[0.0, -2.0, 1.0],
                               [-1.0, -2.0, 2.0],
                               [0.0, 0.0, 1.0]])
        self.assertEqual((a / b)[:], ans[:])

    def rotate(self):
        m = Matrix(elements=[[1, 2],
                             [3, 4]])
        ans = Matrix(elements=[[-2, 1],
                               [-4, 3]])

        self.assertEqual(m, ans)
