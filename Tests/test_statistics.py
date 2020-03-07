import unittest
from numpy.random import seed
from numpy.random import randint
from Statistics.Statistics import Statistics
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = [0,0,0,5,5,7,21,5]
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 5.375)

    def test_mode_calculator(self):
        mode = self.statistics.mode(self.testData)
        self.assertEqual(mode, 0)

    def test_median_calculator(self):
        median = self.statistics.mode(self.testData)
        self.assertEqual(median, 5)


if __name__ == '__main__':
    unittest.main()
