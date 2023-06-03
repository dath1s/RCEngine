from lib.Math.CoordinateSystem import CoordinateSystem
from lib.RCEngine.BasicClasses.Identifier import Identifier
from lib.Exceptions.EngineExceptions.EngineExceptions import EntityExceptions


class Entity:
    def __init__(self, cs: CoordinateSystem):
        self.__dict__["properties"] = set()
        self.set_property("cs", cs)
        self.set_property("identifier", Identifier())

    def set_property(self, prop: str, value: any) -> None:
        if prop == "properties":
            raise Exception

        self.__dict__[prop] = value
        self.__dict__["properties"].add(prop)

    def remove_property(self, prop: str) -> None:
        if prop == "properties":
            raise Exception

        if prop not in self.__dict__["properties"]:
            raise Exception

        self.__delattr__(prop)
        self.__dict__["properties"].remove(prop)

    def get_property(self, item: str):
        if item not in self.__dict__["properties"]:
            raise Exception

        return self.__dict__[item]

    def __getattr__(self, item):
        return self.get_property(item)

    def __setattr__(self, item, value):
        return self.set_property(item, value)

    def __getitem__(self, item):
        return self.get_property(item)

    def __setitem__(self, item, value):
        return self.set_property(item, value)
