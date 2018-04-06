import scrapy
from scrapy.linkextractors import LinkExtractor

file = open("spiderResult.txt","w")

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://testsmirk.com']

    def parse(self, response):
        print("start 1 " + str(response))

        for title in response.xpath("//*[@class='title text-center']"):
            file.write(title.xpath("a/text()").extract_first()+"\n")
            yield response.follow(title.xpath("a/@href").extract_first(), callback=self.getContent)

        for next_page in response.xpath("//*[@id='articlepage']/a"):
            print("next_page " + str(next_page))
            yield response.follow(next_page, self.parse)
    def getContent(self,response):
        images = response.xpath("//*[@class='gruber-markdown']/img")
        print("response "+str(images))
        for url in images:
            print("url "+str(url))
