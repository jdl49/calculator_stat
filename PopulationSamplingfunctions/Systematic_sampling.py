from Calculator.Division import division
from Calculator.Subtraction import subtraction
from RandomNum.N_numbers_from_list_seed import PickNumbersSeed

class SystemicSample():
    @staticmethod
    def systemicSample(aLst):
        lenLst = len(aLst)
        num = (PickNumbersSeed.pickNumbers(lenLst, lenLst, 2))
        nNum = round(division(num, 4))

        if nNum == 1:
            n =3

        sample = []
        temp = subtraction(nNum, 1)

        while temp <= subtraction(lenLst, 1):
            val = aLst[temp]
            sample.append(val)
            temp += nNum

        return sample