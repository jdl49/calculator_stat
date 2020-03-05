# How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)

from Calculator.SquareRoot import squareRoot
from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Statistics.Z_score import z_scores
from PopulationSamplingfunctions.Margin_error import MarginError


class UnknownPopulation:
    @staticmethod
    def unknown_pop_sample(data, seed, percent):
        z_s = z_scores(data, seed)
        m_e = MarginError.margin(data, seed)
        p = percent
        q = subtraction(1, p)

        val = division(z_s, m_e)
        samplePop = squareRoot(val) * p * q

        return samplePop
