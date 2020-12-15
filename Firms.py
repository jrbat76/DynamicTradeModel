import random
import pandas as pd
from numpy.random import zipf

class Presentation:
    '''this class used to create presentation for Melitz paper'''
    tfp = 2
    capital = 2
    alpha = 0.6

    def __init__(self, name = ' ', num_firms = 0, firm_dict = None, entrance_cost=0):
        self.num_firms = num_firms
        self.name = name
        self.entrance_cost = entrance_cost

    def get_firm_dict(self):
        return self.firm_dict

    def create_zipf_firm(self):
        ref = {}
        random.seed()
        x = zipf(a=4, size=self.num_firms)
        ref[self.name] = x
        return ref

    def cobb_douglas(self, labors):
        tfp = Presentation.tfp
        capital = Presentation.capital
        alpha = Presentation.alpha
        ref = {}
        for keys, values in labors.items():
            sum1 = sum(values)
            for ind, each in enumerate(values):
                distribution = each / sum1
                cobb_douglas = tfp * capital ** (alpha) * each ** (1 - alpha)
                ref[ind] = {'ID': keys + str(ind), 'labor': each, 'productivity': cobb_douglas,
                             'distribution': distribution, 'entrance_cost': self.entrance_cost}
                self.firm_dict = ref
        return self.firm_dict

    def export_firms(self, industry, keyword=None):
        export = {}
        for keys, values in industry.items():
            for sub_keys, sub_values in values.items():
                if sub_keys == keyword and sub_values > self.entrance_cost:
                    export[keys] = values
                else:
                    pass
        return export

    def reallocate(self, dataframe, newColname=None, colname=None):

        ls = []
        toList = dataframe[colname].to_list()
        sum1 = sum(toList)
        for each in toList:
            norm = each / sum1
            ls.append(norm)
        dataframe[newColname] = ls
        return dataframe
'''
def main():
    higher = pd.read_csv('/Users/bbjnn/Desktop/country_codes/income_level.csv')
    #print(higher.columns)
    high_income = higher[higher.IncomeLevel == 'higher']
    world = random.sample(high_income.Country_Code.to_list(), 15)
    #print(world)
    num_firms = 15000
    #rand_cost = random.sample(range(15, 25), len(world))
    #print(rand_cost)
    res = [random.randrange(5, 10, 1) for i in range(len(world))]
    world_zipped = dict(zip(world, res))
    #print(zipped)
    #for k, v in world_zipped.items():
    #    print(k, v)

    world_export_firms = []
    world_trade = []
    for nation, cost in world_zipped.items():
        p1 = Presentation(nation, num_firms, entrance_cost=cost)
        zipf_firms = p1.create_zipf_firm()
        before_rand_cost = p1.cobb_douglas(zipf_firms)
        #print(pd.DataFrame(before_rand_cost).T)
        world_export_firms.append(before_rand_cost)

    distr = []
    for i in world_export_firms:
        each = p1.export_firms(i, keyword='productivity')
        if len(pd.DataFrame(each).T) == 0:
            pass
        else:
            distr.append(pd.DataFrame(each).T)
    #print(distr)

    for i in distr:
        #multinationals = pd.DataFrame(i)
        #print(i)
        world_rellocated = p1.reallocate(i, 'newDistribution', 'distribution')
        print(world_rellocated)
        #world_trade.append(world_rellocated)

    #for each in world_trade:
    #    print(each)

if __name__ == '__main__':
    main()
'''
