from runner_and_tournament import Runner, Tournament
import unittest

class RunnerTest(unittest.TestCase):

    is_frozen = False
    
    @unittest.skipIf(is_frozen, ' Тесты в этом кейсе заморожены')
    def test_walk(self):
        first = Runner('a')
        for i in range(10):
            first.walk()
        self.assertEqual(first.distance,  50)
        
    @unittest.skipIf(is_frozen, ' Тесты в этом кейсе заморожены')
    def test_run(self):
        second = Runner('b')
        for i in range(10):
            second.run()
        self.assertEqual(second.distance,  100)
        
    @unittest.skipIf(is_frozen, ' Тесты в этом кейсе заморожены')
    def test_challenge(self):
        first = Runner('a')
        second = Runner('b')
        for i in range(10):
            first .walk()
            second.run()
        self.assertNotEqual(first.distance, second.distance)

class TournamentTest(unittest.TestCase):

    s_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)

    @unittest.skipIf(s_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tournament (self):
        race = Tournament(90, self.usain, self.nik)
        resault = {key: str(value) for key, value in race.start().items()}
        TournamentTest.all_results.append(resault)
        self.assertEqual(resault[2],"Ник")

    @unittest.skipIf(s_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        race = Tournament(90, self.andrey, self.nik)
        resault = {key: str(value) for key, value in race.start().items()}
        TournamentTest.all_results.append(resault)
        self.assertEqual(resault[2],"Ник")

    @unittest.skipIf(s_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tournament(self):
        race = Tournament(90, self.usain, self.andrey, self.nik)
        resault = {key: str(value) for key, value in race.start().items()}
        TournamentTest.all_results.append(resault)
        self.assertEqual(resault[3],"Ник")


if __name__ == "__main__":
    unittest.main()
