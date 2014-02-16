import requests
from bs4 import BeautifulSoup
import re
import os
import thread
import time

def validate_title(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/\:*?"<>|'
    new_title = re.sub(rstr, "", title)
    return new_title

def ensure_dir(f):
    print f
    if not os.path.exists(f):
        os.makedirs(f)

def get_soup_from_url(url):
    page = requests.get(url)
    return BeautifulSoup(page.content)

def get_img_from_url(url):
    soup = get_soup_from_url(url)
    img = soup.find_all('img', src=re.compile('imgsrc'))
    return img

def down_links_to_folder(links, folder):
    for i, link in enumerate(links):
        r = requests.get(link)
        if r.status_code == 200:
            with open(folder + '\\' + str(i) + '.jpg', 'wb') as f:
                for chunk in r.iter_content():
                    f.write(chunk)

def get_tieba_img_url_from_url(url):
    imgs = {}
    links = set()

    soup = get_soup_from_url(url)
    dirname = validate_title(soup.title.text.encode('gb18030'))
    loc = os.getcwd() + '\\' + dirname
    imgs[1] = get_img_from_url(url)

    if imgs[1]:
        ensure_dir(loc)

    total_page_div = soup.find('span', class_='red')
    if (hasattr(total_page_div, 'text')):
        total_page = int(total_page_div.text)
    else:
        total_page = 1

    for i in range(2, total_page + 1):
        imgs[i] = get_img_from_url(url + "&pn=" + str(i))

    for i in imgs:
        for j in imgs[i]:
            links.add(j.get('src'))

    thread.start_new(down_links_to_folder, (links, dirname))

    return links

baidu_base_url = 'http://tieba.baidu.com'
baidu_homepage = requests.get("http://tieba.baidu.com/f?ie=utf-8&kw=%E5%A7%90%E8%84%B1")
soup = BeautifulSoup(baidu_homepage.content)

titles = soup.find_all('a', target="_blank", class_="j_th_tit")
urls = {}
for i, title in enumerate(titles):
    urls[i] = baidu_base_url + title.get('href')
    print urls[i], title.text.encode('gb18030')

for i in urls:
    thread.start_new(get_tieba_img_url_from_url, (urls[i] + '?see_lz=1',))

#time.sleep(100000)
