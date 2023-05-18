class Identifier:
    IDS = set([0])

    def __init__(self):
        self.value = Identifier.__generate__()
        Identifier.IDS.add(self.value)

    def get_value(self):
        return self.value

    @classmethod
    def __generate__(cls):
        value = cls.IDS[-1] + 1 # Some magic

        if value in cls.IDS:
            return cls.__generate__()

        return value
