import itertools
import math
import pickle
from collections import defaultdict,Counter
import collections
import copy
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
Q = 'Los The Angeles Boston Times Globe Washington Post'
DoE = {'Los Angeles Times':0, 'The Boston Globe':1,'The Washington Post':2, 'Star Tribune':3}

tokens = Q.split()
#token list
counter = collections.Counter(tokens)
#token_count
token_dictionary=dict(counter)
subset_of_doe = []
DoE_list = list(DoE.keys())
for L in range(1, len(tokens)+1):
    for subset in itertools.combinations(tokens, L):
        string = ' '.join(list(subset))
        #print(string)
        if string in DoE_list:
            if string not in subset_of_doe:
                subset_of_doe.append(string)

combination_of_subset = []
for L in range(0, len(subset_of_doe)+1):
    for subset in itertools.combinations(subset_of_doe, L):
        combination_of_subset.append(list(subset))

entities = []
for i in combination_of_subset:
    n = []
    if i != []:
        for j in i:
            n += j.split()
        counter = collections.Counter(n)
        dictionary=dict(counter)
        if(all((k in token_dictionary and token_dictionary[k]>=v) for k,v in dictionary.items())):
            entities.append(i)
    else:
        entities.append(i)
splits = {}
count = 0
for e in entities:
    splits[count] = {}
    token_list = copy.deepcopy(tokens)
    n = []
    if e != []:
        for j in e:
            n += j.split()
        for item in n:
            token_list.remove(item)
        splits[count] = {'tokens':token_list}
    else:
            splits[count] = {'tokens':token_list}
    splits[count]['entities'] = e
    count += 1
return splits