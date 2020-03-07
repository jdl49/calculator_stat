from numpy.random import seed
import random


class random_float:

    @staticmethod
    def list_Of_Floats(data, length, theSeed):
        aList = []
        seed(theSeed)

        for each in range(length):
            number = random.uniform(data, length)
            aList.append(number)

        return aList
