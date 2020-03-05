from Statistics.Z_score import z_scores
from PopulationSamplingfunctions.Margin_error import MarginError
from Statistics.PopulationProportion import PopulationProportion
from Calculator.Exponentiation import exponentiation
from Calculator.Subtraction import subtraction


class Cochran():
    @staticmethod
    def cochran(data, lstLen, seed):
        z_s = z_scores(data,seed)
        p_p = PopulationProportion.proportion(data, lstLen, seed)
        m_e = MarginError.margin(data, seed)
        q = subtraction(1, p_p)

        cochran = (exponentiation(z_s,2) * p_p * q)/exponentiation(m_e,2)

        return cochran