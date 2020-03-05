from RandomNum.random_list import RandomList
from numpy.random import seed

class RandomSample():
    @staticmethod
    def random_sample(seed_, data, lstLen):
        seed(seed_)
        return RandomList.list_Of_Ints(data, lstLen, seed)