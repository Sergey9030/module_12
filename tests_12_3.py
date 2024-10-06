import unittest
from runner_and_tournament import Runner as Runner, Tournament as Tournament

def print_dict(dct):
    for i in dct:
        spr = ''
        print(i, ':{', end='', sep='')
        for j in dct[i]:
            print(f'{spr}{j}:{dct[i][j]}', end='')
            spr = ', '
        print('}')

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        rnr1 = Runner('r1')
        for _ in range(10):
            rnr1.walk()
        self.assertEqual(rnr1.distance, 50)

    @unittest.skipIf(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        rnr1 = Runner('r1')
        for _ in range(10):
            rnr1.run()
        self.assertEqual(rnr1.distance, 100)

    @unittest.skipIf(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        rnr1 = Runner('r1')
        rnr2 = Runner('r2')
        for _ in range(10):
            rnr1.run()
        for _ in range(10):
            rnr2.walk()
        self.assertNotEqual(rnr1, rnr2)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(self):
        setattr(self, 'all_results', {})

    def setUp(self):
        self.Usein = Runner("Усэйн", 10)
        self.Andrey = Runner("Андрей", 9)
        self.Nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(self):
        print_dict(self.all_results)

    @unittest.skipIf(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament1(self):
        t1 = Tournament(40, self.Usein, self.Nik)
        r1 = t1.start()
        self.all_results['Test1'] = r1
        self.assertTrue(r1[len(r1)] == 'Ник')

    @unittest.skipIf(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament2(self):
        t1 = Tournament(90, self.Andrey, self.Nik)
        r1 = t1.start()
        self.all_results['Test2'] = r1
        self.assertTrue(r1[len(r1)] == 'Ник')

    @unittest.skipIf(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament3(self):

        t1 = Tournament(90, self.Usein, self.Andrey, self.Nik)
        r1 = t1.start()
        self.all_results['Test3'] = r1
        self.assertTrue(r1[len(r1)] == 'Ник')

    @unittest.skipIf(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament4(self):
        t1 = Tournament(6, self.Usein, self.Andrey, self.Nik)
        r1 = t1.start()
        self.all_results['Test4'] = r1
        self.assertTrue(r1[len(r1)] == 'Ник')
