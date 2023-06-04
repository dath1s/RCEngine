import uuid

class Identifier:
    IDS = set()

    def __init__(self):
        self.value = Identifier.__generate__()
        Identifier.IDS.add(self.value)

    def get_value(self):
        return self.value

    @classmethod
    def __generate__(cls):
        value = uuid.uuid4()

        if value in cls.IDS:
            return cls.__generate__()

        return value

    def __eq__(self, other):
        return True if self.value == other.value else False
