from lib.Math.CoordinateSystem import CoordinateSystem
from lib.RCEngine.BasicClasses.EntityList import EntityList
from lib.Math.Vector import Vector
from lib.Math.Point import Point
from math import pi
from lib.globals import *
from lib.RCEngine.BasicClasses.Entity import Entity
from lib.RCEngine.BasicClasses.Ray import Ray
from lib.Exceptions.EngineExceptions.EngineExceptions import GameObjectExceptions


class Game:
    def __init__(self, cs: CoordinateSystem, entities: EntityList):
        self.cs = cs
        self.entities = entities

    def run(self) -> None:
        pass

    def update(self) -> None:
        pass

    def exit(self) -> None:
        pass

    def get_entity_class(self):
        return Entity(self.cs)

    def get_ray_class(self):
        return Ray(self.cs, Point(3), Vector(3))

    class Object(Entity):
        def __init__(self, pos: Point, dir: Vector, cs: CoordinateSystem):
            super().__init__(cs)
            self.set_property('position', pos)
            self.set_property('direction', dir)

        def move(self, dir: Vector) -> None:
            self.set_property('position', self['position'] + dir)

        def planar_rotate(self, inds: (int, int), angle: float) -> None:
            if self['direction'].dim() != 2:
                raise GameObjectExceptions.WRONG_DIM(2)

            self['direction'].rotate(inds, angle)

        def rotate_3d(self, angles: (float, float, float)) -> None:
            if self.dir.dim() != 3:
                raise GameObjectExceptions.WRONG_DIM(3)

            self['direction'].teit_bryan_rotate(angles)

        def set_position(self, pos: Point) -> None:
            self.pos = pos

        def set_direction(self, dir: Vector) -> None:
            self.dir = dir.normalize()

    class Camera:
        def __init__(self, fov: float, draw_dist: float, vfov: float = None, look_at: Point = None):
            self.fov = round(fov * pi / 180, PRECISION)
            self.draw_dist = round(draw_dist, PRECISION)
            self.entity = Entity()


            if vfov is not None:
                self.vfov = round(2/3*fov, PRECISION)
            if look_at is not None:
                self.look_at = look_at