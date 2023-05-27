from lib.Math.Vector import Vector
from lib.Math.Matrix import Matrix
from lib.Exceptions.MathExceptions.MathExceptions import VectorSpaceExceptions


class VectorSpace:
    def __init__(self, basis: list[Vector]) -> None:
        self.basis = basis

    def scalar_product(self, v1: Vector, v2: Vector) -> float:
        return v1.scalar_product(v2, basis=self.basis)

    def vector_product(self, v1: Vector, v2: Vector) -> Vector:
        return v1.vector_product(v2, basis=self.basis)

    def as_vector(self, point):
        if not isinstance(point, Vector):
            raise VectorSpaceExceptions.AS_POINT_TYPE_ERROR
        if self.basis[0].dim() != point.dim():
            raise VectorSpaceExceptions.WRONG_DIMS

        ans = Matrix(1, point.dim())
        det = Matrix(elements=[i[:] for i in self.basis]).determinant()

        for col in range(point.dim()):
            dt_matrix = Matrix(elements=[i[:] for i in self.basis]).transpose()
            for row in range(point.dim()):
                dt_matrix[row][col] = point[row]

            ans[0][col] = dt_matrix.determinant() / det
        return Vector(elements=ans.elements[0])

    def __str__(self):
        return 'basis:\n' + ''.join(["\t" + str(i) + "\n" for i in self.basis])
