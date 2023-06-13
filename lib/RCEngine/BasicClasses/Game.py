from lib.Math.CoordinateSystem import CoordinateSystem
from lib.RCEngine.BasicClasses.EntityList import EntityList
from lib.Math.Vector import Vector
from lib.Math.Point import Point
from math import pi, atan, tan
from config.globals import *
from lib.RCEngine.BasicClasses.Entity import Entity
from lib.RCEngine.BasicClasses.Ray import Ray
from lib.Math.Matrix import Matrix
from math import sqrt
from lib.EventSystem import EventSystem
from curses import wrapper
from math import sqrt


class Game:
    def __init__(self, cs: CoordinateSystem, entities: EntityList = [], es: EventSystem = None):
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
            def __init__(self, pos: Point, dir: Vector | None):
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
                super().__init__(position, None)
                other.set_property('fov', round(fov * pi / 180, PRECISION))
                other.set_property('draw_dist', round(draw_dist, PRECISION))
                other.entity = Entity(other.cs)

                if vfov is None:
                    other.set_property('vfov', atan((SCREEN_SIZE[0] / SCREEN_SIZE[1]) * tan(other['fov'] / 2)))
                else:
                    other.set_property('vfov', round(vfov * pi / 180, PRECISION))

                if look_at is not None:
                    other.set_property('look_at', look_at)

                other.set_property('direction', Vector(
                    elements=[other['look_at'][i] - other['position'][i] for i in
                              range(len(other['position'][:]))]).normalize())

            def get_rays_matrix(self, n: int, m: int):
                deltaAlpha = self.fov / n
                deltaBetta = self.vfov / m

                zeroAngleX = self.fov / 2.0
                zeroAngleY = self.vfov / 2.0

                position = self.position
                direction = self.direction

                rayMatrix = Matrix(n, m)
                for r in range(n):
                    curAngleX = deltaAlpha * r - zeroAngleX
                    for c in range(m):
                        curAngleY = deltaBetta * c - zeroAngleY

                        proectionDir = direction.rotate([1, 2], curAngleX).rotate([0, 2], curAngleY)
                        projectionDir = direction.length() ** 2 / direction.scalar_product(proectionDir) * proectionDir
                        rayMatrix[r][c] = Ray(self.cs, position, projectionDir)

                return rayMatrix

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
                A, B, C, D = [0 for _ in range(4)]
                for i in range(len(self.semiaxes)):
                    A += ray.dir[i] ** 2
                    B += (ray.initial_pt[i] - self.position[i]) * ray.dir[i]
                    C += (ray.initial_pt[i] - self.position[i]) ** 2
                    D += self.semiaxes[i] ** 2

                B *= 2
                C -= D

                discr = B ** 2 - 4 * A * C
                if discr < 0:
                    return 999

                sol1, sol2 = (-B - sqrt(discr)) / (2 * A), (-B + sqrt(discr)) / (2 * A)

                if sol1 < 0:
                    if sol2 < 0:
                        return 999
                    return sol2
                if sol2 < 0:
                    return sol1
                return min(sol1, sol2)

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

            def update(other, camera):
                ray_matrix = camera.get_rays_matrix(other.n, other.m)
                other.distances = Matrix(other.n, other.m)
                for row in range(len(other.distances[:])):
                    for col in range(len(other.distances[row][:])):
                        other.distances[row][col] = 999

                for entity in self.entities.entities:
                    for row_ind, ray_vector in enumerate(ray_matrix):
                        for ray_ind, ray in enumerate(ray_vector):
                            ans = entity.intersection_distance(ray)
                            other.distances[row_ind][ray_ind] = ans if ans < other.distances[row_ind][ray_ind] else \
                                other.distances[row_ind][ray_ind]

        return GCanvas

    def Console(self):
        class GConsole(self.Canvas()):
            def __init__(other):
                other.charmap = ".:;><+r*zsvfwqkP694VOGbUAKXH8RD#$B0MNWQ%&@"[::-1]

            def draw(self, canvas, camera):
                def main(stdscr):
                    stdscr.clear()

                    while True:
                        canvas.update(camera)

                        stdscr.addstr(47, 0, f"camera at: {str(camera.position)}")
                        stdscr.addstr(48, 0, f"camera direction: {str(camera.direction)}")

                        for i in range(canvas.n):
                            for j in range(canvas.m):
                                if canvas.distances[i][j] >= camera.draw_dist:
                                    stdscr.addch(i, j, '.')
                                else:
                                    ratio = canvas.distances[i][j] / camera.draw_dist
                                    ind = int(ratio * 38)
                                    stdscr.addch(i, j, self.charmap[ind])
                        camera.set_direction(camera.direction + Vector(elements=[0, 0, 0.05]))

                        key = stdscr.getkey()
                        if key == "q":
                            exit(0)
                        if key == 'w':
                            camera.move(Vector(elements=[0, 0, 1]))
                        if key == 's':
                            camera.move(Vector(elements=[0, 0, -1]))
                        if key == ' ':
                            camera.move(Vector(elements=[0, 0.2, 0]))
                        if key == 'v':
                            camera.move(Vector(elements=[0, -0.2, 0]))
                        if key == 'a':
                            camera.move(Vector(elements=[-0.2, 0, 0]))
                        if key == 'd':
                            camera.move(Vector(elements=[0.2, 0, 0]))
                        if key == 'KEY_RIGHT':
                            camera.direction = camera.direction.rotate([0, 2], 0.2)
                        if key == 'KEY_LEFT':
                            camera.direction = camera.direction.rotate([0, 2], -0.2)
                        if key == 'KEY_UP':
                            camera.direction = camera.direction.rotate([1, 2], -0.2)
                        if key == 'KEY_DOWN':
                            camera.direction = camera.direction.rotate([1, 2], 0.2)

                        stdscr.refresh()

                wrapper(main)

        return GConsole

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
