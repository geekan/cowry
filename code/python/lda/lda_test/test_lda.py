from gensim import corpora, models

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')
corpus_tfidf = corpora.MmCorpus('/tmp/deerwester.mm')

num_topic = 100
model = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=num_topic)
# corpus_lsi = model[corpus_tfidf]
model.print_topics(num_topic)

model.save('/tmp/test_lda.mm')