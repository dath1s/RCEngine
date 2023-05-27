class EngineException(Exception):
    pass


class GameObjectExceptions(EngineException):
    @staticmethod
    def WRONG_DIM(d):
        return f"Dimension size must be equal {d}"
