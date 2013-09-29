# -*- coding: gbk -*-

import re
import os.path
import urllib.request
import threading
import time

urlopen = urllib.request.urlopen
request = urllib.request.Request

base_url = 'http://38.103.161.147/forum/'
http_proxy = "http://localhost:8086"
http_proxys = {'http':http_proxy}
download_dir = 'dl/'

def get_valid_filename(filename):
    keepcharacters = (' ','.','_')
    return "".join(c for c in filename if c.isalnum() or c in keepcharacters).rstrip()

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

def down_link(url, filename):
    if os.path.exists(filename): #TODO MD5
        return
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:22.0) Gecko/20100101 Firefox/22.0'}
    req = request(url, headers = headers)
    try:
        u = urlopen(req, timeout = 60)
        f = open(filename, 'wb')
        f.write(u.read())
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
    st = set(torrents)
    print(imgs, st)
    for img in imgs:
        down_link(img, dirname + '/' + os.path.basename(img))
    for t in st:
        down_link(base_url + t[0], dirname + '/' + t[1])

    return



def down_link_imgs_torrents(topic):
    print('GET:', topic)
    dirname = get_valid_filename(topic['title'])
    os.makedirs(dirname, exist_ok = True)
    
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
    topics_html = re.findall('<tbody.*?normalthread.*?>.*?</tbody>', content, re.M | re.S)
    #print(topics_html)
    topics = dict()
    # GET: 1-url 2-title 3-star 4-comment 5-view 6-time
    p = '<span id.*?<a href=\"(?P<url>.*?)\".*?>(?P<title>.*?)</a>.*?<img.*?<td.*?author.*?img.*?>.*?(?P<star>\d+).*?</cite>.*?<td.*?nums\">.*?(?P<comment>\d+).*?<em>(?P<view>\d+).*?lastpost.*?<a href.*?>(?P<time>.*?)</a>'
    for h in topics_html:
        gd = re.search(p, h, re.M | re.S).groupdict()
        gd['url'] = base_url + gd['url']
        topics[gd['title']] = gd
        print(topics[gd['title']])

    for i in topics:
        down_link_imgs_torrents(topics[i])

    return topics

def install_proxy():
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
    
    url = 'http://38.103.161.147/forum/thread-4917240-1-1.html'
    down_imgs_from_url(url)

def main():
    install_proxy()
    base_forum_url = 'http://38.103.161.147/forum/forum-{0}-{1}.html'
    
    forum_ids = {'Asia Censored' : 230, 'Asia Uncensored' : 143}
    #urls = map(base_forum_url.format, forum_ids.values())

    wtfdir = 'wtf'
    os.makedirs(wtfdir, exist_ok = True)
    os.chdir(wtfdir)
    end = 4
    for forum_id in forum_ids.values(): #or using thread
        for page in range(50,400,25):
            begin = end + 1
            end = page
            #t = ThreadUrl(base_forum_url.format(forum_id, page))
            t = ThreadUrl(base_forum_url, forum_id, begin, end)
            t.start()

start = time.time()
if __name__ == '__main__':
    main()
print("Elapsed Time:", (time.time() - start))