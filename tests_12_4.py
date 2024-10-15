import logging
from tests_12_1 import RunnerTest
from rt_with_exceptions import Runner as Runner


log_file = 'runner_tests.log'

class RunnerTest(RunnerTest):
    def test_walk(self):
        try:
            rnr1 = Runner('r1', -5)
            for _ in range(10):
                rnr1.walk()
            self.assertEqual(rnr1.distance, 50)
            logging.info('"test_walk" выполнен успешно', exc_info=True)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            rnr1 = Runner(1)
            for _ in range(10):
                rnr1.run()
            self.assertEqual(rnr1.distance, 100)
            logging.info('"test_run" выполнен успешно', exc_info=True)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


logging.basicConfig(level=logging.INFO, filemode='w', filename=log_file,
                    format="%(asctime)s | %(levelname)s | %(message)s", encoding='utf-8')
