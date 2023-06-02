from lib.Math.CoordinateSystem import CoordinateSystem
from lib.RCEngine.BasicClasses.Identifier import Identifier
from lib.Exceptions.EngineExceptions.EngineExceptions import EntityExceptions


class Entity:
    def __init__(self, cs: CoordinateSystem):
        self.cs = cs
        self.identifier = Identifier()
        self.properties = {}

    def set_property(self, prop: str, value: any) -> None:
        self.properties[prop] = value

    def remove_property(self, prop: str) -> None:
        if prop not in self.properties.keys():
            raise EntityExceptions.PROPERTY_ERROR
        del self.properties[prop]

    def get_property(self, item: str):
        if item not in self.properties.keys():
            raise EntityExceptions.PROPERTY_ERROR
        return self.properties[item]

    def __getitem__(self, item: str) -> any:
        return self.get_property(item)

    def __setitem__(self, key: str, value: any) -> None:
        self.properties[key] = value

    def __getattr__(self, item: str):
        return self[item]
