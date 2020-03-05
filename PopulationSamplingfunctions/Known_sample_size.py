# How to Find a Sample Size Given a Confidence Interval and Width (known population standard deviation)

from Calculator.SquareRoot import squareRoot
from Statistics.Z_score import z_scores
from Statistics.Standard_Deviation import standard_deviation
from PopulationSamplingfunctions.Margin_error import MarginError

class KnownPopulation():
    @staticmethod
    def known_pop_sample(data, seed):

        z_s = z_scores(data, seed)
        m_e = MarginError.margin(data, seed)
        s_d = standard_deviation(data)

        value = (z_s * s_d) / m_e

        popSample = squareRoot(value)

        return popSample