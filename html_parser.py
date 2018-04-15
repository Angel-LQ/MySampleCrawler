import re
import urllib.parse
from bs4 import BeautifulSoup

class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/"))
        # 网址有变，表达式做了调整
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            # Py3中用到的模块名称变为urllib.parse
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        '''
        title 的 html 格式
        
        < dd class ="lemmaWgt-lemmaTitle-title" >
        < h1 > Python < / h1 >
        < h2 >（计算机程序设计语言） < / h2 >
        < / dd >
        
        summary 的 html 格式
        
        <div class="lemma-summary" label-module="lemmaSummary">
        ......
        '''

        title = soup.find('dd', class_ = "lemmaWgt-lemmaTitle-title").find('h1')
        summary = soup.find('div', class_='lemma-summary')

        res_data['url'] = page_url
        res_data['title'] = title.get_text()
        res_data['summary'] = summary.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data


