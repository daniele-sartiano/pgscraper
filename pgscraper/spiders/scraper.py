#!/usr/bin/env python

import sys
import scrapy
import tldextract

class PGScraper(scrapy.Spider):
    name = 'pgscraper'
    download_delay = 2
    
    def start_requests(self):
        URL = 'https://www.paginegialle.it/ricerca/informatica/%s?mr=%s'
        n = 50
        p = ''
        c = 1
        while c:
            yield scrapy.Request(url=URL % (p, n), callback=self.parse)
            c += 1
            p = 'p-%s' % c
            if c > 600:
                c = None

    def parse(self, response):
        for el in response.xpath('//*//a[contains(@data-pag, "www")]/@href'):
            u = el.extract()
            tld = tldextract.extract(u)
            if tld.suffix == 'it':
                yield {'url': '%s.%s' % (tld.domain, tld.suffix)}
    

if __name__ == '__main__':
    main()
