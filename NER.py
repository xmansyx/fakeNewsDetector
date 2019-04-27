
# coding: utf-8

# In[11]:


import nltk
from nltk import ne_chunk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag



def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent




ex = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'
sent = preprocess(ex)
sent




pattern = 'NP: {<DT>?<JJ>*<NN>}'




cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
print(cs)




from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint

iob_tagged = tree2conlltags(cs)
pprint(iob_tagged[:][:])

