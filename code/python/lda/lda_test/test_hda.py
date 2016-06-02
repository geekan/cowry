from gensim import corpora, models

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')
corpus_tfidf = corpora.MmCorpus('/tmp/deerwester.mm')

model = models.HdpModel(corpus_tfidf, id2word=dictionary)
# corpus_lsi = model[corpus_tfidf]
model.print_topics()