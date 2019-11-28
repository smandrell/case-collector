# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

# documentation: http://crawl.blog/scrapy-loop/ for looping the crawler using Twisted rules

from scrapy.crawler import CrawlerProcess
import case_collector.case_collector.spiders.record_scraper as record_scraper
import case_collector.case_collector.query_generator as query_gen

process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'items.json'
})

queries = query_gen.generate(3)
print(len(queries))
query_index = len(queries) // 5
print(query_index)


def crawl(result, spider):
    # multithread and paralellize this
    # implement how to change SEARCH_TEXT in record_scraper
    global query_index
    while query_index >= 198:
        record_scraper.change_query_term(queries[query_index])
        deferred = process.crawl(spider)
        query_index -= 1
        deferred.addCallback(crawl, spider)
        return deferred


crawl(None, record_scraper.CourtRecordScraper)
process.start()  # the script will block here until the crawling is finished
record_scraper.display_dfs()
