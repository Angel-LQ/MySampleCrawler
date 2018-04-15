from MySampleCrawler import url_manager, html_downloader, html_outputer, html_parser


class SpiderMain():
    def __init__(self):  # 初始化
        self.urls = url_manager.UrlManager()  # url管理器
        self.downloader = html_downloader.HtmlDownloader()  # 下载器
        self.parser = html_parser.HtmlParser()  # 解析器
        self.outputer = html_outputer.HtmlOutputer()  # 输出器

    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('No.' + str(count), 'craw', new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                count += 1
                if count > 100: #定义爬取的页面数量
                    break
            except Exception as e:
                print('craw failed', str(e))

        self.outputer.output_html()

if __name__ == "__main__":
    root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)