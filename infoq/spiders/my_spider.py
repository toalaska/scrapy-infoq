import scrapy

from infoq.items import InfoqItem




class DmozSpider(scrapy.Spider):
    name = "my_spider"
    allowed_domains = ["www.infoq.com"]
    start_urls = [
        "http://www.infoq.com/cn/presentations/1876",

    ]

    _page=1876

    def _get_next_url(self,cur_url):
        DmozSpider._page+=1
        url="/".join(cur_url.split("/")[:-1])+ ("/%s" % DmozSpider._page)
        print("==url",url)
        return url


    def parse(self, response):
        for sel in response.css(".news_type_video"):
            item=InfoqItem()
            item['title']=sel.css("h2 a::text").extract_first().strip()
            item['url']=sel.css("h2 a::attr(href)").extract_first()
            item['cover']=sel.css("a > div > img::attr(src)").extract_first()
            item['author']=sel.css("span.author > span > span > a::text").extract_first()
            yield item

        print("response===", dir(response))
        print("response===", response.url)
        url = self._get_next_url(response.url)
        yield scrapy.Request(url, callback=self.parse)