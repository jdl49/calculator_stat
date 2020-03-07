import unittest
from random import seed
from numpy.random import randint
import pprint

from RandomNum.random_no_seed import RandomNoSeed
from RandomNum.random_seed import RandomSeed
from RandomNum.random_list import RandomList
from RandomNum.pickRandom import PickRandomly
from RandomNum.pickSeed import PickSeed
from RandomNum.N_numbers_from_list import PickNumbersNoSeed
from RandomNum.N_numbers_from_list_seed import PickNumbersSeed




class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.mySeed = seed(3)
        #self.setNumber = randint(1,10)
        self.aList = randint(0, 3,10)
        #pprint.pprint(self.aList)

    def test_Random_No_Seed_Int(self):
        result = RandomNoSeed.randomInt(0, 10)
        self.assertEqual(isinstance(result, int), True)

    def test_Random_No_Seed_Float(self):
        result = RandomNoSeed.randomFloat(0, 10)
        self.assertEqual(isinstance(result, float), True)

    def test_Random_Seed_Int(self):

        result = RandomSeed.randomInt(3, 0, 10)
        result2 = RandomSeed.randomInt(3, 0, 10)




        self.assertEqual(result, result2)
    def test_Random_Seed_Float(self):
        result = RandomSeed.randomFloat(3, 0, 10)
        result2 = RandomSeed.randomFloat(3, 0, 10)
        self.assertEqual(result, result2)


    def test_Make_List_Ints(self):
        result = RandomList.list_Of_Ints(0, 10, 10)
        self.assertEqual(result, [3, 9, 8, 2, 5, 9, 7, 10, 9, 1])

    def test_Make_List_Floats(self):
        result = RandomList.list_Of_Floats(0, 10, 10)
        self.assertEqual(result, [2.3796462709189137, 5.442292252959518, 3.6995516654807927, 6.039200385961944, 6.25720304108054,
                                  0.6552885923981311, 0.13167991554874137, 8.3746908209646, 2.5935401432800766, 2.3433096104669637])

    def test_Pick_Random_Number(self):
        myList = RandomList.list_Of_Ints(0, 10, 10)
        result = PickRandomly.pick(myList)
        #pprint.pprint(result)
        self.assertEqual(result, 1)

    def test_Pick_Number_With_Seed(self):
        myList = RandomList.list_Of_Ints(0, 10, 10)
        result = PickSeed.pickSeed(3, myList)
        self.assertEqual(result, 2)

    def test_N_numbers_from_List(self):
        myList = RandomList.list_Of_Ints(0, 10, 10)
        result = PickNumbersNoSeed.pickNumbers(myList, 5)
        self.assertEqual(result, [1, 3, 10, 5, 9])

    def test_N_numbers_from_list_seed(self):
        myList = RandomList.list_Of_Ints(0, 10, 10)
        result = PickNumbersSeed.pickNumbers(3, myList, 5)
        self.assertEqual(result, [2, 1, 9, 8, 9])





if __name__ == '__main__':
    unittest.main()
