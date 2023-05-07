from unittest import TestCase
from lib.RCEngine.BasicClasses.Point import Point
from lib.RCEngine.BasicClasses.Vector import Vector
from lib.RCEngine.BasicClasses.VectorSpace import VectorSpace


class TestVectorSpace(TestCase):
    def test_as_vector(self):
        v1 = Vector(elements=[1, 0, 0])
        v2 = Vector(elements=[0, 1, 0])
        v3 = Vector(elements=[0, 0, 1])
        vs = VectorSpace([v1, v2, v3])

        ans = Vector(elements=[1, 2, 3])

        self.assertEqual(vs.as_vector(Point(elements=[1, 2, 3])), ans)
