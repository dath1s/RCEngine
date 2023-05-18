from lib.Math.Matrix import Matrix
from lib.Math.Vector import Vector


def BilinearForm(matrix: Matrix, vector1: Vector, vector2: Vector):
    if matrix.n != matrix.m and matrix.n == vector1.size and matrix.m == vector2.size:
        # raise EngineException(EngineException.WRONG_SIZE)
        raise Exception

    return sum([matrix[i][j] * vector1[i] * vector2[j] for i in range(matrix.n) for j in range(matrix.n)])
