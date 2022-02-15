import scrapy 

class CisaSpider(scrapy.Spider):
    name = 'cisa'
    start_urls = [
        'https://www.cisa.gov/uscert/ncas/current-activity'
    ]
    def parse(self, response): 
        for bulletin in response.css("div.views-row"):
            yield {
                'source': 'cisa',
                'link' : "https://www.cisa.gov/uscert"+bulletin.xpath("descendant-or-self::h3/span/a/@href").get(),
                'date' : bulletin.xpath("descendant-or-self::div[contains(@class,'entry-date')]/span[2]/text()").get().replace("\n","").replace("\t","").replace("\r","").replace("  ",""),
                'title' : bulletin.xpath("descendant-or-self::h3/span/a/text()").get().replace("\n","").replace("\t","").replace("\r","").replace("  ",""),
                'description' : bulletin.xpath('descendant-or-self::div[contains(@class,"field-content")]/p').get().replace("\n","").replace("\t","").replace("\r","").replace("  ",""),
            }
