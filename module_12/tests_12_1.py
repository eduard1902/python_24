import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        first = Runner('a')
        for i in range(10):
            first.walk()
        self.assertEqual(first.distance,  50)

    def test_run(self):
        second = Runner('b')
        for i in range(10):
            second.run()
        self.assertEqual(second.distance,  100)

    def test_challenge(self):
        first = Runner('a')
        second = Runner('b')
        for i in range(10):
            first .walk()
            second.run()
        self.assertNotEqual(first.distance, second.distance)


if __name__ == "__main__":
    unittest.main()
