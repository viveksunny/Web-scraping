import json
import scrapy


class ChartlinkscrapperSpider(scrapy.Spider):
    name = "chartlink"
    # allowed_domains = ["s"]
    start_urls = ['https://chartink.com/screener/d-up-48']
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Length': '511',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        #'Cookie': '_ga=GA1.2.1411384014.1720223851; _gid=GA1.2.1332128089.1720223851; _gat=1; _ga_7P3KPC3ZPP=GS1.2.1720223852.1.0.1720223852.0.0.0; XSRF-TOKEN=eyJpdiI6Im9GbGJMdUpuZWsySStEOUJzSHhrbXc9PSIsInZhbHVlIjoic2hEdkIyZXVQMlZTNnpoWUxxQ1puK1Q4SVlKVjZBdlY4NGpqbTBQankwSUtCclA0MUFHNmVMY0JXMmc0YnNyMjFxVWZ0Q1I4bGdmenYwdThoM1lsRERHaHdBcHFWeHhqZTdyOXVaYzFrb1NlUzhyUlRVRTh1TGh3bGJyYnRpUUgiLCJtYWMiOiJmMzNmYTEyNDdhOTQ0NGM4MjVmN2M0NGUyNzc1ODgyOTUxM2M3MWU3YjFkNWQ3NWUzOWRjYTRkMmM2Njk4YWM3IiwidGFnIjoiIn0%3D; ci_session=eyJpdiI6InBzSlJOazFlbCtMU3RGY2RqRzVid2c9PSIsInZhbHVlIjoiKzdTV1RVM28wY3V6RStSRzZzQU11Rnpzc20rUzlwRGIrZlBhV2hhVmMrc2tCS0hVNGpUV3ZLN2IrcVBzMVBQZ1dodk1nN0dtK0FLcUg5Um1xbUdvZmcxdHRDaUM3ejE4YjVVSXBrSHFHRFVoVVpaOGtBNSt3ZFdBdmZWYXQ5cEgiLCJtYWMiOiJkZmQ4ZTAwMDdmZWEzNWI5OGFmZjk5MjlhYjEyNmI4NTg3ZGRjZDAwYjY4ZDM2OTU3MjJiYTdjYjQ2YzllMWZmIiwidGFnIjoiIn0%3D',
        'Origin': 'https://chartink.com',
        'Priority': 'u=1, i',
        'Referer':'https://chartink.com/screener/d-up-48',
        # 'Sec-Ch-Ua: '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': 'Windows',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        #'X-Csrf-Token': 'zckRGcNeC4YRtLzXTG3q5BG98gbRaldhw3J2QZb3',
        'X-Requested-With': 'XMLHttpRequest'
               }

    def parse(self, response):
        url = 'https://chartink.com/screener/process'
        payload_body = {'scan_clause': '(+%7Bcash%7D+(+(+%7Bcash%7D+(+latest+close+%3E+latest+ema(+close%2C20+)+and+1+day+ago++close+%3C%3D+1+day+ago++ema(+close%2C20+)+and+latest+close+%3E+latest+ema(+close%2C50+)+and+1+day+ago++close+%3C%3D+1+day+ago++ema(+close%2C50+)+)+)+)+)+',
                        'debug_clause': 'groupcount(+1+where+++++daily+close+%3E+daily+ema(+close%2C20+)+and+1+day+ago++close+%3C%3D+1+day+ago++ema(+close%2C20+))%2Cgroupcount(+1+where+++++daily+close+%3E+daily+ema(+close%2C50+)+and+1+day+ago++close+%3C%3D+1+day+ago++ema(+close%2C50+))'}
        response = scrapy.Request(url=url, headers=self.headers, callback=self.parse_api, method='POST', body=json.dumps(payload_body))
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