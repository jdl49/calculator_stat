import random


# Integer and Decimal randomseed

class RandomSeed():
    @staticmethod
    def randomInt(theSeed, num1, num2):

        random.seed(theSeed)
        if isinstance(num1, float):
            return RandomSeed.randomFloat(theSeed, num1, num2)

        return random.randint(num1,num2)

    @staticmethod
    def randomFloat(theSeed, num1, num2):
        random.seed(theSeed)
        ranNum = random.uniform(num1, num2)

        return ranNum


