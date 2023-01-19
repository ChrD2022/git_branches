import unittest

from src.high_scores import latest, personal_best, personal_top_three, high_to_low_scores

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests
    def setUp(self):
        self.score_list = [5, 1, 3, 3, 3, 2, 4]

    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        self.assertEqual(4, latest(self.score_list))

    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        self.assertEqual(5, personal_best(self.score_list))

    # Test top three from list of scores
    def test_top_three_scores_return(self):
        self.assertEqual([5, 4, 3], personal_top_three(self.score_list))

    # Test ordered from highest to lowest
    def test_scores_high_to_low(self):
        self.assertEqual([5, 4, 3, 3, 3, 2, 1], high_to_low_scores(self.score_list))

    # Test top three when there is a tie
    def test_there_is_a_top_3_tie(self):
        self.assertEqual()


    # Test top three when there are less than three


    # Test top three when there is only one
    
