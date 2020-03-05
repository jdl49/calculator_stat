from Statistics.Standard_Deviation import standard_deviation
from Statistics.Z_score import z_scores
from Calculator.Multiplication import multiplication


class MarginError:
    @staticmethod
    def margin(data, seed):
        zs = z_scores(data, seed)
        sd = standard_deviation(data)
        margin = multiplication(zs, sd)
        return margin
