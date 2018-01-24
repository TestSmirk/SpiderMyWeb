import scrapy


file = open("spiderResult.txt","w")

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://testsmirk.com']

    def parse(self, response):
        print("start 1 " + str(response))
        for title in response.xpath("//header[@class='post-header']"):
            file.write(title.xpath("h2/a/text()").extract_first()+"\n")
            yield {'title': title.xpath("h2/a/text()").extract_first()}

        for next_page in response.xpath("//nav[@class='pagination']/a"):
            print("next_page " + str(next_page))
            yield response.follow(next_page, self.parse)
