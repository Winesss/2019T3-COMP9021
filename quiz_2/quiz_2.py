# COMP9021 19T3 - Rachid Hamadi
# Quiz 2 *** Due Thursday Week 3


import sys
from random import seed, randrange
from pprint import pprint

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}

# cycles
def orderAndDuplicate(list):
    list_ = []
    for i in list:
        index = i.index(min(i))
        for x in range(index):
            i.insert(len(i), i[0])
            i.remove(i[0])
    for i in list:
        if i not in list_:
            list_.append(i)
    def takeFirst(list):
            return list[0]
    list_.sort(key=takeFirst)
    return list_

for key in mapping:
    list_1=[key]
    list_2=[]
    list_3=[]
    i=0
    list_4=[]
    list_5=[]
    value_n=mapping.get(key)
    while i<= len(mapping):
        if value_n == key:
            if i==0:
                cycles.append(list(list_1))
            else:
                list_1.extend(list_2)
                list_3.append(list_1)
                list_4=orderAndDuplicate(list_3)
                list_5=orderAndDuplicate(cycles)
                for i in list_4:
                    if i not in list_5:
                        cycles.append(i)
            break
        key_n = value_n
        value_n=mapping.get(key_n,None)
        i+=1
        list_2.append(key_n)

#reversed dictionary per lengths
for key in mapping:
    list_1 = list(mapping.values())
    list_2 = list(mapping.keys())
    dic_1 = {}
    dic_2={}
    i = 1
    list_3 = [key]
    value_n=mapping.get(key)
    while i<=len(mapping):
        list_1[list_2.index(key)]=None
        if value_n in list_1:
            n=list_2[list_1.index(value_n)]
            list_3.append(n)
            i+=1
            list_1[list_1.index(value_n)] = None
        else:
            list_3.sort()
            dic_1[value_n] = list_3
            break
    if not i in reversed_dict_per_length.keys():
        reversed_dict_per_length[i] = dic_1
    else:
        reversed_dict_per_length[i][value_n]=list_3



print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)


