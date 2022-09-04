import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
       # heading_tag = response.xpath("//h1/a/text()").extract_first()
       # tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()

        #  yield {'Heading tag': heading_tag, "Tags": tags}

        # getting all the quotes
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//*[@itemprop="text"]/text()').extract()
            author = quote.xpath('.//*[@itemprop="author"]/text()').extract()
            tags = quote.xpath('.//*[@class="tag"]/text()').extract()

            print('\n')
            print(text)
            print(author)
            print(tags)
            print('\n')

        next_page_url = response.xpath(
            '//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)
