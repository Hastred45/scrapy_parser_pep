import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    '''Паук собирающий информацию о версиях PEP'''
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        '''Находит все ссылки на страницы версий PEP и передает в parse_pep'''
        for pep_link in response.css(
                'section#numerical-index td a::attr(href)').getall():
            yield response.follow(pep_link + '/', callback=self.parse_pep)

    def parse_pep(self, response):
        '''Находит номер, название и статус PEP. Создает объект Items'''
        pep = response.css('ul.breadcrumbs > li + li + li::text').get()
        data = {
            'number': pep[4:],
            'name': response.css('.page-title::text').get(),
            'status': response.css('abbr::text').get()
        }
        yield PepParseItem(data)
