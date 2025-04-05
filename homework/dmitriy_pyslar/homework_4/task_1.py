my_dict = {
    'tuple': (1, 'two', True, 15.2, None),
    'list': [None, False, 2.15, 'four', 5],
    'dict': {'true': True, 1: 15, False: 'false', (2,1): (1,2), 'intro_list': [3,2,1]},
    'set': {False, True, 123, 123.45, 'multiset'}
}

print(my_dict['tuple'][-1])

my_dict['list'].append('last element')
my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = ('i', 'am', 'a', 'tuple')
my_dict['dict'].pop('true')

my_dict['set'].add(12)
my_dict['set'].discard('multiset')

print(my_dict)