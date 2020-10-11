import scrapy
import numpy as np

class WikihowScraper(scrapy.Spider):
    name = 'wikihow'
    start_urls = [
        'https://www.wikihow.com/Deal-with-Mind-Games'
    ]

    def parse(self, response):
        title = response.css('#section_0 a::text').get()
        heading = response.css('.in-block .mw-headline::text').getall()
        body = response.css('.whb::text').getall()
        steps = response.css('.step_num::text').getall()

        positions = np.argwhere(np.array(steps) == '1')
        positions = [x[0] for x in positions]

        print('-'*25)
        print('-'*25)
        print(steps)
        print(positions)
        print('-'*25)
        print('-'*25)