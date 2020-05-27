import pickle
import project_part1 as project_part1
#fname = './Data/test_500docs.pickle'
#documents = pickle.load(open(fname,"rb"))

documents = {1: 'According to Times of India, President Donald Trump was on his way to New York City after his address at UNGA.',
             2: 'The New York Times mentioned an interesting story about Trump.',
             3: 'I think it would be great if I can travel to New York this summer to see Trump.'}

#documents = {1:'Donald Trump, Donald Trump, Trump.'}
index = project_part1.InvertedIndex()

index.index_documents(documents)
#print(index.tf_tokens)
#print(index.tf_entities)
#print(index.idf_tokens)
#print(index.idf_entities)

Q = 'The New New York City Times of India'
DoE = {'Times of India':0, 'The New York Times':1,'New York City':2}

doc_id = 1
query_splits = index.split_query(Q, DoE)

#print('Possible query splits:\n',query_splits)


#print('Score for each query split:\n')
result = index.max_score_query(query_splits, doc_id)
print(result)
