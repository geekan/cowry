# -*- coding: utf-8 -*-

import csv
import json
import jieba
import jieba.analyse
import sys
import os.path

import pprint

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class MyPrettyPrinter(pprint.PrettyPrinter):
    def format(self, object, context, maxlevels, level):
        if isinstance(object, unicode):
            return (object.encode('utf8'), True, False)
        return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)


p = MyPrettyPrinter(indent=1, width=80, depth=6)


class DocDetail:
    def __init__(self, title='', title_seg=None, title_tag=None, title_tf_idf=None):
        self.title = title
        self.title_seg = title_seg
        self.title_tag = title_tag
        self.title_tf_idf = title_tf_idf

reload(sys)
sys.setdefaultencoding('utf-8')
csv.field_size_limit(sys.maxsize)

from gensim import corpora, models, similarities

with open(os.path.dirname(__file__) + '/url_info_large.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# cols = dict((v, k) for k, v in enumerate(data[0]))
cols = dict((v, k) for k, v in enumerate(data[0]))

# print(cols)

titles = []
documents = []

doc_details = {}
bad_words = {u'一个', u'什么', u'这些', u'这样', u'知道', u'这个', u'为什么',
             u'如何', u'这么', u'原来', u'男子', u'女子', u'真的', u'怎么', u'自己',
             u'居然', u'震惊', u'他们', u'不要', u'就是', u'为何',
             u'不是', u'可以', u'到底', u'一定', u'最后', u'可能',
             u'已经', u'一生', u'以上', u'不止', u'想起', u'力挺',
             u'原因', u'不仅', u'了解', u'简单', u'表现', u'结果',
             u'以后', u'影响', u'没有', u'看到', u'千万', u'多少',
             u'那么', u'今日', u'产品', u'最新', u'突然', u'惊呆',
             u'这种', u'终于', u'女人', u'所有', u'不会', u'开始',
             u'', u'', u'', u'', u'', u'',
             u'', u'', u'', u'', u'', u'',
             u'', u'', u'', u'', u'', u'',
             u'', u'', u'', u'', u'', u'',
             u'', u'', u'', u'', u'', u'',}

for l in data[1:]:
    # print(json.dumps(l, ensure_ascii=False))
    if not l[cols['topic_id']].startswith("109"):
        continue

    title = l[cols['title']]
    if title in titles:
        continue

    titles.append(title)

    raw_words = jieba.analyse.extract_tags(title, topK=5,
                                           allowPOS=('n', 'an', 'Ng', 'nr', 'nt', 'nz', 'vn'))
    # jieba.lcut(title, cut_all=False)
    words = filter(lambda x: x not in bad_words, raw_words)
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
# print(dictionary)
# print(dictionary.token2id)

# new_doc = "Human computer interaction"
# new_vec = dictionary.doc2bow(new_doc.lower().split())

corpus_tfidf = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus_tfidf)
print(corpus_tfidf[:10])


zip_data = zip(titles, documents, texts, corpus_tfidf)

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

corpus_tfidf = corpora.MmCorpus('/tmp/deerwester.mm')

print("")

tfidf = models.TfidfModel(corpus_tfidf)

vec = [(0, 1), (4, 1)]
# print(tfidf[vec])

print(corpus_tfidf[0])
print(corpus_tfidf[-1])

from sim import print_similaries

num_topic = 250
lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=num_topic,
                      update_every=0, passes=20)
lda.print_topics(num_topic)

tfidf_index = similarities.SparseMatrixSimilarity(tfidf[corpus_tfidf], num_features=len(tfidf.dfs))
lda_index = similarities.MatrixSimilarity(lda[corpus_tfidf])

print_similaries(tfidf, corpus_tfidf, zip_data, tfidf_index)
print_similaries(lda, corpus_tfidf, zip_data, lda_index)


# num_topic = 10
# lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topic)
# corpus_lsi = lsi[corpus_tfidf]
# lsi.print_topics(num_topic)
