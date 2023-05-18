from lib.Math.Matrix import Matrix
from lib.Exceptions.MathExceptions.EngineExceptions import VectorException


class Vector:
    def __init__(self, n: int = None, elements: list[int | float] | list[list[int | float]] = None) -> None:
        match (n, elements):
            case n, None:
                self.elements = [0 for _ in range(n)]
                self.is_line = True
            case None, elements:
                self.elements = elements
                self.is_line = True if isinstance(elements[0], (int, float)) else False

    def __getitem__(self, item: (int | slice)):
        if self.is_line:
            return self.elements[item]
        return self.elements[item] if isinstance(item, slice) else self.elements[item][0]

    def __setitem__(self, key, value) -> None:
        if self.is_line:
            self.elements[key] = value
        self.elements[key][0] = value

    def addition(self, other):
        if not isinstance(other, Vector):
            raise VectorException.SUM_TYPE_ERROR
        if self.dim() != other.dim():
            x1, y1 = [1, len(self.elements)] if self.is_line else [len(self.elements), 1]
            x2, y2 = [1, len(other.elements)] if other.is_line else [len(other.elements), 1]
            raise VectorException.VECTOR_WRONG_SIZES(x1, y1, x2, y2)
        if self.is_line != other.is_line:
            raise VectorException.SUM_IS_LINE_ERROR

        if self.is_line:
            return Vector(elements=[self[i] + other[i] for i in range(self.dim())])
        return Vector(elements=[[self[i] + other[i]] for i in range(self.dim())])

    def __add__(self, other):
        return self.addition(other)

    def multiplication(self, other):
        if isinstance(other, Vector):
            if self.dim() != other.dim():
                raise VectorException.WRONG_DIMS
            if self.is_line != (not other.is_line):
                raise VectorException.VECTOR_TYPE_ERROR

            return self.vector2matrix() * other.vector2matrix()

        if self.is_line:
            return Vector(elements=[self[i] * other for i in range(self.dim())])
        return Vector(elements=[[self[i] * other] for i in range(self.dim())])

    def __mul__(self, other):
        return self.multiplication(other)

    def __sub__(self, other):
        return self.__add__((-1) * other)

    def __truediv__(self, other: int | float):
        return self.__mul__(1 / other)

    def __rmul__(self, other):
        raise self.__mul__(other)

    def vector2matrix(self):
        if self.is_line:
            return Matrix(elements=[self.elements])
        return Matrix(elements=self.elements)

    def scalar_product(self, other, basis=None):
        if not isinstance(other, Vector):
            raise VectorException.SCALAR_PROD_ERROR
        if self.dim() != other.dim():
            x1, y1 = [1, len(self.elements)] if self.is_line else [len(self.elements), 1]
            x2, y2 = [1, len(other.elements)] if other.is_line else [len(other.elements), 1]
            raise VectorException.VECTOR_WRONG_SIZES(x1, y1, x2, y2)
        if self.is_line != other.is_line:
            raise VectorException.SCALAR_PROD_IS_LINE_ERROR
        if basis is None:
            ortonorm_basis = [Matrix(elements=[[1 if x == i else 0 for x in range(self.dim())]]) for i in
                              range(self.dim())]
        else:
            if len(basis) != self.dim():
                x1, y1 = [1, len(self.elements)] if self.is_line else [len(self.elements), 1]
                x2, y2 = [1, len(other.elements)] if other.is_line else [len(other.elements), 1]
                raise VectorException.VECTOR_WRONG_SIZES(x1, y1, x2, y2)
            if not all([isinstance(i, Matrix) for i in basis]):
                raise VectorException.SCALAR_PROD_TYPE_ERROR
            ortonorm_basis = basis

        if not self.is_line:
            self = self.transpose()
        if other.is_line:
            other = other.transpose()
        return (self.vector2matrix() * Matrix().gram(ortonorm_basis) * other.vector2matrix())[0][0]

    def vector_product(self, other, basis=None):
        if not isinstance(other, Vector):
            raise VectorException.VECTOR_PROD_TYPE_ERROR
        if self.dim() != 3 | other.dim() != 3:
            raise VectorException.WRONG_DIMS

        if basis is None:
            v1, v2, v3 = [Matrix(elements=[[1 if x == i else 0 for x in range(3)]]) for i in range(3)]
        else:
            if len(basis) != 3:
                raise VectorException.WRONG_DIMS
            if not all([isinstance(i, Matrix) for i in basis]):
                raise VectorException.VECTOR_PROD_TYPE_ERROR
            v1, v2, v3 = basis

        return Matrix(elements=[[v1, v2, v3],
                                [self[0], self[1], self[2]],
                                [other[0], other[1], other[2]]]).determinant()

    def length(self) -> float:
        return (self % self) ** 0.5

    def normalize(self):
        return self / self.length()

    def dim(self) -> int:
        return len(self[:])

    def __mod__(self, other):
        return self.scalar_product(other)

    def __pow__(self, other):
        return self.vector_product(other)

    def __str__(self):
        return f'{"strint" if self.is_line else "column"} Vector[{", ".join([str(i) for i in self.elements])}]'

    def transpose(self):
        if self.is_line:
            return Vector(elements=[[i] for i in self.elements])
        return Vector(elements=[i[0] for i in self.elements])

    def rotate(self, axes: list[int], angle: float):
        if not self.is_line:
            return Vector(elements=self.transpose().vector2matrix().rotate(axes, angle)[0][:])
        return Vector(elements=self.vector2matrix().rotate(axes, angle)[0][:])

    def teit_bryan_rotate(self, angles: list[int:float]):
        if not self.is_line:
            return self.transpose().vector2matrix().teit_bryan_rotate(angles)
        return self.vector2matrix().teit_bryan_rotate(angles)

    def __eq__(self, other):
        if self.dim() != other.dim():
            return False
        if self.is_line != other.is_line:
            return False
        return all([abs(self[i] - other[i]) < 1e-5 for i in range(self.dim())])
