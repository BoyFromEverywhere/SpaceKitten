# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
import re
from Sex_text.items import Blue_book
from Sex_text.md5 import md5_common

class FourtigerSpider(scrapy.Spider):
    name = 'fourtiger'
    allowed_domains = ['https://www.381abc.com/']
    start_urls = ['https://www.381abc.com/Html/84/']

    def parse(self, response):

        #获取该网站具体文章的url
        sex_urls = response.css('li a::attr(href)').extract()
        for the_url in sex_urls:
            yield Request(url=parse.urljoin('https://www.381abc.com',the_url), callback=self.parse_page,dont_filter=True)

        #提取下一页
        next_pages = response.css('a[class*=next]::attr(href)').extract_first()
        if next_pages:
            yield Request(url=parse.urljoin('https://www.381abc.com', next_pages), callback=self.parse,dont_filter=True)

    def parse_page(self,response):
        BlueBook = Blue_book()
        title = response.xpath('/html/head/title/text()').extract_first("标题里啥也没找到")
        print(title)
        #title = response.css('.page_title h1::text').extract()
        content = response.css('.content font::text').extract()
        content = ' '.join(content).strip(' ')

        BlueBook['title'] = title
        BlueBook['content'] = content
        BlueBook['the_url'] = response.url
        #BlueBook['the_url_id'] = md5_common(response.url)

        yield BlueBook