from unittest import TestCase
from lib.Math.Point import Point
from lib.Math.Vector import Vector


class TestPoint(TestCase):
    def sum_point(self):
        p = Point(elements=[0, 0, 0])
        v = Vector(elements=[1, 0, 0])

        ans = Point(elements=[1, 0, 0])

        self.assertEqual(p+v, ans)

    def sub_point(self):
        p = Point(elements=[1, 0, 0])
        v = Vector(elements=[1, 0, 0])

        ans = Point(elements=[0, 0, 0])

        self.assertEqual(p - v, ans)
