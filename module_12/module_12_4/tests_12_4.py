import logging
import unittest
from rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8", format="%(asctime)s | %(levelname)s | %(message)s")

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            first = Runner("Клод", -5) # speed: 5 (for выполнен успешно)
            for i in range(10):
                first.walk()
            self.assertEqual(first.distance, 50, "test_walk выполнен успешно")
            # logging.info('"test_walk" выполнен успешно')
        except  ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            second = Runner(int)
            for i in range(10):
                second.run()
            self.assertEqual(second.distance, 100, "test_run выполнен успешно")
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


if __name__ == "__main__":
    unittest.main()