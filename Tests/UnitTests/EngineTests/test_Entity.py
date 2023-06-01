from unittest import TestCase
from lib.RCEngine.BasicClasses.Entity import Entity
from lib.Math.Point import Point
from lib.Math.Vector import Vector
from lib.Math.VectorSpace import VectorSpace
from lib.Math.CoordinateSystem import CoordinateSystem


class TestEntity(TestCase):
    def test_set_property(self):
        v1 = Vector(elements=[1, 0, 0])
        v2 = Vector(elements=[0, 1, 0])
        v3 = Vector(elements=[0, 0, 1])
        vs = VectorSpace([v1, v2, v3])
        point = Point(3)

        cs = CoordinateSystem(point, vs)

        entity = Entity(cs)
        entity.set_property("key", 123)
        self.assertEqual(entity.properties['key'], 123)

    def test_remove_property(self):
        v1 = Vector(elements=[1, 0, 0])
        v2 = Vector(elements=[0, 1, 0])
        v3 = Vector(elements=[0, 0, 1])
        vs = VectorSpace([v1, v2, v3])
        point = Point(3)

        cs = CoordinateSystem(point, vs)

        entity = Entity(cs)
        entity.set_property("key", 123)
        entity.remove_property('key')
        self.assertEqual('key' in entity.properties, False)

    def test_get_property(self):
        v1 = Vector(elements=[1, 0, 0])
        v2 = Vector(elements=[0, 1, 0])
        v3 = Vector(elements=[0, 0, 1])
        vs = VectorSpace([v1, v2, v3])
        point = Point(3)

        cs = CoordinateSystem(point, vs)

        entity = Entity(cs)
        entity.set_property("key", 123)
        self.assertEqual(entity.get_property('key'), 123)
