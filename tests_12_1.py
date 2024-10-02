import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        rnr1 = Runner.Runner('r1')
        for _ in range(10):
            rnr1.walk()
        self.assertEqual(rnr1.distance, 50)

    def test_run(self):
        rnr1 = Runner.Runner('r1')
        for _ in range(10):
            rnr1.run()
        self.assertEqual(rnr1.distance, 100)

    def test_challenge(self):
        rnr1 = Runner.Runner('r1')
        rnr2 = Runner.Runner('r2')
        for _ in range(10):
            rnr1.run()
        for _ in range(10):
            rnr2.walk()
        self.assertNotEqual(rnr1, rnr2)

#rt = RunnerTest()
