# coding:UTF8
from baike_spider import html_download, url_manager, html_parser, html_outputer

class SpiderMain(object):
    def __init__(self):#初始化
        self.urls = url_manager.UrlManager()
        self.downloader = html_download.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.htmlOutputer()
            


    
    
    def craw(self, root_url):
        count =1 #记录当前爬取的是第几个URL（记录用）
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d :%s'%(count,new_url)#记录用
                html_cont = self.downloader.Download(new_url) #下载器
                new_urls,new_data = self.parser.parse(new_url,html_cont) #解析器
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data) #输出器
                
                if count ==50:  #爬取1000个失中断
                    break 
                count = count +1
            except:
                print 'craw faild'
            
        self.outputer.outputer_html()
    
    



if  __name__=="__main__":  #��дmain����
    root_url = "http://baike.baidu.com/view/21087.htm"  #���url
    obj_spider = SpiderMain() #����һ��spider
    obj_spider.craw(root_url)
    