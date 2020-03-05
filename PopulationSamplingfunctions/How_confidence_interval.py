from scipy.stats import sem
from scipy.stats import t
from PopulationSamplingfunctions.Confidence_interval import ConfidenceIntervalPopulation
from PopulationSamplingfunctions.Random_sampling import RandomSample

class ConfidenceIntervalSample():
    @staticmethod
    def confidenceInterval(confidence, data, seed, high):
        data = RandomSample.random_sample(seed, data, high)
        cip = ConfidenceIntervalPopulation.confidence_interval(confidence, data)
        return cip