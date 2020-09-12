import unittest

from unittest import mock

from format_output import average_scores as topic2

class MyTestCase (unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect = [85, 90, 95]):
             assert topic2.average() == 90


