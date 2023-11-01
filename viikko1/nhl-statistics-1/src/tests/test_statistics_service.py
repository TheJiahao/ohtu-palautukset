import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        self.assertEqual(self.stats.search("Lemieux"), Player("Lemieux", "PIT", 45, 54))

    def test_search_when_player_not_exist(self):
        self.assertEqual(self.stats.search("A"), None)

    def test_team(self):
        team = self.stats.team("EDM")

        self.assertEqual(len(team), 3)

        self.assertIn(Player("Semenko", "EDM", 4, 12), team)
        self.assertIn(Player("Kurri",   "EDM", 37, 53), team)
        self.assertIn(Player("Gretzky", "EDM", 35, 89), team)

    def test_team_with_no_players(self):
        self.assertEqual(self.stats.team("A"), [])

    def test_top(self):
        top3 = self.stats.top(3)

        self.assertEqual(len(top3), 3)

        self.assertEqual(top3[0], Player("Gretzky", "EDM", 35, 89))
        self.assertEqual(top3[1], Player("Lemieux", "PIT", 45, 54))
        self.assertEqual(top3[2], Player("Yzerman", "DET", 42, 56))

    def test_top_return_empty_list_with_zero(self):
        self.assertEqual(len(self.stats.top(0)), 0)
