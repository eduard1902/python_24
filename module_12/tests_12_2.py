from runner_and_tournament import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):

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

    def test_1(self):
        race = Tournament(90, self.usain, self.nik)
        resault = {key: str(value) for key, value in race.start().items()}
        TournamentTest.all_results.append(resault)
        self.assertEqual(resault[2],"Ник")

    def test_2(self):
        race = Tournament(90, self.andrey, self.nik)
        resault = {key: str(value) for key, value in race.start().items()}
        TournamentTest.all_results.append(resault)
        self.assertEqual(resault[2],"Ник")

    def test_3(self):
        race = Tournament(90, self.usain, self.andrey, self.nik)
        resault = {key: str(value) for key, value in race.start().items()}
        TournamentTest.all_results.append(resault)
        self.assertEqual(resault[3],"Ник")


if __name__ == "--main__":
    unittest.main()
