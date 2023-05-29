from lib.Math.CoordinateSystem import CoordinateSystem
from lib.Math.Vector import Vector
from lib.Math.Point import Point


class Ray:
    def __init__(self, cs: CoordinateSystem, initial_pt: Point, direction: Vector) -> None:
        self.cs = cs
        self.initial_pt = initial_pt
        self.dir = direction

    def normalize(self) -> None:
        self.dir = self.dir.normalize()
