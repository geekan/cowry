# -*- coding: gbk -*-

import re
import sys
import os
import urllib.request

urlopen = urllib.request.urlopen
request = urllib.request.Request

def down_link(url, filename):
    return

def get_links_from_page(url):
    print('GET:' + url)
    
    content = urlopen(url).read().decode('gbk')
    #print(content)
    topics_html = re.findall('<tbody.*?normalthread.*?>.*?</tbody>', content, re.M | re.S)
    #print(topics_html)
    topics = dict()
    # GET: 1-url 2-title 3-star 4-comment 5-view 6-time
    p = '<span id.*?<a href=\"(?P<url>.*?)\".*?>(?P<title>.*?)</a>.*?<img.*?<td.*?author.*?img.*?>.*?(?P<star>\d+).*?</cite>.*?<td.*?nums\">.*?(?P<comment>\d+).*?<em>(?P<view>\d+).*?lastpost.*?<a href.*?>(?P<time>.*?)</a>'
    for i, h in enumerate(topics_html):
        topics[i] = re.search(p, h, re.M | re.S).groupdict()
        print(topics[i])

    return topics


def main():
    base_forum_url = 'http://38.103.161.147/forum/forum-{0}-{1}.html'
    
    forum_ids = {'Asia Censored' : 230, 'Asia Uncensored' : 143}
    #urls = map(base_forum_url.format, forum_ids.values())

    for forum_id in forum_ids.values(): #or using thread
        for page in range(5,1000):
            get_links_from_page(base_forum_url.format(forum_id, page))


if __name__ == '__main__':
    main()