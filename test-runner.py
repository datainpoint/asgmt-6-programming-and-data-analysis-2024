import unittest
import importlib
import numpy as np
import pandas as pd

class TestAssignmentSix(unittest.TestCase):
    def test_01_import_teams_nba_json(self):
        teams_json = asgmt.import_teams_nba_json()
        self.assertIsInstance(teams_json, dict)
        self.assertEqual(len(teams_json["data"]), 30)
    def test_02_find_teams_conference_division(self):
        self.assertEqual(asgmt.find_teams_conference_division("BOS"), ('East', 'Atlantic'))
        self.assertEqual(asgmt.find_teams_conference_division("MIA"), ('East', 'Southeast'))
        self.assertEqual(asgmt.find_teams_conference_division("NYK"), ('East', 'Atlantic'))
        self.assertEqual(asgmt.find_teams_conference_division("PHI"), ('East', 'Atlantic'))
        self.assertEqual(asgmt.find_teams_conference_division("LAL"), ('West', 'Pacific'))
        self.assertEqual(asgmt.find_teams_conference_division("DEN"), ('West', 'Northwest'))
        self.assertEqual(asgmt.find_teams_conference_division("PHX"), ('West', 'Pacific'))
        self.assertEqual(asgmt.find_teams_conference_division("GSW"), ('West', 'Pacific'))
    def test_03_find_teams_city(self):
        self.assertEqual(asgmt.find_teams_city("Celtics"), "Boston")
        self.assertEqual(asgmt.find_teams_city("Heat"), "Miami")
        self.assertEqual(asgmt.find_teams_city("Knicks"), "New York")
        self.assertEqual(asgmt.find_teams_city("76ers"), "Philadelphia")
        self.assertEqual(asgmt.find_teams_city("Lakers"), "Los Angeles")
        self.assertEqual(asgmt.find_teams_city("Nuggets"), "Denver")
        self.assertEqual(asgmt.find_teams_city("Suns"), "Phoenix")
        self.assertEqual(asgmt.find_teams_city("Warriors"), "Golden State")
    def test_04_import_movies_csv(self):
        movies = asgmt.import_movies_csv()
        self.assertIsInstance(movies, pd.core.frame.DataFrame)
        self.assertEqual(movies.shape, (250, 5))
    def test_05_find_top_gun_maverick(self):
        top_gun_maverick = asgmt.find_top_gun_maverick()
        self.assertIsInstance(top_gun_maverick, pd.core.frame.DataFrame)
        self.assertEqual(top_gun_maverick.shape, (1, 5))
    def test_06_find_starwars_episodes(self):
        starwars_episodes = asgmt.find_starwars_episodes()
        self.assertIsInstance(starwars_episodes, pd.core.frame.DataFrame)
        self.assertEqual(starwars_episodes.shape, (3, 5))
    def test_07_import_team_taiwan(self):
        team_taiwan = asgmt.import_team_taiwan()
        self.assertEqual(team_taiwan.shape, (36, 7))
    def test_08_get_roster(self):
        roster_players = asgmt.get_roster("players")
        self.assertEqual(len(roster_players), 28)
        self.assertIn("CHEN Chieh-Hsien", roster_players)
        self.assertIn("CHIANG Kun-Yu", roster_players)
        self.assertIn("CHANG Yi", roster_players)
        roster_coaches = asgmt.get_roster("coaches")
        self.assertEqual(len(roster_coaches), 8)
        self.assertIn("PENG Cheng-Min", roster_coaches)
        self.assertIn("TSENG Hao-Jiu", roster_coaches)
        self.assertIn("WANG Chien-Ming", roster_coaches)
    def test_09_get_information(self):
        self.assertEqual(asgmt.get_information(24), ('CHEN Chieh-Hsien', 'OF', 'L/R', 173.0, 73.0, 1994.0))
        self.assertEqual(asgmt.get_information(45), ('LIN Yu-Min', 'P', 'L/L', 180.0, 82.0, 2003.0))
        self.assertEqual(asgmt.get_information(27), ('LIN Chia-Cheng', 'C', 'R/R', 185.0, 91.0, 1997.0))
        self.assertEqual(asgmt.get_information(35), ('PAN Chieh-Kai', 'IF', 'L/R', 184.0, 78.0, 1994.0))
        self.assertEqual(asgmt.get_information(40), ('WANG Chien-Ming', 'Pitching Coach'))
        self.assertEqual(asgmt.get_information(23), ('PENG Cheng-Min', 'Coach'))
    def test_10_DataframeAttrs(self):
        movies = asgmt.import_movies_csv()
        dfa = asgmt.DataframeAttrs(movies)
        self.assertEqual(dfa.get_shape(), (250, 5))
        self.assertEqual(dfa.get_dtypes().size, 5)
        self.assertEqual(dfa.get_summary().shape, (8, 4))
        team_taiwan = asgmt.import_team_taiwan()
        dfa = asgmt.DataframeAttrs(team_taiwan)
        self.assertEqual(dfa.get_shape(), (36, 7))
        self.assertEqual(dfa.get_dtypes().size, 7)
        self.assertEqual(dfa.get_summary().shape, (8, 4))

asgmt = importlib.import_module("asgmt")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentSix)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))