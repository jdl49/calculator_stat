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
        median = self.statistics.median(self.testData)
        self.assertEqual(median, 5)

    def test_variance_calculator(self):
        variance = self.statistics.variance(self.testData)
        self.assertEqual(variance, 47.69642857142857)

    def test_standard_deviation_calculator(self):
        standard_deviation = self.statistics.standard_deviation(self.testData)
        self.assertEqual(standard_deviation, 6.906260100186538)

    def test_quartile_calculator(self):
        quartile = self.statistics.quartile(self.testData)
        self.assertEqual(quartile, [0, 0, 5, 5, 21])

    def test_skew_calculator(self):
        skew = self.statistics.skew(self.testData)
        self.assertEqual(skew, 1.554528469606428)

    def test_correlate_calculator(self):
        correlate = self.statistics.correlate(self.testData)
        self.assertEqual(correlate, 5)

    #def test_z_scores_calculator(self):
     #   z_scores = self.statistics.z_scores(self.testData)
      #  self.assertEqual(z_scores, [0.7782794047757948, 0.778279404775794, 0.7782794047757948, 0.7782794047757948, 0.7782794047757948, 0.05429856312389266, 0.05429856312389266, -0.2352937735368682, -2.262440130162194, 0.05429856312389266])

if __name__ == '__main__':
    unittest.main()
