import pandas as pd
from Developed import Developed
from Middle import Middle
from Firms import Presentation

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

def main():

    num_firms = 1500000
    num_nations = 30
    
    d1 = Developed()
    high_income = d1.gen_RandomHINations(num_nations=num_nations)

    m1 = Middle()
    middle_income = m1.gen_RandomMINations(num_nations = num_nations)

    ind_economies = Merge(high_income, middle_income)
    exporting = []
    multinationals = []
    for ind, (keys, values) in enumerate(ind_economies.items()):
        #print(values)
        f1 = Presentation(name=keys, num_firms=num_firms, entrance_cost=values)
        zipf_firms = f1.create_zipf_firm()
        cobb_doug = f1.cobb_douglas(zipf_firms)
        #print(pd.DataFrame(cobb_doug).T)
        ex_firms = f1.export_firms(cobb_doug, keyword='labor')
        exporting.append(ex_firms)

    for each in exporting:
        sub_each = pd.DataFrame(each).T
        if len(sub_each) == 0:
            pass
        else:
            sub = f1.reallocate(sub_each, 'newDistribution', 'distribution')
            multinationals.append(sub)
    for i in multinationals:
        print('\n',i)

    #print(high_income)

if __name__ == '__main__':
    main()
