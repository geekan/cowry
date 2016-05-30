# -*- coding: utf-8 -*-

import csv
import json
import jieba
import jieba.analyse
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from gensim import corpora, models, similarities

with open('/Users/wuchenglin/code/recsys/data/2016.5.4.url_info.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# cols = dict((v, k) for k, v in enumerate(data[0]))
cols = dict((v, k) for k, v in enumerate(data[0]))


# print(cols)


class DocDetail:
    def __init__(self, title='', title_seg=None, title_tag=None, title_tf_idf=None):
        self.title = title
        self.title_seg = title_seg
        self.title_tag = title_tag
        self.title_tf_idf = title_tf_idf


titles = []
documents = []

doc_details = {}

for l in data[1:1000]:
    # print(json.dumps(l, ensure_ascii=False))
    title = l[cols['title']]
    titles.append(title)
    words = jieba.lcut(title, cut_all=False)
    # print(' '.join(words))
    documents.append(words)

    doc_detail = DocDetail(title=title, title_seg=words)
    doc_details[title] = doc_detail

    # print(json.dumps(words, ensure_ascii=False))
    # print(json.dumps(jieba.analyse.extract_tags(title, topK=5, allowPOS=('ns', 'n', 'vn', 'v')), ensure_ascii=False))

from collections import defaultdict

frequency = defaultdict(int)

for text in documents:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if len(token) > 1]  # frequency[token] > 1 and
         for text in documents]

dictionary = corpora.Dictionary(texts)
dictionary.save('/tmp/deerwester.dict')
print(dictionary)
print(dictionary.token2id)

# new_doc = "Human computer interaction"
# new_vec = dictionary.doc2bow(new_doc.lower().split())

corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus)
print(corpus[:10])


zip_data = zip(titles, documents, texts, corpus)

# for id, t in enumerate(texts[:10]):
#     print(json.dumps(titles[id], ensure_ascii=False))
#     print(json.dumps(t, ensure_ascii=False))
#     print(corpus[id])

for (title, document, text, c) in zip_data[-10:]:
    print(json.dumps(title, ensure_ascii=False))
    print(json.dumps(document, ensure_ascii=False))
    print(json.dumps(text, ensure_ascii=False))
    print(c)

print("")

corpus = corpora.MmCorpus('/tmp/deerwester.mm')

print("")

tfidf = models.TfidfModel(corpus)
vec = [(0, 1), (4, 1)]
print(tfidf[vec])

index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=4286)
sims = index[tfidf[vec]]
print(list(enumerate(sims)))
