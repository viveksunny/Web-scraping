import json
import scrapy


class ChartlinkscrapperSpider(scrapy.Spider):
    name = "chartlink"
    # allowed_domains = ["s"]
    start_urls = ['https://chartink.com/screener/d-up-48']
    headers = {'User-Agent':
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/126.0.0.0 '
                  'Safari/537.36',
               'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Sec - Fetch - Site': 'same - origin',
               'X-Csrf-Token': 'QeMleTmt2s9EMsnsuXkU8DNP5dwGGSFUQH5M33kh',
               'X - Requested - With': 'XMLHttpRequest',
               'Accept-Language': 'en-US,en;q=0.5',
               'Accept - Encoding': 'gzip, deflate, br, zstd',
               'Origin': 'https://chartink.com',
               'Content - Length': 511
               }

    def parse(self, response):
        url = 'https://chartink.com/screener/process'
        response = scrapy.Request(url=url, headers=self.headers, callback=self.parse_api, method='POST')
        yield response

    def parse_api(self, response):
        raw_data = response.body
        data = json.load(raw_data)
        for element in data:
            yield {'Stock_Name': element["nsecode"],
                   'Stock_Price': element["close"]}



# scrapy startproject chartlinkscrapper -- to create project with all objects
# scrapy genspider chartlinkscrapper <Base URL> -- to create a small project with template
# scrapy runspider chartlinkscrapper.py -- to run the code