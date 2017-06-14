__author__ = 'arshad'

from collections import  defaultdict
import datetime

dict_of_lists = defaultdict(list)

dict_of_lists['a'].append(1)
dict_of_lists['a'].append(2)
print dict_of_lists

dict_of_dicts = defaultdict(dict)
#dict_of_dicts = {}
dict_of_dicts['a']['b'] = 1
dict_of_dicts['a']['c'] = 2
print  dict_of_dicts

defTime = datetime()
print type(defTime)