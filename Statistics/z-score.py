from Statistics.Mean import mean
from Statistics.Deci import decimalize
from Statistics.Standard_Deviation import standard_deviation


def z_scores(data, sample=True):
    if type(data) is int:
        return None
    elif type(data) is list:
        # You can't get z scores for one number
        if len(data) < 2:
            return None

        mean_of_data = decimalize(mean(data))
        sd_of_data = decimalize(standard_deviation(data, sample))

        scores = [float((mean_of_data - ii) / sd_of_data) for ii in data]
        return scores
