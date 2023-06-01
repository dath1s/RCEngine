from unittest import TestCase
from lib.RCEngine.BasicClasses.EntityList import EntityList
from lib.RCEngine.BasicClasses.Entity import Entity
from lib.Math.Point import Point
from lib.Math.Vector import Vector
from lib.Math.VectorSpace import VectorSpace
from lib.Math.CoordinateSystem import CoordinateSystem


class TestEntityList(TestCase):
    def test_append(self):
        v1 = Vector(elements=[1, 0, 0])
        v2 = Vector(elements=[0, 1, 0])
        v3 = Vector(elements=[0, 0, 1])
        vs = VectorSpace([v1, v2, v3])
        point = Point(3)

        cs = CoordinateSystem(point, vs)

        entity1 = Entity(cs)
        entity2 = Entity(cs)
        entity_list = EntityList([entity1, entity2])

        entity3 = Entity(cs)
        entity_list.append(entity3)
        self.assertEqual(len(entity_list.entities), 3)

    def test_remove(self):
        v1 = Vector(elements=[1, 0, 0])
        v2 = Vector(elements=[0, 1, 0])
        v3 = Vector(elements=[0, 0, 1])
        vs = VectorSpace([v1, v2, v3])
        point = Point(3)

        cs = CoordinateSystem(point, vs)

        entity1 = Entity(cs)
        entity2 = Entity(cs)
        entity_list = EntityList([entity1, entity2])

        entity_list.remove(entity1)

        self.assertEqual(entity1 in entity_list.entities, False)

    def test_get(self):
        v1 = Vector(elements=[1, 0, 0])
        v2 = Vector(elements=[0, 1, 0])
        v3 = Vector(elements=[0, 0, 1])
        vs = VectorSpace([v1, v2, v3])
        point = Point(3)

        cs = CoordinateSystem(point, vs)

        entity1 = Entity(cs)
        entity2 = Entity(cs)
        entity_list = EntityList([entity1, entity2])

        entity1_id = entity1.identifier

        self.assertEqual(entity_list.get(entity1_id), entity1)

    def test_exec(self):
        v1 = Vector(elements=[1, 0, 0])
        v2 = Vector(elements=[0, 1, 0])
        v3 = Vector(elements=[0, 0, 1])
        vs = VectorSpace([v1, v2, v3])
        point = Point(3)

        cs = CoordinateSystem(point, vs)

        entity1 = Entity(cs)
        entity2 = Entity(cs)
        entity_list = EntityList([entity1, entity2])

        entity_list.exec(Entity.set_property, 'key', 1)
        self.assertEqual(all([entity['key'] == 1 for entity in entity_list.entities]), True)
