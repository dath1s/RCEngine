from lib.RCEngine.BasicClasses.Entity import Entity
from lib.RCEngine.BasicClasses.Identifier import Identifier


class EntityList:
    def __init__(self, entities: list[Entity]) -> None:
        self.entities = entities

    def append(self, entity: Entity) -> None:
        self.entities.append(entity)

    def remove(self, entity: Entity) -> None:
        if entity.identifier not in [i.identifier for i in self.entities]:
            raise Exception

        self.entities.remove(entity)

    def get(self, id: Identifier):
        if id not in [i.identifier for i in self.entities]:
            raise Exception

        return [i for i in self.entities if i.identifier == id][0]

    def exec(self, func: callable, *args, **kwargs) -> None:
        for entity in self.entities:
            func(entity, *args, **kwargs)

    def __getitem__(self, item):
        self.get(item)
