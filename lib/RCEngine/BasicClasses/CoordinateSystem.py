from lib.RCEngine.BasicClasses.Point import Point
from lib.RCEngine.BasicClasses.VectorSpace import VectorSpace


class CoordinateSystem:
    def __init__(self, initial: Point, basis: VectorSpace) -> None:
        self.initial_point = initial
        self.space = basis
