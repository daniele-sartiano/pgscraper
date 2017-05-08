#!/usr/bin/env python

import sys
import scrapy
import tldextract

class PGScraper(scrapy.Spider):
    name = 'pgscraper'
    download_delay = 2

    def __init__(self, url, n, max):
        self.url = url
        self.n = n
        self.max = int(max)
        
    def start_requests(self):
        p = ''
        c = 1
        while c < self.<max:
            yield scrapy.Request(url=self.url % (p, self.n), callback=self.parse)
            c += 1
            p = 'p-%s' % c

    def parse(self, response):
        for el in response.xpath('//*//a[contains(@data-pag, "www")]/@href'):
            u = el.extract()
            tld = tldextract.extract(u)
            if tld.suffix == 'it':
                yield {'url': '%s.%s' % (tld.domain, tld.suffix)}
    

if __name__ == '__main__':
    main()
