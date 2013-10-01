# -*- coding: gbk -*-

import re
import os.path
import threading
import time

try:
    import urllib.request
    #import urllib.parse
except ImportError:
    import urllib
    urllib.request = __import__('urllib2')
    urllib.parse = __import__('urlparse')

urlopen = urllib.request.urlopen
request = urllib.request.Request

'''
try:
    input = raw_input
except NameError:
    pass

host = input('input target ip:')
'''

host = '38.103.161.147'
base_url = 'http://' + host + '/forum/'
http_proxy = "http://localhost:8086"
use_proxy = True
http_proxys = {'http':http_proxy}
wtfdir = 'test'
mode = 'see' # see, down
analytics_file = 'test.txt'
forum_ids = {'YM' : 230, 'WM' : 143}

text_order = ['star','url','title','comment','view','time']

def get_valid_filename(filename):
    keepcharacters = (' ','.','_')
    return "".join(c for c in filename if c.isalnum() or c in keepcharacters).rstrip()

def get_data_from_req(req):
    attempts = 0
    binary = ''
    while attempts < 10:
        try:
            binary = urlopen(req).read()
            break
        except Exception as e:
            attempts += 1
            print(e)
    return binary
    

def get_content_from_url(url):
    attempts = 0
    content = ''
    while attempts < 10:
        try:
            content = urlopen(url).read().decode('gbk', 'ignore')
            break
        except Exception as e:
            attempts += 1
            print(e)
    return content

def down_link(url, filename, thresold = 0):
    if os.path.exists(filename) and os.path.getsize(filename) > 0: #TODO MD5
        return
    #filename = get_valid_filename(filename)
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:22.0) Gecko/20100101 Firefox/22.0'}
    req = request(url, headers = headers)
    try:
        data = get_data_from_req(req)
        if data is '':
            return
        f = open(filename, 'wb')
        f.write(data)
        f.close
    except Exception as e:
        print(e)
    return

def down_imgs_from_url(url):
    content = get_content_from_url(url)
    #p = 'postmessage.*?(img src=\"([^\"]+?jpg).*?)postinfo postactions'
    #p2 = 'postmessage.*?img src=\"(http[^\"]+?)\".*?postactions'
    #p3 = 'postmessage(.*?)postactions'
    #i = re.findall(p3, content, re.M | re.S)
    #ix = re.findall(p1, str(i), re.M | re.S)
    dirname = 'tmp1'
    os.makedirs(dirname, exist_ok = True)
    imgs = re.findall('img src=\"(http[^\"]+)\"', content, re.M | re.S)
    torrents = re.findall('a href=\"(?P<url>attach[=0-9a-zA-Z\.\?]+).*?>(?P<title>[^<>\"]*?torrent)', content, re.M | re.S)
    
    imgs = set(imgs)
    torrent_set = set(torrents)
    print(imgs, torrent_set)
    for img in imgs:
        down_link(img, dirname + '/' + get_valid_filename(os.path.basename(img)))
    for torrent in torrent_set:
        down_link(base_url + torrent[0], dirname + '/' + get_valid_filename(torrent[1]))

    return

def down_link_imgs_torrents(topic):
    print('GET:', topic)
    dirname = get_valid_filename(topic['title'])
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    
    content = get_content_from_url(topic['url'])

    imgs = re.findall('img src=\"(http[^\"]+)\"', content, re.M | re.S)
    torrents = re.findall('a href=\"(?P<url>attach[=0-9a-zA-Z\.\?]+).*?>(?P<title>[^<>\"]*?torrent)', content, re.M | re.S)
    
    imgs = set(imgs)
    st = set(torrents)
    #t = re.findall('a href=\"attach.*?torrent', content, re.M | re.S)
    #t = re.findall('a href=\"(?P<torrent>attach[=0-9a-zA-Z\.\?]+).*?>(.*?torrent)', content, re.M | re.S)
    
    print(imgs, st)
    for img in imgs:
        down_link(img, dirname + '/' + os.path.basename(img))
    for t in st:
        down_link(base_url + t[0], dirname + '/' + t[1])

    return

