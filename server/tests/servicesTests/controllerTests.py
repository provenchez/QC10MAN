import unittest

from server.sources.controller.controller import Controller


class ControllerTests(unittest.TestCase):

    def testControllerConstructor(self):
        self.controller = Controller()
        self.assertEquals(0,0)