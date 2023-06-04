from unittest import TestCase
from lib.RCEngine.BasicClasses.Game import Game, Vector, Point, CoordinateSystem, EntityList, Entity
from lib.Math.VectorSpace import VectorSpace


class TestGame(TestCase):
    def test_get_entity_class(self):
        v1 = Vector(elements=[1, 0, 0])
        v2 = Vector(elements=[0, 1, 0])
        v3 = Vector(elements=[0, 0, 1])
        vs = VectorSpace([v1, v2, v3])
        point = Point(3)

        cs = CoordinateSystem(point, vs)

        entity1 = Entity(cs)
        entity2 = Entity(cs)
        entity_list = EntityList([entity1, entity2])
        game = Game(cs, entity_list)
        entity = game.get_entity_class()
        self.assertEqual(all([entity().cs.space.basis[i] == cs.space.basis[i] for i in range(len(cs.space.basis))]),
                         True)

    def test_get_ray_class(self):
        v1 = Vector(elements=[1, 0, 0])
        v2 = Vector(elements=[0, 1, 0])
        v3 = Vector(elements=[0, 0, 1])
        vs = VectorSpace([v1, v2, v3])
        point = Point(3)

        cs = CoordinateSystem(point, vs)

        entity1 = Entity(cs)
        entity2 = Entity(cs)
        entity_list = EntityList([entity1, entity2])
        game = Game(cs, entity_list)
        ray = game.get_ray_class()
        self.assertEqual(
            all([ray(Point(3), Vector(3)).cs.space.basis[i] == cs.space.basis[i] for i in range(len(cs.space.basis))]),
            True)

    def test_object(self):
        v1 = Vector(elements=[1, 0, 0])
        v2 = Vector(elements=[0, 1, 0])
        v3 = Vector(elements=[0, 0, 1])
        vs = VectorSpace([v1, v2, v3])
        point = Point(3)

        cs = CoordinateSystem(point, vs)

        entity1 = Entity(cs)
        entity2 = Entity(cs)
        entity_list = EntityList([entity1, entity2])
        game = Game(cs, entity_list)

        def test_move():
            obj = game.Object()(Point(2), Vector(2))
            obj.move(Vector(elements=[1, 1]))
            self.assertEqual(obj.get_property('position'), Vector(elements=[1, 1]))

        def test_planar_rotate():
            obj = game.Object()(Point(3), Vector(elements=[1, 2, 3]))
            obj.planar_rotate([0, 1], 90)
            self.assertEqual(obj['direction'], Vector(elements=[-2.0, 1.0, 3]))

        def test_set_position():
            obj = game.Object()(Point(2), Vector(2))
            obj.set_position(Point(elements=[1, 1, 1]))
            self.assertEqual(obj['position'], Point(elements=[1, 1, 1]))

        def test_set_direction():
            obj = game.Object()(Point(2), Vector(2))
            obj.set_direction(Vector(elements=[3, 0, 0]))
            self.assertEqual(obj['direction'], Vector(elements=[1, 0, 0]))

        test_move()
        test_planar_rotate()
        test_set_direction()
        test_set_position()

    def test_hyper_plane(self):
        v1 = Vector(elements=[1, 0, 0])
        v2 = Vector(elements=[0, 1, 0])
        v3 = Vector(elements=[0, 0, 1])
        vs = VectorSpace([v1, v2, v3])
        point = Point(3)

        cs = CoordinateSystem(point, vs)

        entity1 = Entity(cs)
        entity2 = Entity(cs)
        entity_list = EntityList([entity1, entity2])
        game = Game(cs, entity_list)

    def test_hyper_ellipsoid(self):
        v1 = Vector(elements=[1, 0, 0])
        v2 = Vector(elements=[0, 1, 0])
        v3 = Vector(elements=[0, 0, 1])
        vs = VectorSpace([v1, v2, v3])
        point = Point(3)

        cs = CoordinateSystem(point, vs)

        entity1 = Entity(cs)
        entity2 = Entity(cs)
        entity_list = EntityList([entity1, entity2])
        game = Game(cs, entity_list)

    def test_canvas(self):
        v1 = Vector(elements=[1, 0, 0])
        v2 = Vector(elements=[0, 1, 0])
        v3 = Vector(elements=[0, 0, 1])
        vs = VectorSpace([v1, v2, v3])
        point = Point(3)

        cs = CoordinateSystem(point, vs)

        entity1 = Entity(cs)
        entity2 = Entity(cs)
        entity_list = EntityList([entity1, entity2])
        game = Game(cs, entity_list)
