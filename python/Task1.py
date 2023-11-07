import random


def slt1(lst):
    dct = {}
    for x in lst:
        dct[x] = lst.count(x)
    print(dct)

def slt5(lst):
    dct = {}
    for x in lst:
        try:
            dct[x] += 1
        except:
            dct[x] = 1
    print(dct)

def get_dict_with_count(rng,vol):
    return [random.randrange(vol) for i in range(rng)]

lst1 = get_dict_with_count(1000, 10)
lst2 = get_dict_with_count(100000, 10)
lst3 = get_dict_with_count(100, 10)

slt1(lst1)
slt1(lst2)
slt1(lst3)
