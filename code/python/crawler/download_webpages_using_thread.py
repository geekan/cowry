# -*- coding:utf-8 -*-   
import urllib, httplib   
import thread   
import time   
from Queue import Queue, Empty, Full   
HEADERS = {"Content-type": "application/x-www-form-urlencoded",   
                        'Accept-Language':'zh-cn',   
                        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0;Windows NT 5.0)',   
                        "Accept": "text/plain"}   
UNEXPECTED_ERROR = -1  
POST = 'POST'  
GET = 'GET'  
def base_log(msg):   
    print msg   
def base_fail_op(task, status, log):   
    log('fail op. task = %s, status = %d'%(str(task), status))   
def get_remote_data(tasks, results, fail_op = base_fail_op, log = base_log):   
    while True:   
        task = tasks.get()   
        try:   
            tid = task['id']   
            hpt = task['conn_args'] # hpt <= host:port, timeout   
        except KeyError, e:   
            log(str(e))   
            continue  
        log('thread_%s doing task %d'%(thread.get_ident(), tid))   
        #log('hpt = ' + str(hpt))   
        conn = httplib.HTTPConnection(**hpt)   
               
        try:   
            params = task['params']   
        except KeyError, e:   
            params = {}   
        params = urllib.urlencode(params)   
        #log('params = ' + params)   
           
        try:   
            method = task['method']   
        except KeyError:   
            method = 'GET'  
        #log('method = ' + method)   
           
        try:   
            url = task['url']   
        except KeyError:   
            url = '/'  
        #log('url = ' + url)   
           
        headers = HEADERS   
        try:   
            tmp = task['headers']   
        except KeyError, e:   
            tmp = {}   
        headers.update(tmp)   
        #log('headers = ' + str(headers))   
        headers['Content-Length'] = len(params)   
           
        try:   
            if method == POST:   
                conn.request(method, url, params, headers)   
            else:   
                conn.request(method, url + params)   
            response = conn.getresponse()   
        except Exception, e:   
            log('request failed. method = %s, url = %s, params = %s headers = %s'%(   
                        method, url, params, headers))   
            log(str(e))   
            fail_op(task, UNEXPECTED_ERROR, log)   
            continue  
               
        if response.status != httplib.OK:   
            fail_op(task, response.status, log)   
            continue  
               
        data = response.read()   
        results.put((tid, data), True)   
           
class HttpPool(object):   
    def __init__(self, threads_count, fail_op, log):   
        self._tasks = Queue()   
        self._results = Queue()   
           
        for i in xrange(threads_count):   
            thread.start_new_thread(get_remote_data,    
                                                            (self._tasks, self._results, fail_op, log))   
               
    def add_task(self, tid, host, url, params, headers = {}, method = 'GET', timeout = None):   
        task = {   
            'id' : tid,   
            'conn_args' : {'host' : host} if timeout is None else {'host' : host, 'timeout' : timeout},   
            'headers' : headers,   
            'url' : url,   
            'params' : params,   
            'method' : method,   
            }   
        try:   
            self._tasks.put_nowait(task)   
        except Full:   
            return False  
        return True  
           
    def get_results(self):   
        results = []   
        while True:   
            try:   
                res = self._results.get_nowait()   
            except Empty:   
                break  
            results.append(res)   
        return results   
           
def test_google(task_count, threads_count):   
    hp = HttpPool(threads_count, base_fail_op, base_log)   
    for i in xrange(task_count):   
        if hp.add_task(i,   
                'www.google.cn',   
                '/search?',   
                {'q' : 'lai'},   
#               method = 'POST'   
                ):   
            print 'add task successed.'  
               
    while True:   
        results = hp.get_results()   
        if not results:   
            time.sleep(1.0 * random.random())   
        for i in results:   
            print i[0], len(i[1])   
#           print unicode(i[1], 'gb18030')   
               
if __name__ == '__main__':   
    import sys, random   
    task_count, threads_count = int(sys.argv[1]), int(sys.argv[2])   
    test_google(task_count, threads_count)  
