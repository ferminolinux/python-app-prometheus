from flask import Flask
from flask import render_template
from flaskext.markdown import Markdown
from werkzeug.exceptions import NotFound
from metrics.counters import HTTP_REQUESTS_TOTAL, HTTP_EXCEPTIONS_TOTAL
from metrics.gauge import HTTP_REQUEST_IN_PROGRESS
from metrics.summary import HTTP_REQUEST_LATENCY
from prometheus_client import generate_latest
from time import sleep


class WebApp(Flask):
    def __init__(self):
       super().__init__(__name__)
       Markdown(self)
       
       # PROPERTIES
       self._request_interval = None
       
       ## MAP URLS
       self.add_url_rule('/', 'index', self.__index)
       self.add_url_rule('/index', 'index', self.__index)
       self.add_url_rule('/wth', 'wth', self.__wth)
       self.add_url_rule('/part/<num>', 'part', self.__part)
       self.add_url_rule('/metrics', 'metrics', self.__metrics)
       
    
    @HTTP_REQUEST_LATENCY.labels('jjoba', '/').time()
    @HTTP_REQUEST_IN_PROGRESS.labels("jojoba", '/').track_inprogress()
    def __index(self):
        self.__sleep_request()
        HTTP_REQUESTS_TOTAL.labels('jojoba', '/', 200).inc()
        return render_template('index.html'), 200
    
    @HTTP_REQUEST_LATENCY.labels('jjoba', '/').time()
    @HTTP_REQUEST_IN_PROGRESS.labels("jojoba", '/').track_inprogress()
    def __wth(self):
        self.__sleep_request()
        HTTP_REQUESTS_TOTAL.labels('jojoba', '/wth', 200).inc()
        tmp_md = self.__read_md('templates/markdown/jojoba-description.md')
        
        return render_template('md.html', md=tmp_md), 200
        
        
    def __read_md(self, file: str) -> str:
            with open(file, 'r') as f:
                tmp_md = f.read()
            return  tmp_md
     
    @HTTP_REQUEST_LATENCY.labels('jjoba', '/').time()
    @HTTP_REQUEST_IN_PROGRESS.labels("jojoba", '/').track_inprogress()   
    @HTTP_EXCEPTIONS_TOTAL.labels('jojoba', '/part/', 404).count_exceptions()
    def __part(self, num: str):
        self.__sleep_request()
        tmp_md = None
        
        if num == '1':
            HTTP_REQUESTS_TOTAL.labels('jojoba', '/part/1', 200).inc()
            tmp_md = self.__read_md('templates/markdown/pb-description.md')
        elif num == '2':
            HTTP_REQUESTS_TOTAL.labels('jojoba', '/part/2', 200).inc()
            tmp_md = self.__read_md('templates/markdown/bt-description.md')
        elif num == '3':
            HTTP_REQUESTS_TOTAL.labels('jojoba', '/part/3', 200).inc()
            tmp_md = self.__read_md('templates/markdown/st-description.md')
        elif num == '4':
            HTTP_REQUESTS_TOTAL.labels('jojoba', '/part/4', 200).inc()
            tmp_md = self.__read_md('templates/markdown/du-description.md')
        elif num == '5':
            HTTP_REQUESTS_TOTAL.labels('jojoba', '/part/5', 200).inc()
            tmp_md = self.__read_md('templates/markdown/va-description.md')
        elif num == '6':
            HTTP_REQUESTS_TOTAL.labels('jojoba', '/part/6', 200).inc()
            tmp_md = self.__read_md('templates/markdown/so-description.md')
        else:
            raise NotFound
        
        return render_template('md.html', md=tmp_md), 200
    
    def __metrics(self):
        return generate_latest()
    
    def set_request_interval(self, num: int):
        self._request_interval = num
        
    def __sleep_request(self):
        sleep(self._request_interval)