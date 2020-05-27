import itertools
import math
import pickle
from collections import defaultdict
from collections import Counter
import collections
import copy
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
documents = {1: 'According to Times of India, President Donald Trump was on his way to New York City after his address at UNGA.',
             2: 'The New York Times mentioned an interesting story about Trump.',
             3: 'I think it would be great if I can travel to New York this summer to see Trump.'}
tf_tokens = defaultdict(dict)
tf_entities = defaultdict(dict)
tokens_dict = {}
entities_dict = {}
for k,v in documents.items():
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(v)
    entities = []
    tokens = []
    for token in doc:
        if token.is_stop != True and token.is_punct != True:
            tokens.append(token)
    
    for ent in doc.ents:
        entities.append(ent)
        #counter = Counter(tokens)
        #dictionary=dict(counter)
        #print(dictionary)
    
    counter1 = Counter(tokens)
    counter2 = Counter(entities)
    token_count = dict(counter1)
    entity_count = dict(counter2)
    for key in entity_count:
        if key not in entities_dict:
            entities_dict[key] = {k:entity_count[key]}
        else:
            entities_dict[key][k] = entity_count[key]
print(entities_dict)
  

    
