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


def crawl(result, spider):
    queries = query_gen.run_query_generator()
    i = len(queries) / 5
    # multithread and paralellize this
    # implement how to change SEARCH_TEXT in record_scraper
    while i >= 198:
        record_scraper.change_query_term(queries[i])
        deferred = process.crawl(spider)
        i -= 1
        deferred.addCallback(crawl, spider)
        return deferred


crawl(None, record_scraper.CourtRecordScraper)
process.start()  # the script will block here until the crawling is finished
record_scraper.display_dfs()
