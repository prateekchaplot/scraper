import scrapy
# import numpy as np

class WikihowScraper(scrapy.Spider):
    name = 'wikihow'
    start_urls = [
        'https://www.wikihow.com/Think-Positively',
        'https://www.wikihow.com/Improve-Critical-Thinking-Skills',
        'https://www.wikihow.com/Teach-Critical-Thinking',
        'https://www.wikihow.com/Deal-with-Mind-Games'
    ]

    def parse(self, response):
        title = response.css('#section_0 a::text').get()
        headings = response.css('.in-block .mw-headline::text').getall()
        body = response.css('.whb::text').getall()
        steps = response.css('.step_num::text').getall()

        text = str('[{}]({})\n===\n').format(title, response.url)
        for heading in headings:
            text += heading + '\n---\n'
            # text += body[0] + '\n'

            # i = 1
            i = 0
            while True:
                text += body[i] + '\n'
                i += 1
                if (steps[i] == None or steps[i] == '1'):
                    break

            text += '\n'

        with open('wikihow.txt', 'a+') as f:
            f.write(text)