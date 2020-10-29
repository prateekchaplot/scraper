import scrapy
from ..items import AmazonItem

def savefile(text, filename):
  with open(filename, 'a+') as f:
            f.write(text)

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
      'https://www.amazon.in/gp/goldbox/ref=gbps_ftr_s-5_859c_sort_RELV?gb_f_c2xvdC01=dealTypes:LIGHTNING_DEAL%252CBEST_DEAL,includedAccessTypes:KINDLE_CONTENT_DEAL,sortOrder:BY_SCORE&pf_rd_p=daa47517-5bef-4e97-b82e-ec3e7d37859c&pf_rd_s=slot-5&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=8N9MMA4T1T7F3E5W4WCB&ie=UTF8'
      ]

    def parse(self, response):
        items = AmazonItem()

        name = response.css('#dealTitle .a-declarative').extract() # '#dealTitle'
        price = response.css('.dealPriceText').extract()
        mrp = response.css('.a-text-strike').css('::text').extract()
        image = response.css('.backGround').css('::attr(src)').extract()

        print(str(name) + '\n' + str(price) + '\n' + str(mrp) + '\n' + str(image) + '\n---\n\n')

        items['name'] = name
        items['price'] = price
        items['mrp'] = mrp
        items['image'] = image

        # text = str(name) + '\n' + str(price) + '\n' + str(mrp) + '\n' + str(image) + '\n---\n\n'
        savefile(response.text, 'amazon.txt')