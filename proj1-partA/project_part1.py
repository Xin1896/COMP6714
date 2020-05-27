## Import Libraries and Modules here...
import itertools
import math
import pickle
from collections import defaultdict,Counter
import collections
import copy
import spacy
import re
from spacy.lang.en.stop_words import STOP_WORDS


class InvertedIndex:
    def __init__(self):
        ## You should use these variable to store the term frequencies for tokens and entities...
        self.tf_tokens = defaultdict(dict)
        self.tf_entities = defaultdict(dict)

        ## You should use these variable to store the inverse document frequencies for tokens and entities...
        self.idf_tokens = {}
        self.idf_entities = {}

    ## Your implementation for indexing the documents...
    def index_documents(self, documents):
        total_doc_num = len(documents)
        for k,v in documents.items():
            nlp = spacy.load("en_core_web_sm")
            doc = nlp(v)
            tokens = []
            single_entity = []
            for token in doc:
                if token.is_stop != True and token.is_punct != True:
                    tokens.append(token.text)
            for key in doc.ents:
                if (len(key.text.split()) == 1):
                    single_entity.append(key.text)
                if k not in self.tf_entities[key.text]:
                    self.tf_entities[key.text][k] = 1
                else:
                    self.tf_entities[key.text][k] += 1
            for i in single_entity:
                if i in tokens:
                    tokens.remove(i)
            counter1 = Counter(tokens)
            token_count = dict(counter1)
            for m in token_count:
                if m not in self.tf_tokens.keys():
                    self.tf_tokens[m] = {k:1.0 + math.log(1.0 + math.log(token_count[m]))}
                else:
                    self.tf_tokens[m][k] = 1.0 + math.log(1.0 + math.log(token_count[m]))             
        for i in self.tf_tokens.keys():
            # token idf
            doc_contain_t = len(self.tf_tokens[i])
            self.idf_tokens[i] = 1.0 + math.log(total_doc_num/(1.0 + doc_contain_t))
        for i in self.tf_entities.keys():
            # token idf
            doc_contain_e = len(self.tf_entities[i])
            self.idf_entities[i] = 1.0 + math.log(total_doc_num/(1.0 + doc_contain_e))     
    
    ## Your implementation to split the query to tokens and entities...
    def split_query(self, Q, DoE):
        tokens = Q.split()
        subset_of_doe = []
        DoE_list = list(DoE.keys())
        for i in DoE_list:
            word_split = i.split()
            string = '[0-9a-zA-Z\\s]+'.join(word_split)
            if re.search(string,Q):
                subset_of_doe.append(i)
        combination_of_subset = []
        splits = []
        for L in range(0, len(subset_of_doe)+1):
            for subset in itertools.combinations(subset_of_doe, L):
                combination_of_subset.append(list(subset))
        for i in combination_of_subset:
            n = []
            token_list = copy.deepcopy(tokens)
            if i != []:
                for j in i:
                    n += j.split()
                for k in n:
                    if k in token_list:
                        token_list.remove(k)
                    else:
                        break
                else:
                    splits.append((i,token_list))
            else:
                splits.append((i,token_list))
        return splits
    ## Your implementation to return the max score among all the query splits...
    def max_score_query(self, query_splits, doc_id):
        result = []
        for i in query_splits:
            s1 = 0.0
            s2 = 0.0
            for j in i[1]:
                if doc_id in self.tf_tokens[j].keys():
                    s1 += self.tf_tokens[j][doc_id] * self.idf_tokens[j]
            if i[0] == []:
                    s2 = 0.0
            else:
                for e in i[0]:
                    if doc_id in self.tf_entities[e].keys():
                        s2 += ((1.0 + math.log(self.tf_entities[e][doc_id])) * self.idf_entities[e])
            result.append(s2 + 0.4*s1)
        result_dict = {}
        max_score = max(result)
        index = result.index(max_score)
        result_dict['tokens'] = query_splits[index][1]
        result_dict['entities'] = query_splits[index][0]
        return (max_score,result_dict) 
