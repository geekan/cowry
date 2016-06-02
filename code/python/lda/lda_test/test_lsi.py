from gensim import corpora, models, similarities

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')
corpus_tfidf = corpora.MmCorpus('/tmp/deerwester.mm')

num_topic = 300
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topic)
corpus_lsi = lsi[corpus_tfidf]
lsi.print_topics(num_topic)