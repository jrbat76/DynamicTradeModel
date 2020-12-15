#from Firms import Firms
import pandas as pd
import random

class Developed:
    ''' this is the class for Developed country firms'''
    def __init__(self):
        data = pd.read_csv('income_level.csv')
        high_income = data[data.IncomeLevel == 'higher']
        self.high_income = high_income

    def getHigher(self):
        return self.high_income

    def gen_RandomHINations(self, num_nations=0):
        random.seed(101)
        world = random.sample(self.high_income.Country_Code.to_list(), num_nations)
        res = [random.randrange(10, 15, 1) for i in range(len(world))]
        zipped = dict(zip(world, res))
        #print(zipped)
        return zipped
