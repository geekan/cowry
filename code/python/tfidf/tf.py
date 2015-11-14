

import jieba
import jieba.analyse
import psu

data = ''
for file in ['2015-November.txt']:
    with open (file, "r") as myfile:
        d=myfile.read().replace('\n', '')
        data += d

tags_1 = jieba.analyse.extract_tags(data, topK=100, withWeight=True)
jieba.analyse.set_idf_path('./idf')
tags = jieba.analyse.extract_tags(data, topK=100, withWeight=True)
print(tags_1)
print('')
print(tags)


import pdb;pdb.set_trace()


print('exit')

