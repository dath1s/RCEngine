from lib.Math.CoordinateSystem import CoordinateSystem
from lib.RCEngine.BasicClasses.EntityList import EntityList
from lib.Math.Vector import Vector
from lib.Math.Point import Point
from math import pi
from config.globals import *
from lib.RCEngine.BasicClasses.Entity import Entity
from lib.RCEngine.BasicClasses.Ray import Ray
from lib.Exceptions.EngineExceptions.EngineExceptions import GameObjectExceptions
from lib.Math.Matrix import Matrix


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
            self['position'] = pos

        def set_direction(self, dir: Vector) -> None:
            self['direction'] = dir.normalize()

        def intersection_distance(self, ray: Ray) -> float:
            return 0

    class Camera(Object):
        def __init__(self, fov: float, draw_dist: float, vfov: float = None, look_at: Point = None):
            self.set_property('fov', round(fov * pi / 180, PRECISION))
            self.set_property('draw_dist', round(draw_dist, PRECISION))
            self.entity = Entity(self.cs)

            if vfov is not None:
                self.set_property('vfov', round(2 / 3 * fov, PRECISION))
            if look_at is not None:
                self.set_property('look_at', look_at)

        def get_rays_matrix(self, n: int, m: int):
            delta_alpha = round(self['fov'] / n, PRECISION)
            delta_beta = round(self['vfov'] / m, PRECISION)
            zero_angle_x = round(self['fov'] / 2, PRECISION)
            zero_angle_y = round(self['vfov'] / 2, PRECISION)

            if self['direction'] is None:
                direction = Vector(elements=[self['look_at'][i] - self['position'][i] for i in len(self['position'])])
            else:
                direction = self['direction']

            ray_matrix = Matrix(n, m)
            for i in range(n):
                cur_angle_x = delta_alpha * i - zero_angle_x
                for j in range(m):
                    cur_angle_y = delta_beta * j - zero_angle_y
                    proection_dir = direction.rotate([1, 2], cur_angle_x).rotate([0, 2], cur_angle_y)
                    proection_dir *= (direction.length() ** 2) / direction.scalar_product(proection_dir)
                    ray_matrix[i][j] = Ray(self.cs, self['position'], proection_dir)

            return ray_matrix

    class HyperPlane(Object):
        def __init__(self, pos: Point, normal: Vector) -> None:
            self.set_property('position', pos)
            self.set_property('normal', normal)
            self['direction'] = self['direction'].normalize()

        def planar_rotate(self, inds: (int, int), angle: float) -> None:
            self['normal'].rotate(inds, angle)

        def rotate_3d(self, angles: (float, float, float)) -> None:
            self['normal'].teit_bryan_rotate(angles)

        def intersection_distance(self, ray: Ray) -> float:
            pass

    class HyperEllipsoid(Object):
        def __init__(self, pos: Point, dir: Vector, semiaxes: list[float]) -> None:
            pass

        def planar_rotate(self, inds: (int, int), angle: float) -> None:
            pass

        def rotate_3d(self, angles: (float, float, float)) -> None:
            pass

        def intersection_distance(self, ray: Ray) -> float:
            pass

    class Canvas:
        def __init__(self, n: int, m: int) -> None:
            self.n = n
            self.m = m
            self.distances = Game.Camera.get_rays_matrix(n, m)

        def draw(self) -> None:
            pass

        def update(self, camera):
            pass