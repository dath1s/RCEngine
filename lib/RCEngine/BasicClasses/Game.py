from lib.Math.CoordinateSystem import CoordinateSystem
from lib.RCEngine.BasicClasses.EntityList import EntityList
from lib.Math.Vector import Vector
from lib.Math.Point import Point
from math import pi, atan, tan
from config.globals import *
from lib.RCEngine.BasicClasses.Entity import Entity
from lib.RCEngine.BasicClasses.Ray import Ray
from lib.Exceptions.EngineExceptions.EngineExceptions import GameObjectExceptions
from lib.Math.Matrix import Matrix
from math import sqrt
from lib.RCEngine.BasicClasses.EventSystem import EventSystem
import curses


class Game:
    def __init__(self, cs: CoordinateSystem, entities: EntityList, es: EventSystem = None):
        self.cs = cs
        self.entities = entities
        self.game_entity_class = self.get_entity_class()
        self.es = es

    def run(self) -> None:
        pass

    def update(self) -> None:
        pass

    def exit(self) -> None:
        pass

    def get_event_system(self):
        class GEventSystem(EventSystem):
            def __init__(other):
                super().__init__()

        return GEventSystem

    def apply_configuration(self, configuration):
        pass

    def get_entity_class(self):
        class GEntity(Entity):
            def __init__(other):
                super().__init__(self.cs)

        return GEntity

    def get_ray_class(self):
        class GRay(Ray):
            def __init__(other, initial_pt: Point, direction: Vector):
                super().__init__(self.cs, initial_pt, direction)

        return GRay

    def Object(self):
        class GObject(self.get_entity_class()):
            def __init__(self, pos: Point, dir: Vector):
                super().__init__()
                self.cs = self.cs
                self.set_property('position', pos)
                self.set_property('direction', dir)

            def move(self, dir: Vector) -> None:
                self.set_property('position', self['position'] + dir)

            def planar_rotate(self, inds: (int, int), angle: float) -> None:
                self.set_property('direction', self['direction'].rotate(inds, angle))

            def rotate_3d(self, angles: (float, float, float)) -> None:
                self.set_property('direction', self['direction'].teit_bryan_rotate(angles))

            def set_position(self, pos: Point) -> None:
                self.set_property('position', pos)

            def set_direction(self, dir: Vector) -> None:
                self.set_property('direction', dir.normalize())

            def intersection_distance(self, ray: Ray) -> float:
                return 0

        return GObject

    def Camera(self):
        class GCamera(self.Object()):
            def __init__(other, position: Point, fov: float, draw_dist: float, vfov: float = None,
                         look_at: Point = None):
                super().__init__(position, look_at)
                other.set_property('fov', round(fov * pi / 180, PRECISION))
                other.set_property('draw_dist', round(draw_dist, PRECISION))
                other.entity = Entity(other.cs)

                if vfov is None:
                    other.set_property('vfov', atan((SCREEN_SIZE[0] / SCREEN_SIZE[1]) * tan(other['fov'] / 2)))
                else:
                    other.set_property('vfov', round(vfov * pi / 180, PRECISION))

                if look_at is not None:
                    other.set_property('look_at', look_at)

            def get_rays_matrix(self, n: int, m: int):
                delta_alpha = round(self['fov'] / n, PRECISION)
                delta_beta = round(self['vfov'] / m, PRECISION)
                zero_angle_x = round(self['fov'] / 2, PRECISION)
                zero_angle_y = round(self['vfov'] / 2, PRECISION)

                if self['direction'] is None:
                    direction = Vector(
                        elements=[self['look_at'][i] - self['position'][i] for i in range(len(self['position']))])
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

        return GCamera

    def HyperPlane(self):
        class GHyperPlane(self.Object()):
            def __init__(other, pos: Point, normal: Vector) -> None:
                super().__init__(pos, normal)
                other.set_property('position', pos)
                other.set_property('normal', normal)
                other.set_property('direction', other['direction'].normalize())

            def planar_rotate(self, inds: (int, int), angle: float) -> None:
                self.set_property('normal', self['normal'].rotate(inds, angle))

            def rotate_3d(self, angles: (float, float, float)) -> None:
                self.set_property('normal', self['normal'].teit_bryan_rotate(angles))

            def intersection_distance(self, ray: Ray) -> float:
                ray_pt = ray.initial_pt
                ray_dir = ray.dir

                plane_pt = self.position
                plane_dir = self.direction

                if not (plane_dir % ray_dir):
                    if plane_dir % (ray_pt - plane_pt):
                        raise Exception
                    else:
                        return 0
                else:
                    temp = -(plane_dir % (ray_pt - plane_pt)) / (plane_dir % ray_dir)
                    if temp < 0:
                        return -1
                    else:
                        return (ray_dir * temp).length()

        return GHyperPlane

    def HyperEllipsoid(self):
        class GHyperEllipsoid(self.Object()):
            def __init__(other, pos: Point, dir: Vector, semiaxes: list[float]) -> None:
                super().__init__(pos, dir)
                other.set_property("semiaxes", semiaxes)

            def planar_rotate(self, inds: (int, int), angle: float) -> None:
                super(GHyperEllipsoid, self).planar_rotate(inds, angle)

            def rotate_3d(self, angles: (float, float, float)) -> None:
                super(GHyperEllipsoid, self).rotate_3d(angles)

            def intersection_distance(self, ray: Ray):
                ray_pt = ray.initial_pt
                ray_dir = ray.dir

                ellips_dir = self.direction

                alpha = (ray_dir[0] ** 2) / (ellips_dir[0] ** 2) + (ray_dir[1] ** 2) / (ellips_dir[1] ** 2) + (
                        ray_dir[2] ** 2) / (ellips_dir[2] ** 2)
                beta = 2 * ((ray_dir[0] * ray_pt[0]) / (ellips_dir[0] ** 2) + (ray_dir[1] * ray_pt[1]) / (
                        ellips_dir[1] ** 2) + (ray_dir[2] * ray_pt[2]) / (ellips_dir[2] ** 2))
                gamma = (ray_pt[0] ** 2) / (ellips_dir[0] ** 2) + (ray_pt[1] ** 2) / (ellips_dir[1] ** 2) + (
                        ray_pt[2] ** 2) / (ellips_dir[2] ** 2)

                disc = beta ** 2 - 4 * alpha * gamma
                if disc < 0:
                    return -1
                else:
                    t1 = (-beta + sqrt(disc)) / (2 * alpha)
                    t2 = (-beta - sqrt(disc)) / (2 * alpha)

                    vec1 = ray_dir * t1
                    vec2 = ray_dir * t2

                    if (t1 > 0) and (t2 > 0):
                        return min(vec1.length(), vec2.length())

                    elif (t1 > 0) and (t2 <= 0):
                        return vec1.length()

                    elif (t1 <= 0) and (t2 < 0):
                        return vec2.length()

                    else:
                        return -1

        return GHyperEllipsoid

    def Canvas(self):
        class GCanvas:
            def __init__(other, n: int, m: int) -> None:
                other.n = n
                other.m = m
                other.distances = Matrix(n, m)
                for row in range(len(other.distances[:])):
                    for col in range(len(other.distances[row][:])):
                        other.distances[row][col] = 999

            def draw(self) -> None:
                pass

            def update(other, camera):
                ray_matrix = camera.get_rays_matrix(other.n, other.m)

                for entity in self.entities:
                    for row_ind, ray_vector in enumerate(ray_matrix):
                        for ray_ind, ray in enumerate(ray_vector):
                            ans = entity.intersection_distance(ray)
                            other.distances[row_ind][ray_ind] = ans if ans < other.distances[row_ind][ray_ind] else \
                                other.distances[row_ind][ray_ind]

        return GCanvas

    def Console(self):
        class GConsole(self.Canvas()):
            def __init__(other):
                other.charmap = ".:;><+r*zsvfwqkP694VOGbUAKXH8RD#$B0MNWQ%&@"

            def draw(self):
                # charmap 42 symbols
                pass

    def Configuration(self):
        class GConfiguration:
            def __init__(self, filepath: str = None):
                self.filepath = None if filepath is None else filepath
                self.configuration: dict[str: any] = dict()

            def set_variable(self, var: str, value):
                self.configuration[var] = value

            def execute_file(self, filepath: str):
                self.filepath = filepath

            def save(self, filepath: str):
                if filepath is None:
                    raise Exception
                with open(filepath) as f:
                    for key in self.configuration.keys():
                        f.write(f"{key} : {self.configuration[key]}\n")

            def __getitem__(self, item):
                return self.configuration[item]

            def __setitem__(self, key, value):
                self.configuration[key] = value

        return GConfiguration
