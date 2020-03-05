# Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
from numpy.random import seed
from RandomNum.random_list_float import random_float
import random


class RandomList():


    @staticmethod
    def list_Of_Ints(data, length, theSeed):

        if isinstance(data, float):
            return random_float.list_Of_Floats(data, length, theSeed)

        aList = []
        seed(theSeed)

        for each in range(length):
            number = random.randint(data)
            aList.append(number)

        return aList