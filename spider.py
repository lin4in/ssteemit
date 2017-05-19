# Reserved
# Reserved

import scrapy



class steemit(scrapy.Spider):
    name = 'steemitspyder'
    allowed_domains = ['steemit.com']
    start_urls = ['https://steemit.com/']

    def parse(self, response):
        for postSummary in response.css('article.PostSummary'):
            voting=float(postSummary.css('span.integer::text').extract_first()+postSummary.css('span.decimal::text').extract_first())
            yield {'title': postSummary.css('div.PostSummary__content h3.entry-title a::text').extract_first(),
                   'url': postSummary.css('div.PostSummary__content h3.entry-title a::attr(href)').extract_first(),
                   'imageurl': postSummary.css('span.PostSummary__image::attr(style)').re_first(r'https[^\"\;]*'),
                   'entryContent': postSummary.css('div.PostSummary__content div.PostSummary__body a::text').extract_first(),
                   'Voting': voting,
                   'votes': int(postSummary.css('span.VotesAndComments__votes::text').re_first(r'\d.*')),
                   'comments': int(postSummary.css('span.VotesAndComments__comments a::text').re_first(r'\d.*')),
                   'updated': postSummary.css('span.updated::attr(title)').extract_first(),
                   'author': postSummary.css('span.author strong::text').extract_first(),
                   'trending': postSummary.css('span.vcard strong a::text').extract_first()
                   }

        # next_page = response.css('div.prev-post > a ::attr(href)').extract_first()
        # if next_page:
            # yield scrapy.Request(response.urljoin(next_page), callback=self.parse)



