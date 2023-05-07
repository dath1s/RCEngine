from unittest import TestCase
from lib.RCEngine.BasicClasses.Vector import Vector
from lib.RCEngine.BasicClasses.Matrix import Matrix


class TestVector(TestCase):
    def test_scalar_product(self):
        v1 = Vector(elements=[1, 2, 3])
        v2 = Vector(elements=[1, 2, 3])

        self.assertEqual(v1.scalar_product(v2), 14)

    def test_vector_product(self):
        v1 = Vector(elements=[1, 2, 3])
        v2 = Vector(elements=[1, 2, 4])

        ans = Matrix(elements=[[2, -1, 0]])

        self.assertEqual(v1.vector_product(v2), ans)

    def test_length(self):
        a = Vector(elements=[3, 0, 4])
        self.assertEqual(a.length(), 5)

    def test_normalize(self):
        a = Vector(elements=[3, 0, 4])
        ans = Vector(elements=[0.6, 0, 0.8])

        self.assertEqual(a, ans)

    def test_dim(self):
        a = Vector(elements=[3, 0, 4])
        self.assertEqual(a.dim(), 3)

    def test_transpose(self):
        a = Vector(elements=[3, 0, 4])
        a_tr = Vector(elements=[[3], [0], [4]])

        self.assertEqual(a.transpose()[:], a_tr[:])

    def sum_vector(self):
        a = Vector(elements=[1, 2, 3])
        b = Vector(elements=[1, 2, 3])

        ans = Vector(elements=[2, 4, 6])

        self.assertEqual((a+b)[:], ans[:])

    def sub_vector(self):
        a = Vector(elements=[1, 2, 3])
        b = Vector(elements=[1, 2, 3])

        ans = Vector(elements=[0, 0, 0])

        self.assertEqual((a - b)[:], ans[:])

    def mul_vec2vec(self):
        a = Vector(elements=[3, 0, 4])
        b = Vector(elements=[[3], [0], [4]])

        ans = Matrix(elements=[[25]])

        self.assertEqual((a*b), ans)

    def mul_vec2num(self):
        b = Vector(elements=[1, 2, 3])
        ans = Vector(elements=[2, 4, 6])

        self.assertEqual((b*2)[:], ans[:])

    def div_vec(self):
        a = Vector(elements=[2, 4, 6])
        ans = Vector(elements=[1, 2, 3])

        self.assertEqual((a/2)[:], ans[:])

    def rotate(self):
        a = Vector(elements=[1, 2, 3])
        ans = Vector(elements=[-2.0, 1.0, 3])

        self.assertEqual(a, ans)
