from unittest import TestCase
from lib.EventSystem import EventSystem


class TestEventSystem(TestCase):
    def test_add(self):
        es = EventSystem()
        es.add('move')
        self.assertEqual('move' in es.events.keys(), True)

    def test_remove(self):
        es = EventSystem()
        es.add('move')
        es.remove('move')
        self.assertEqual('move' in es.events.keys(), False)

    def test_handle(self):
        es = EventSystem()
        es.add('move')

        def f():
            return 0

        es.handle('move', f)
        self.assertEqual(es['move'][0] is f, True)

    def test_remove_handle(self):
        es = EventSystem()
        es.add('move')

        def f():
            return 0

        es.handle('move', f)
        es.remove_handle('move', f)
        self.assertEqual(len(es['move']), 0)

    def test_remove_handle_not_working(self):
        es = EventSystem()
        es.add('move')

        def f():
            return 0

        def g():
            return 0

        es.handle('move', f)
        # es.remove_handle('move', g)
        # self.assertEqual(len(es['move']), 1)

    def test_get_handle(self):
        es = EventSystem()
        es.add('move')

        def f():
            return 0

        es.handle('move', f)
        self.assertEqual(es.get_handle('move'), [f])
