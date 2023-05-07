from math import pi, cos, sin
from lib.Exceptions.EngineExceptions import MatrixException


class Matrix:
    def __init__(self, n: int = 0, m: int = None, elements: list[list[int | float]] = None) -> None:
        match (n, m, elements):
            case (n, None, None):
                self.elements = [[0 for _ in range(n)] for _ in range(n)]
                self.m = self.n = n
            case (n, m, None):
                self.elements = [[0 for _ in range(m)] for _ in range(n)]
                self.m = m
                self.n = n
            case (_, None, elements):
                self.elements = elements
                self.n = len(elements)
                self.m = len(elements[0])

    def __str__(self) -> str:
        return f"Matrix_{self.n}x{self.m}[{', '.join([str(row) for row in self.elements])}]"

    def __getitem__(self, item: int | slice) -> list[int | float] | int | float:
        return self.elements[item]

    def __setitem__(self, key: int | slice, value: int | float | list) -> None:
        self[key] = value

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise MatrixException.SUM_TYPE_ERROR

        if (self.n, self.m) != (other.n, other.m):
            raise MatrixException.MATRIX_WRONG_SIZES(self.n, self.m, other.n, other.m)

        return Matrix(elements=[
            [self[row][col] + other[row][col] for col in range(self.m)] for row in range(self.n)
        ])

    def __mul__(self, other):
        if not isinstance(other, int | float | Matrix):
            raise MatrixException.MUL_TYPE_ERROR

        match other:
            case int() | float():
                return Matrix(elements=[
                    [self[row][col] * other for col in range(self.m)] for row in range(self.n)
                ])
            case Matrix():
                if self.m != other.n:
                    raise MatrixException.MATRIX_WRONG_SIZES(self.n, self.m, other.n, other.m)

                return Matrix(elements=[
                    [sum([i * j for (i, j) in zip(row1, row2)]) for row2 in zip(*(other[:]))] for row1 in self[:]
                ])

    def __rmul__(self, other):
        if not isinstance(other, int | float | Matrix):
            raise MatrixException.MUL_TYPE_ERROR

        return self.__mul__(other)

    def get_minor(self, rows: list[int], cols: list[int]):
        return Matrix(elements=[
            [self[row][col] for col in range(self.m) if col not in cols] for row in range(self.n) if row not in rows
        ])

    def determinant(self):
        if self.n != self.m:
            raise MatrixException.MATRIX_NOT_SQUARED

        if isinstance(self[0][0], int | float):
            if self.n == 1:
                return self[0][0]

            det = 0
            for i in range(self.n):
                m = Matrix(elements=[row[:i] + row[i + 1:] for row in self[1:]])
                det += (-1) ** i * self.elements[0][i] * m.determinant()

            return det
        else:
            ans_vector = Matrix(elements=[[0, 0, 0]])
            for i in range(self.n):
                sub_matrix = self.get_minor([0], [i])
                ans_vector += (-1) ** i * sub_matrix.determinant() * self.elements[0][i]
            return ans_vector

    def transpose(self):
        return Matrix(elements=[
            list(line) for line in list(zip(*self[:]))
        ])

    def inverse(self):
        if self.n != self.m:
            raise MatrixException.MATRIX_NOT_SQUARED
        if not self.determinant():
            raise MatrixException.ZERO_DETERMINANT

        alpha: float = 1 / self.determinant()
        addition_matrix = Matrix(n=self.n)
        for row in range(self.n):
            for col in range(self.m):
                addition_matrix[row][col] = self.get_minor([row], [col]).determinant() * ((-1) ** (row + col))
        return addition_matrix.transpose() * alpha

    @staticmethod
    def identity(n: int):
        return Matrix(elements=[
            [1 if row == col else 0 for col in range(n)] for row in range(n)
        ])

    def euclid_norm(self) -> float:
        return sum([i ** 2 for i in sum(self, [])]) ** .5

    def norm(self) -> float:
        return sum([max([abs(x) for x in row]) for row in self])

    def __truediv__(self, other):
        if not isinstance(other, int | float | Matrix):
            raise MatrixException.DIV_TYPE_ERROR
        match other:
            case int() | float():
                return self * (1 / other)
            case Matrix():
                return self * other.inverse()

    def __sub__(self, other):
        return self.__add__((-1) * other)

    def __invert__(self):
        return self.inverse()

    @staticmethod
    def gram(args):
        if not all([isinstance(vector, Matrix) for vector in args]):
            raise MatrixException.GRAM_TYPE_ERROR
        if not all([vector.n == 1 for vector in args]):
            raise MatrixException.WRONG_SIZE

        gram_matrix = Matrix(n=len(args))
        for i in range(len(args)):
            for j in range(len(args)):
                for (vector1, vector2) in zip(args[i], args[j]):
                    gram_matrix[i][j] = sum(vector1[k] * vector2[k] for k in range(len(vector1)))

        return gram_matrix

    def rotate(self, axes_inx: list[int], angle: float | int):
        angle = angle*pi/180
        rot_matrix = Matrix().identity(self.m)

        power = (-1) ** sum(axes_inx)
        rot_matrix[axes_inx[0]][axes_inx[0]] = round(cos(angle), 6)
        rot_matrix[axes_inx[1]][axes_inx[1]] = round(cos(angle), 6)
        rot_matrix[axes_inx[1]][axes_inx[0]] = power * round(sin(angle), 6)
        rot_matrix[axes_inx[0]][axes_inx[1]] = (-power) * round(sin(angle), 6)

        return self * rot_matrix

    def teit_bryan_rotate(self, angles: list[int | float]):
        if len(angles) == 2:
            angle = angles[0] * pi / 180
            rotation_matrix = Matrix(elements=[[cos(angle), -sin(angle)],
                                               [sin(angle), cos(angle)]])
            return self * rotation_matrix
        elif len(angles) == 3:
            angle_x, angle_y, angle_z = angles[0] * pi / 180, angles[1] * pi / 180, angles[2] * pi / 180

            rotation_matrix_x = Matrix(elements=[[1, 0, 0],
                                                 [0, cos(angle_x), -sin(angle_x)],
                                                 [0, sin(angle_x), cos(angle_x)]])
            rotation_matrix_y = Matrix(elements=[[cos(angle_y), 0, -sin(angle_y)],
                                                 [0, 1, 0],
                                                 [sin(angle_y), 0, cos(angle_y)]])
            rotation_matrix_z = Matrix(elements=[[cos(angle_z), -sin(angle_z), 0],
                                                 [sin(angle_z), cos(angle_z), 0],
                                                 [0, 0, 1]])

            return self * rotation_matrix_x * rotation_matrix_y * rotation_matrix_z
        else:
            raise MatrixException.WRONG_DIMENSION

    def __eq__(self, other):
        if (self.n != other.n) | (self.m != other.m):
            return False
        return all(abs(self[i][j] - other[i][j]) < 1e-5 for i in range(self.n) for j in range(self.m))