def get_links_from_page(url):
    print('GET:' + url)
    
    content = get_content_from_url(url)
    if content == '':
        return
    #print(content)
    attempts = 0
    while attempts < 3:
        topics_html = re.findall('<tbody.*?normalthread.*?>.*?</tbody>', content, re.M | re.S)
        if topics_html == '':
            attempts += 1 # need retry download
        else:
            break
    #print(topics_html)
    topics = dict()
    # GET: 1-url 2-title 3-star 4-comment 5-view 6-time
    p = '<span id.*?<a href=\"(?P<url>.*?)\".*?>(?P<title>.*?)</a>.*?<img.*?<td.*?author.*?img.*?>.*?(?P<star>\d+).*?</cite>.*?<td.*?nums\">.*?(?P<comment>\d+).*?<em>(?P<view>\d+).*?lastpost.*?<a href.*?>(?P<time>.*?)</a>'
    
    try:
        for h in topics_html:
            gd = re.search(p, h, re.M | re.S).groupdict()
            gd['url'] = base_url + gd['url']
            topic_index = gd['title']
            topics[topic_index] = gd
            print(topics[topic_index])
    except Exception as e:
        print(e)
    
    if mode is 'down':
        for i in topics:
            down_link_imgs_torrents(topics[i])

    return topics

def install_proxy():
    if use_proxy == False:
        return
    proxy_support = urllib.request.ProxyHandler({"http":http_proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    return

class ThreadUrl(threading.Thread):
    url_base = forum_id = begin = end = None
    def __init__(self, url_base, forum_id, begin, end):
        threading.Thread.__init__(self)
        self.url_base = url_base
        self.forum_id = forum_id
        self.begin = begin
        self.end = end

    def run(self):
        for i in range(self.begin, self.end):
            url = self.url_base.format(self.forum_id, i)
            get_links_from_page(url)

def test_main():
    install_proxy()
    
    url = base_url + 'thread-4917240-1-1.html'
    down_imgs_from_url(url)

def down_imgs_torrents():
    install_proxy()
    base_forum_url = base_url + 'forum-{0}-{1}.html'
    
    forum_ids = {'YM' : 230, 'WM' : 143}
    #urls = map(base_forum_url.format, forum_ids.values())

    if not os.path.exists(wtfdir):
        os.makedirs(wtfdir)
    os.chdir(wtfdir)
    end = 0
    t = dict()
    pages = range(5,40,5)
    for forum_id in forum_ids.values(): #or using thread
        for page in pages:
            begin = end + 1
            end = page
            #t = ThreadUrl(base_forum_url.format(forum_id, page))
            t[forum_id,page] = ThreadUrl(base_forum_url, forum_id, begin, end)
            t[forum_id,page].start()

    for forum_id in forum_ids.values(): #or using thread
        for page in pages:
            t[forum_id,page].join()

def write_topic_list_to_file(topic_list, filename = 'test.txt'):
    f = open(filename, 'wb')
    #binary = str(topic_list).encode('utf8')
    for topic in topic_list: # topic is a dict
        for key in text_order:
            value = topic[key]
            binary = (str(value) + ',').encode('utf8')
            f.write(binary)
        f.write('\n'.encode('utf8'))
    

def down_topics_and_store(forum):
    install_proxy()
    base_forum_url = base_url + 'forum-{0}-{1}.html'
    #base_forum_url.format(forum_id, page)
    topics = dict();
    
    for page in range(1,1024):
        topics.update(get_links_from_page(base_forum_url.format(forum, page)))

    topic_list = list()
    #topic_list = sorted(list(topics), key=lambda topic: topic['star'])
    for value in topics.values():
        temp = value
        topic_list.append(temp)
    topic_list.sort(key=lambda x: int(x['star']), reverse = True)
    write_topic_list_to_file(topic_list, filename = str(forum) + analytics_file)

    return 

class ThreadDownTopicsAnalytics(threading.Thread):
    forum_id = None
    def __init__(self, forum_id):
        threading.Thread.__init__(self)
        self.forum_id = forum_id
    
    def run(self):
        down_topics_and_store(self.forum_id)

def get_all_analytics():
    f1 = ThreadDownTopicsAnalytics(forum_ids['YM'])
    f2 = ThreadDownTopicsAnalytics(forum_ids['WM'])
    f1.start()
    f2.start()
    

def main():
    #down_imgs_torrents()
    # 下载所有topics，排序，输入文件
    get_all_analytics()

start = time.time()
if __name__ == '__main__':
    main()

print("Elapsed Time:", (time.time() - start))