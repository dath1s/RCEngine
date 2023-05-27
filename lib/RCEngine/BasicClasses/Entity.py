from lib.Math.CoordinateSystem import CoordinateSystem
from lib.RCEngine.BasicClasses.Identifier import Identifier


class Entity:
    def __init__(self, cs: CoordinateSystem):
        self.cs = cs
        self.identifier = Identifier()
        self.properties = {}

    def set_property(self, prop: str, value: any) -> None:
        self.properties[prop] = value

    def remove_property(self, prop: str) -> None:
        if prop not in self.properties.keys():
            raise Exception
        del self.properties[prop]

    def __getitem__(self, item: str) -> any:
        if item not in self.properties.keys():
            raise Exception
        return self.properties[item]

    def __setitem__(self, key: str, value: any) -> None:
        self.properties[key] = value

    def __getattr__(self, item: str):
        return self[item]
