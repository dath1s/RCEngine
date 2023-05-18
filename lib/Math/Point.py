from lib.Math.Vector import Vector
from lib.Exceptions.MathExceptions.EngineExceptions import PointExceptions


class Point(Vector):
    def __init__(self, n: int = None, elements: list[int | float] | list[list[int | float]] | Vector = None) -> None:
        super().__init__(n, elements)
        match elements:
            case list():
                self.elements = elements
            case Vector():
                self.elements = elements[:]

    def __str__(self):
        return f'Point({", ".join([str(i) for i in self])})'

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise PointExceptions.SUM_TYPE_ERROR
        if self.dim() != other.dim():
            raise PointExceptions.WRONG_DIMS

        return Point(elements=[self[i] + other[i] for i in range(self.dim())])

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise PointExceptions.SUB_TYPE_ERROR
        if self.dim() != other.dim():
            raise PointExceptions.WRONG_DIMS

        return Point(elements=[self[i] - other[i] for i in range(self.dim())])
