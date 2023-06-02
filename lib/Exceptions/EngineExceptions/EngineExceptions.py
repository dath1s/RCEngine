class EngineException(Exception):
    pass


class GameObjectExceptions(EngineException):
    @staticmethod
    def WRONG_DIM(d):
        return f"Dimension size must be equal {d}"


class EntityExceptions(EngineException):
    PROPERTY_ERROR = "That property doesn't exists in Entity property list"


class EntityListExceptions(EngineException):
    ID_ERROR = "Entity with that identifier doesn't exists in entity list"
