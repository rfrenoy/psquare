import unittest
import numpy as np
from psquare.psquare import PSquare


class TestPSquare(unittest.TestCase):

    def init_test_psquare(self):
        obs = [1, 2, 3, 4, 5]
        psquare = PSquare(0.5)
        for o in obs:
            psquare.update(o)
        return psquare

    def test_find_cell_should_return_neg_one_when_new_obs_is_lower_than_first_marker_height(self):
        # Given
        psquare = self.init_test_psquare()

        # When
        i = psquare.find_cell(0)

        # Then
        self.assertEqual(i, -1)

    def test_find_cell_should_return_max_index_when_new_obs_is_greater_than_last_marker_height(self):
        # Given
        psquare = self.init_test_psquare()

        # When
        i = psquare.find_cell(7)

        # Then
        self.assertEqual(i, 4)

    def test_find_cell_should_return_higher_marker_value_which_is_less_or_equal_than_input_value(self):
        # Given
        psquare = self.init_test_psquare()

        # When
        i = psquare.find_cell(4)
        j = psquare.find_cell(3.5)

        # Then
        self.assertEqual(3, i)
        self.assertEqual(2, j)

    def test_psquare_should_match_baseline_function(self):
        # Given
        examples = np.random.normal(loc=500, scale=100, size=1000)
        p = 0.9
        base_p_est = np.percentile(examples, p * 100)

        # When
        psquare = PSquare(p)
        for obs in examples:
            psquare.update(obs)
        p_est = psquare.p_estimate()

        # Then
        self.assertLess(np.abs(base_p_est - p_est), 10)
