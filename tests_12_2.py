from runner_and_tournament import Runner as Runner, Tournament as Tournament
import unittest


def print_dict(dct):
    for i in dct:
        spr = ''
        print(i, ':{', end='', sep='')
        for j in dct[i]:
            print(f'{spr}{j}:{dct[i][j]}', end='')
            spr = ', '
        print('}')


class TournamentTest(unittest.TestCase):

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

    def test_Tournament1(self):
        t1 = Tournament(40, self.Usein, self.Nik)
        r1 = t1.start()
        self.all_results['Test1'] = r1
        self.assertTrue(r1[len(r1)] == 'Ник')

    def test_Tournament2(self):
        t1 = Tournament(90, self.Andrey, self.Nik)
        r1 = t1.start()
        self.all_results['Test2'] = r1
        self.assertTrue(r1[len(r1)] == 'Ник')

    def test_Tournament3(self):

        t1 = Tournament(90, self.Usein, self.Andrey, self.Nik)
        r1 = t1.start()
        self.all_results['Test3'] = r1
        self.assertTrue(r1[len(r1)] == 'Ник')

    def test_Tournament4(self):
        t1 = Tournament(6, self.Usein, self.Andrey, self.Nik)
        r1 = t1.start()
        self.all_results['Test4'] = r1
        self.assertTrue(r1[len(r1)] == 'Ник')

"""
        При забеге на малые дистанции (до 6) все участники достигнyт финиша
    за один проход цика for в методе start.
    Усейн первый в списке и он будет первым удален из спска participants и
    первым добавлен в список finishers.
    Первам в списке participants станет Андрей.
    После завершения цикла for указатель participant сместится на второй элемент списка,
    которым теперь является Ник и Ник будет обработан вторым и вторым помещен в список finishers.
    И оставшееся третье место достается Андрею.
        Чтобы в этом убедиться мжно добавить print в цикл for и увидеть, в каком порядке
    обрабатываются участники.
    
    Лечение: Заменим цикл for на while и при удалении участника из списка participants
            не будем увеличивать указатель.
    
    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            participant = 0
            while participant < len(self.participants):
                self.participants[participant].run()
                if self.participants[participant].distance >= self.full_distance:
                    finishers[place] = self.participants[participant]
                    place += 1
                    self.participants.remove(self.participants[participant])
                else:
                    participant += 1
        return finishers

Но проблему это не решает, мы просто обработали список последовательно.

И нет тут никакой логической ошибки. Участники достигли финиша одновремеено и результат уних одинаков.
Это, как если бы судья на финише фиксировал пересечение финишной черты раз за 6 сек.

Если мы хотим, что бы при одинаковом результате выигрывал самый быстрый мы должны разместить
участников в списке в порядке убывания их скорости и использовать предложенный код.

Проблема в дискретизации. Наши участники движуться дискретно (минимальная величина дескетизации = 6)
и пока длина дистанции больше этой величинв все в порядке.
А дальше мы переходим на поле боя квантовой физики со всеми ее неопределенностями.(Прикол)
"""
