import pandas as pd
import random

class Middle:
    '''this is the class for Developed country firms'''
    def __init__(self):
        data = pd.read_csv('income_level.csv')
        up_middle_income = data[data.IncomeLevel == 'upper middle']
        self.up_middle_income = up_middle_income

    def getMiddle(self):
        return self.up_middle_income

    def gen_RandomMINations(self, num_nations=0):
        random.seed(101)
        middle = random.sample(self.up_middle_income.Country_Code.to_list(), num_nations)
        res = [random.randrange(5, 10, 1) for i in range(len(middle))]
        zipped = dict(zip(middle, res))
        return zipped

'''
def test():
    m1 = Middle()
    num_nations = 15
    middle = m1.getMiddle()
    middle_rand = m1.gen_RandomMINations(num_nations)
    print(middle_rand)

if __name__ == '__main__':
    test()
'''
