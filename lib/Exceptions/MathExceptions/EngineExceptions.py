class EngineException(Exception):
    pass


class MatrixException(EngineException):
    SUM_TYPE_ERROR = 'added element must be Matrix()'
    SUB_TYPE_ERROR = 'subtracted element must be Matrix()'
    MUL_TYPE_ERROR = 'Matrix() can be multiplied by int/float or Matrix()'
    MATRIX_NOT_SQUARED = 'Matrix() is not square'
    ZERO_DETERMINANT = 'matrix determinant equals 0'
    DIV_TYPE_ERROR = 'Matrix() can be divided by int/float or Matrix()'
    GRAM_TYPE_ERROR = 'all elements in args must be Matrix()'
    WRONG_SIZE = 'Matrix() must be 1xm'
    WRONG_DIMENSION = 'Matrix() can be rotated only in 2/3 dimension'
    WRONG_SIZE = "different size, so operation isn't allowed"

    @staticmethod
    def MATRIX_WRONG_SIZES(n1: int, m1: int, n2: int, m2: int) -> str:
        return f" Wrong sizes : {n1}x{m1} and {n2}x{m2}"


class VectorException(EngineException):
    SUM_TYPE_ERROR = 'added element must be Vector()'
    SUB_TYPE_ERROR = 'subtracted element must be Vector()'
    SUM_IS_LINE_ERROR = "column Vector() and string Vector() can't be added"
    SCALAR_PROD_ERROR = 'second element must be Vector()'
    SCALAR_PROD_IS_LINE_ERROR = 'first Vector() and second Vector() both must be column/string vectors'
    SCALAR_PROD_TYPE_ERROR = 'all elements must be Matrix()'
    VECTOR_PROD_TYPE_ERROR = 'all elements must be Vector()/Matrix()'
    WRONG_DIMS = "not all vectors dims equals 3"
    VECTOR_TYPE_ERROR = "to multiply a Vector() by a Vector(), they must be of different types"

    @staticmethod
    def VECTOR_WRONG_SIZES(n1: int, m1: int, n2: int, m2: int) -> str:
        return f" Wrong sizes : {n1}x{m1} and {n2}x{m2}"


class VectorSpaceExceptions(EngineException):
    AS_POINT_TYPE_ERROR = "as_point() can be used only for Point() type"
    WRONG_DIMS = "VectorSpace() dim and Point dim must be equal"


class PointExceptions(EngineException):
    SUM_TYPE_ERROR = "only Vector() can be added to Point()"
    WRONG_DIMS = "all Point() type variables must be same dim"
    SUB_TYPE_ERROR = "Point() can be substracted only by Vector()"

