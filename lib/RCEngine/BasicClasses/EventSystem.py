class EventSystem:
    def __init__(self):
        self.events: dict[str: list] = dict()

    def add(self, name: str):
        self.events[name] = []

    def remove(self, name: str):
        if name not in self.events.keys():
            raise Exception
        del self.events[name]

    def handle(self, name: str, function):
        if name not in self.events.keys():
            raise Exception
        self.events[name].append(function)

    def remove_handle(self, name: str, function):
        if name not in self.events.keys():
            raise Exception
        if function not in self.events[name]:
            raise Exception
        del self.events[name][self.events[name].index(function)]

    def trigger(self, name: str, *args):
        if name not in self.events.keys():
            raise Exception

        for item in self.events[name]:
            item(*args)

    def get_handle(self, name: str):
        return self.events[name]

    def __getitem__(self, item: str):
        return self.events[item]

