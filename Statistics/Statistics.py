from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Mode import mode
from Statistics.Median import median
from Statistics.Variance import variance
from Statistics.Standard_Deviation import standard_deviation
from Statistics.Z_score import z_scores
from Statistics.Mean_Deviation import MeanDeviation
from Statistics.PopulationProportion import PopulationProportion
from Statistics.Quartiles import quartile
from Statistics.Skewness import skew
from Statistics.Sample_Correlation import correlate


class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def standard_deviation(self, data):
        self.result = standard_deviation(data)
        return self.result

    def quartile(self, data):
        self.result = quartile(data)
        return self.result

    def skew(self, data):
        self.result = skew(data)
        return self.result

    def correlate(self, data, ydata):
        self.result = correlate(data, ydata)
        return self.result

    def z_scores(self, data):
        self.result = z_scores(data)
        return self.result


'''    
    def MeanDeviation(self, data):
        self.result = MeanDeviation(data)
        return self.result

    def PopulationProportion(self, data):
        self.result = PopulationProportion(data, lstLen, seed)
        return self.result
'''
