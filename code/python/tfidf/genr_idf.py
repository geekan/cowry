

import jieba
import jieba.analyse
import psu

files = psu.ls()

files = filter(lambda x: x.endswith('txt'), files)

data = ''
for file in files:
    with open (file, "r") as myfile:
        d=myfile.read().replace('\n', '')
        data += d

tags = jieba.analyse.extract_tags(data, topK=100000, withWeight=True)
print(len(tags))


with open('idf', 'a') as f:
    for tag in tags:
        try:
            f.write(tag[0] + ' ' + str(tag[1]) + '\n')
        except:
            pass

import pdb;pdb.set_trace()


print('exit')

